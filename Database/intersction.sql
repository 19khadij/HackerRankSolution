SELECT COUNT(*) AS intersection_count
FROM A
WHERE element IN (SELECT element FROM B);
