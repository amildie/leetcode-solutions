# https://leetcode.com/problems/classes-more-than-5-student/

SELECT class 
FROM (
    SELECT DISTINCT student, class
    FROM courses
) AS t 
GROUP BY class
HAVING COUNT(*) > 4;