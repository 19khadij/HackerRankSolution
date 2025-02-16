SELECT COUNT(DISTINCT element) AS union_count
FROM (
    SELECT element FROM A
    UNION
    SELECT element FROM B
) AS union_set;