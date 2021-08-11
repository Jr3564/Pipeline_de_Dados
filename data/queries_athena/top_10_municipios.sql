SELECT mun.NO_MUNICIPIO AS municipio, COUNT(cen.CO_MUNICIPIO) AS quantidade
FROM microdadoscensoescolar AS cen
JOIN tabela_auxiliar_municipios_ufs AS mun ON cen.CO_MUNICIPIO = mun.CO_MUNICIPIO
WHERE cen.TP_ETAPA_ENSINO = 41
GROUP BY mun.NO_MUNICIPIO
ORDER BY quantidade DESC LIMIT 10;
