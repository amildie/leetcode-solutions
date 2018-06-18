# https://leetcode.com/problems/employees-earning-more-than-their-managers/

SELECT A.Name AS Employee
FROM Employee A, Employee B
WHERE A.ManagerId = B.Id AND A.Salary > B.Salary