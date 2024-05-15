import numpy as np

from data_extraction import get_full_scope, get_salaires
from referentials import REFERENTIALS, complement_dispositif_public_iae
from sqlalchemy import create_engine, engine

import pandas as pd

# get scope
# split pop (= get IAE, keep IAE end date, remove IAE and time before)
# Apply referentials
#

def pipeline(engine):
    full_scope = get_full_scope(engine)
    future_contracts, no_future_contracts = split_contracts(full_scope)
    transformed_contracts = transform_contracts(future_contracts, engine)

    return transformed_contracts, no_future_contracts


def split_contracts(full_scope):

    full_scope.loc[full_scope['date_fin_contrat'] == '2999-12-31 00:00:00', 'date_fin_contrat'] = np.nan
    full_scope['date_fin_contrat'] = pd.to_datetime(full_scope['date_fin_contrat'].fillna(full_scope['date_fin_previsionnelle']))
    full_scope['is_iae_contract'] = full_scope['complement_dispositif_public'].isin(complement_dispositif_public_iae)
    iae_contracts = full_scope.loc[full_scope['is_iae_contract'], ['id_assure', 'date_fin_contrat']]
    iae_contracts = iae_contracts.groupby('id_assure').max().reset_index().rename({"date_fin_contrat": "date_fin_contrat_iae"}, axis=1)
    non_iae_contract = full_scope[~full_scope['is_iae_contract']]
    non_iae_contract = non_iae_contract.merge(iae_contracts, how='left', on='id_assure')
    non_iae_contract['date_debut_contrat'] = pd.to_datetime(non_iae_contract['date_debut_contrat'])

    no_post_iae_contracts = iae_contracts.loc[~iae_contracts['id_assure'].isin(non_iae_contract['id_assure'])]
    post_iae_contracts = non_iae_contract.loc[non_iae_contract['date_debut_contrat'] >= non_iae_contract['date_fin_contrat_iae']]

    return post_iae_contracts, no_post_iae_contracts


def transform_contracts(post_iae_contracts, engine, months_after=12):

    # Trouver tous les contrats commençant au plus tard après x mois

    post_iae_contracts = post_iae_contracts.loc[
        (post_iae_contracts['date_debut_contrat'] - post_iae_contracts['date_fin_contrat_iae']).dt.days < months_after*30
    ].reset_index(drop=True)

    # Calculer le salaire brut pour chaque couple (salarié, employeur)

    salaires = get_salaires(engine, post_iae_contracts['id_employeur_assure'].unique().tolist())
    post_iae_contracts = post_iae_contracts.merge(salaires, on='id_employeur_assure')

    # Calculer le nombre de mois travaillés pour chaque contrat

    post_iae_contracts['mois_travailles'] = np.minimum(
            post_iae_contracts['date_fin_contrat'] - post_iae_contracts['date_debut_contrat'],
            pd.Timestamp.now() - post_iae_contracts['date_debut_contrat']
    ).dt.days/30

    # Calculer la quotite pour chaque contrat

    post_iae_contracts['pourcentage_temps'] = post_iae_contracts['quotite'].astype(float).fillna(0)/post_iae_contracts['quotite_categorie'].astype(float).fillna(1)
    post_iae_contracts.loc[post_iae_contracts['pourcentage_temps'] > 1, 'pourcentage_temps'] = 1
    post_iae_contracts.loc[post_iae_contracts['pourcentage_temps'] < 0, 'pourcentage_temps'] = 0

    # Mapper le type de contrat (CDD CDI etc)

    post_iae_contracts['nature_contrat'] = post_iae_contracts['nature_contrat'].map(REFERENTIALS['nature_contrat'])

    # Si rupture, indiquer le motif

    post_iae_contracts['motif_rupture'] = post_iae_contracts['motif_rupture'].fillna('0').astype(int).map(REFERENTIALS['motif_rupture'])

    return post_iae_contracts


if __name__ == '__main__':
    import dotenv
    config = dotenv.dotenv_values()
    engine = create_engine(config['CONN_HACKATHON_GEOFFREY'])
    contrats_12_mois, _ = pipeline(engine)
    contrats_12_mois.to_sql("contrats_12_mois_apres_insertion", con=engine, schema='udeb9', if_exists='replace')
