# https://leetcode.com/problems/exchange-seats/

SELECT id, CASE 
            WHEN id % 2 = 1 AND student_s2 IS NOT NULL THEN student_s2
            WHEN id % 2 = 0 AND student_s3 IS NOT NULL THEN student_s3
            ELSE student_s1
           END AS student
FROM (
    SELECT s1.id AS id, s1.student AS student_s1, s2.student AS student_s2, s3.student AS student_s3
    FROM seat s1 
    LEFT JOIN seat s2 
    ON s2.id = s1.id+1 
    LEFT JOIN seat s3
    ON s3.id = s1.id-1 
    ORDER BY s1.id ASC
) AS T