SELECT COUNT(*) AS difference_count
FROM A
WHERE element NOT IN (SELECT element FROM B);