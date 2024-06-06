-- 11. suspectsInvestigation
SELECT id, name, surname FROM Suspect WHERE height <= 170 AND name LIKE 'B%' AND surname LIKE 'Gre_n' ORDER BY id;

-- 12. suspectsInvestigation2
SELECT id, name, surname FROM Suspect
WHERE NOT (height > 170 AND name LIKE 'B%' AND surname LIKE 'Gre_n')
ORDER BY id;

-- 13. securityBreach
SELECT * FROM users
WHERE BINARY attribute LIKE CONCAT('_%\%%', first_name, '_', second_name ,'\%%%')
ORDER BY attribute;

-- 14. testCheck
    SELECT id, IF (
        IFNULL(given_answer, "") = "", "no answer",
        IF (correct_answer = given_answer, "correct", "incorrect")
    ) AS checks
    FROM answers
    ORDER BY id;

-- 15. expressionsVerification
SELECT id, a, b, operation, c FROM (
	SELECt *,
	CASE
		WHEN operation = '+' THEN a + b
		WHEN operation = '-' THEN a - b
		WHEN operation = '*' THEN a * b
		WHEN operation = '/' THEN a / b
	END AS v
	FROM expressions
) AS tmp
WHERE c = v;

-- 16. newsSubscribers
SELECT DISTINCT subscriber
FROM (
	SELECT * FROM full_year WHERE newspaper LIKE '%Daily%'
	UNION ALL
	SELECT * FROM half_year WHERE newspaper LIKE '%Daily%'
) AS combined
ORDER BY SUBSTRING_INDEX(subscriber, ' ', 1);






