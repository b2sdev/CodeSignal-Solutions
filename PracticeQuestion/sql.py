WITH 
requests_rank AS (
    SELECT *, Rank() OVER (PARTITION BY seat_no ORDER BY request_id) AS rank1 FROM requests	
),
requests_rank1 AS (
    SELECT * FROM requests_rank WHERE rank1 = 1
)
SELECT
    s.seat_no,
    CASE
        WHEN s.status = 0 AND r.request = 1 THEN r.request
        WHEN s.status = 1 AND r.request = 2 AND s.person_id = r.person_id THEN r.request
        WHEN s.status = 0 and r.request = 2 THEN r.request
        ELSE COALESCE(s.status, 0)
    END AS status,
    CASE
        WHEN s.status = 0 AND r.request = 1 THEN r.person_id
        WHEN s.status = 1 AND r.request = 2 AND s.person_id = r.person_id THEN r.person_id
        WHEN s.status = 0 AND r.request = 2 THEN r.person_id
        ELSE COALESCE(s.person_id, 0)
    END AS person_id
FROM seats s
LEFT JOIN requests_rank1 r ON s.seat_no = r.seat_no
ORDER BY s.seat_no
;
