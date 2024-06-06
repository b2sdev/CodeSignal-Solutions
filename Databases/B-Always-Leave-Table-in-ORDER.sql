-- 6. volleyBallResults
SELECT * FROM results ORDER BY wins;

-- 7. mostExpensive 
SELECT name FROM Products ORDER BY price * quantity DESC, name LIMIT 1;

-- 8. contestLeaderBoard
SELECT name FROM leaderboard ORDER BY score DESC LIMIT 5 OFFSET 3;

-- 9. gradeDistribution
SELECT Name, ID FROM (
    SELECT
        Name,
        ID,
        0.25 * Midterm1 + 0.25 * Midterm2 + 0.5 * Final as Option1,
        0.5 * Midterm1 + 0.5 * Midterm2 as Option2,
        Final as Option3
    FROM Grades
) AS tmp
WHERE Option3 > Option1 AND Option3 > Option2
ORDER BY SUBSTRING(Name, 1, 3), ID;

-- 10. mischievousNephews
SELECT WEEKDAY(mischief_date) weekday, mischief_date, author, title FROM mischief
ORDER BY weekday, FIELD(author, "Huey", "Dewey", "Louie"), mischief_date, title;







