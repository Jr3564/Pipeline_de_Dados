SELECT mun.no_uf AS UF, cor.cor_raca_name AS cor_raca, COUNT(*) AS quantidade_de_pessoas
FROM microdadoscensoescolar AS cen
JOIN tabela_auxiliar_municipios_ufs AS mun
	ON cen.co_uf = mun.co_uf
JOIN tabela_auxiliar_cor_raca AS cor
	ON cor.tp_cor_raca = cen.tp_cor_raca
GROUP BY cor.cor_raca_name, mun.no_uf
ORDER BY mun.no_uf, quantidade_de_pessoas, cor.cor_raca_name DESC;