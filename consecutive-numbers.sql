# https://leetcode.com/problems/consecutive-numbers/

SELECT DISTINCT offset0 AS ConsecutiveNums FROM (
  SELECT l1.Num AS offset0, l2.Num AS offset1, l3.Num AS offset2
  FROM Logs l1
  INNER JOIN Logs l2
  ON l1.Id + 1 = l2.Id
  INNER JOIN Logs l3
  ON l1.Id + 2 = l3.Id
) AS T
WHERE offset0 = offset1 AND offset0 = offset2