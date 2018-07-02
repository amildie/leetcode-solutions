# https://leetcode.com/problems/department-highest-salary/description/

SELECT Department.Name AS Department, T.Name AS Employee, T.Salary AS Salary FROM
(
    SELECT DepartmentId, Name, Salary
    FROM Employee E1
    WHERE Salary = (
        SELECT MAX(Salary) FROM Employee E2 WHERE E2.DepartmentId = E1.DepartmentId
    ) 
) AS T
INNER JOIN Department
ON Department.Id = T.DepartmentId