import logging
import pandas as pd

def get_full_scope(engine):

    query = """
        SELECT
            ddadtemployeur_assure.id_assure,
            ddadtemployeur_assure.id_employeur,
            id_employeur_assure,
            date_debut_contrat,
            date_fin_contrat,
            date_fin_previsionnelle,
            statut_rc,
            quotite,
            quotite_categorie,
            modalite_temps,
            SUBSTRING(pcs_ese, 1, 1) AS pcs,
            nature_contrat,
            taux_accident_travail,
            motif_rupture,
            date_naissance,
            sexe_assure,
            SUBSTRING(et_ad_code_postal, 1, 2) as departement_et,
            complement_dispositif_public,
	        dispositif_politique,
	        unite_mesure,
        	case 
                when contrats_assures_en_insertion.date_fin_contrat is null or contrats_assures_en_insertion.date_fin_contrat::timestamp <= '06/01/2023' then contrats_assures_en_insertion.date_fin_contrat::timestamp - contrats_assures_en_insertion.date_debut_contrat::timestamp
                when contrats_assures_en_insertion.date_fin_contrat::timestamp > '06/01/2023' and (date_part('day','06/01/2023' - contrats_assures_en_insertion.mois_declaration::timestamp) < 90) then '06/01/2023' - contrats_assures_en_insertion.date_debut_contrat::timestamp
                else (date_trunc('month', contrats_assures_en_insertion.mois_declaration::timestamp) - interval '1 day' + interval '1 month') - contrats_assures_en_insertion.date_debut_contrat::timestamp
            end as anciennete_contrat

        FROM udeb9.contrats_assures_en_insertion
        LEFT JOIN ddadtemployeur_assure ON ddadtemployeur_assure.id::varchar = contrats_assures_en_insertion.id_employeur_assure
        
    """

    results = pd.read_sql(query, engine)
    logging.info(f"Read {len(results)} lines")

    return results


def get_salaires(engine, id_employeur_assure_list):

    results = pd.DataFrame()

    for step in range(int(len(id_employeur_assure_list)/500)):
        queried_id_tuple = tuple(id_employeur_assure_list[step*500:(step+1)*500])

        query = f"""
            select
                ea.id_assure as assure_id,
                ea.id as id_employeur_assure,
                avg(rem_brute_mensuelle.montant_total_mensuel) as salaire_moyen_employeur_assure
            from 
                dsn.dadeh.ddadtassure assure
                left join dadeh.ddadtemployeur_assure ea on ea.id_assure = assure.id
                left join dadeh.ddadtversement versement on versement.id_employeur_assure = ea.id 
                inner join 
                    (select 
                        sum(rem_brute.montant) as montant_total_mensuel,
                        date_trunc('month',rem_brute.date_debut_paie) as date_paie,
                        versement.id_employeur_assure
                    from 
                        dadeh.ddadtrem_brute_ss as rem_brute
                        inner join dadeh.ddadtversement versement on versement.id = rem_brute.id_versement
                    group by 
                        date_trunc('month',rem_brute.date_debut_paie),
                        versement.id_employeur_assure
                    order by 
                        date_paie ) rem_brute_mensuelle on rem_brute_mensuelle.id_employeur_assure = versement.id_employeur_assure and rem_brute_mensuelle.date_paie = versement.mois_declaration
            where versement.id_employeur_assure in {queried_id_tuple}
            group by 
                assure.id,
                ea.id
            order by 
                assure_id
        """

        results = pd.concat([results, pd.read_sql(query, engine)])
        logging.info(f"Read {len(results)} lines")

    return results
