-- 17. countriesInfo
SELECT COUNT(*) as number, AVG(population) as average, SUM(population) as total FROM countries;

-- 18. itemCounts
SELECT item_name, item_type, COUNT(*) as item_count
FROM availableItems
GROUP BY item_name, item_type
ORDER BY item_type, item_name;

-- 19. usersByContinent
SELECT continent, SUM(users) users
FROM countries
GROUP BY continent
ORDER BY users DESC;

-- 20. movieDirectors
SELECT director FROM moviesInfo
WHERE year > 2000
GROUP BY director HAVING SUM(oscars) > 2
ORDER BY director;

-- 21. travelDiary
SELECT GROUP_CONCAT(country) FROM (
	SELECT DISTINCT country
	FROM diary
	GROUP BY country
	ORDER BY country
) tmp;

-- 22. soccerPlayers
SELECT
    CONCAT(
        GROUP_CONCAT(
            CONCAT(first_name, ' ', surname, ' #', player_number)
            ORDER BY player_number
            SEPARATOR '; '
        )
    ) AS players
FROM
    soccer_team;

-- 23. marketReport
SELECT
	IFNULL(country, 'Total:') AS country,
	COUNT(competitor) AS competitors
FROM foreignCompetitors
GROUP BY country WITH ROLLUP;
