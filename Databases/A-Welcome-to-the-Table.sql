-- 01. projectList
SELECT project_name, team_lead, income FROM Projects;

-- 02. countriesSelection
SELECT * FROM countries WHERE continent = 'Africa';

-- 03. monthlyScholarships
SELECT id, scholarship / 12 as scholarship FROM scholarships;

-- 04. prokectsTeam
SELECT DISTINCT(name) FROM projectLog ORDER BY name;

-- 05. automaticNotifications
SELECT email
FROM users
WHERE role NOT IN ("admin", "premium")
ORDER BY email;
