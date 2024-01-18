-- Script that ranks the origins of bands
-- and the number of non unique fans they have


SELECT origin, COUNT(DISTINCT(fans)) AS nb_fans FROM metal_bands
GROUP BY origin ORDER BY nb_fans DESC;
