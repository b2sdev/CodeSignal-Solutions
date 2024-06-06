-- 28. interestClub
SELECT name
FROM people_interests
WHERE interests & 1<<0 AND interests & 1<<3
ORDER BY name;

-- 29. personalHobbies
SELECT name
FROM people_hobbies
WHERE hobbies LIKE '%reading%sports%';
--WHERE FIND_IN_SET('reading', hobbies)>0 AND FIND_IN_SET('sports', hobbies)>0;

-- 30. booksCatalogs
SELECT ExtractValue(xml_doc, '/catalog/book[1]/author') as author
FROM catalogs
ORDER BY author;

-- 31. habitatArea
SELECT ST_Area(ST_ConvexHull(ST_MPointFromText(CONCAT('MULTIPOINT(', GROUP_CONCAT(CONCAT_WS(' ', x, y)), ')')))) AS area
FROM places;
