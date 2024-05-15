select 
	case 
		when contrat.date_fin_contrat is null or contrat.date_fin_contrat <= '06/01/2023' then now() - contrat.date_debut_contrat
		when contrat.date_fin_contrat > '01/06/2023' and (date_part('day','06/01/2023' - contrat.mois_declaration) < 90) then '06/01/2023' - contrat.date_debut_contrat
		else (date_trunc('month', contrat.mois_declaration) - interval '1 day' + interval '1 month') - contrat.date_debut_contrat 
	end as anciennete_contrat,
	contrat.date_debut_contrat,
	contrat.date_fin_contrat,
	contrat.mois_declaration,
	contrat.id 
from 
	dsn.dadeh.ddadtassure assure
	left join dadeh.ddadtemployeur_assure ea on ea.id_assure = assure.id
	left join public.ddadtcontrat contrat on contrat.id_employeur_assure = ea.id
	--left join dadeh.ddadtversement versement on versement.id_employeur_assure = ea.id 
limit 10