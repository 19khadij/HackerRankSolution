SELECT a.element, b.element  -- Assuming your tables have a column named 'element'
FROM TableA a
CROSS JOIN TableB b;

-- Or the older, implicit comma join style:
SELECT a.element, b.element
FROM TableA a, TableB b;