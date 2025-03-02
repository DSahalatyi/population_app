from sqlalchemy import text

WIKIPEDIA_DATA_QUERY = text(
"""
WITH ranked_population AS (
    SELECT 
        continental_region, 
        country, 
        population_2023,
        MAX(population_2023) OVER (PARTITION BY continental_region) AS largest_population,
        MIN(population_2023) OVER (PARTITION BY continental_region) AS smallest_population
    FROM population_wiki
    WHERE continental_region IS NOT NULL AND continental_region <> ''
)
SELECT 
    p.continental_region,
    SUM(p.population_2023) AS total_population,
    MAX(CASE WHEN p.population_2023 = p.largest_population THEN p.country END) AS largest_population_country,
    MAX(p.population_2023) AS largest_population,
    MAX(CASE WHEN p.population_2023 = p.smallest_population THEN p.country END) AS smallest_population_country,
    MIN(p.population_2023) AS smallest_population
FROM ranked_population p
GROUP BY p.continental_region;
"""
)

STATISTICS_TIMES_DATA_QUERY = text(
"""
WITH ranked_population AS (
    SELECT
        region,
        country,
        population_2024,
        MAX(population_2024) OVER (PARTITION BY region) AS largest_population,
        MIN(population_2024) OVER (PARTITION BY region) AS smallest_population
    FROM population_stats_times
    WHERE region IS NOT NULL AND region <> ''
)
SELECT
    p.region,
    SUM(p.population_2024) AS total_population,
    MAX(CASE WHEN p.population_2024 = p.largest_population THEN p.country END) AS largest_population_country,
    MAX(p.population_2024) AS largest_population,
    MAX(CASE WHEN p.population_2024 = p.smallest_population THEN p.country END) AS smallest_population_country,
    MIN(p.population_2024) AS smallest_population
FROM ranked_population p
GROUP BY p.region;
"""
)