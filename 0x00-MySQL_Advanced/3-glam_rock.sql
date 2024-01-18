-- List all bands with Glam rock as their origin.
-- Rank by longevity.


SELECT band_name, COALESCE(split, 2022) - formed AS lifespan FROM metal_bands
WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
