SELECT N,CASE
            WHEN P IS NULL THEN 'Root'
            WHEN (SELECT COUNT(*) FROM BST child where child.P = FATHER.N )> 0 THEN 'Inner'
            ELSE 'Leaf'
        END
FROM BST father
ORDER BY N;
