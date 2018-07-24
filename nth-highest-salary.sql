# https://leetcode.com/problems/nth-highest-salary/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
    # Write your MySQL query statement below.
    SELECT e1.Salary
    FROM Employee e1
    WHERE (
      SELECT COUNT(DISTINCT e2.Salary)
      FROM Employee e2
      WHERE e2.Salary > e1.Salary
    ) = N-1
    LIMIT 1
  );
END