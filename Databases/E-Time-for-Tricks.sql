-- 24. websiteHacking
SELECT id,login,name
FROM users
WHERE type='user'
OR type!='user'
ORDER BY id;

-- 25. nullIntern
SELECT COUNT(*) FROM departments
WHERE description IS NULL OR LOWER(TRIM(description)) = 'null' OR LOWER(TRIM(description)) = 'nil' OR LOWER(TRIM(description)) = '-';

-- 26. legsCount
SELECT SUM(IF(type = 'human', 2, 4)) as summary_legs
FROM creatures
ORDER BY id;

-- 27. combinationLock
SET @comb = 1;
SELECT max(@comb:=@comb*length(characters)) as combinations
FROM discs;
