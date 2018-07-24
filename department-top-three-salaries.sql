# https://leetcode.com/problems/department-top-three-salaries/

SELECT d.Name AS Department, e1.Name AS Employee, e1.Salary AS Salary
FROM Employee e1
INNER JOIN Department d
ON e1.DepartmentId = d.Id
WHERE (
    SELECT COUNT(DISTINCT e2.Salary)
    FROM Employee e2
    WHERE e2.DepartmentId = e1.DepartmentId AND e2.Salary > e1.Salary
) < 3
ORDER BY e1.Salary DESC