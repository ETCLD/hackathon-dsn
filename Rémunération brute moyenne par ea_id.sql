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
group by 
	assure.id,
	ea.id
order by 
	assure_id