# https://leetcode.com/problems/rising-temperature/

SELECT W2.Id
FROM Weather W1
CROSS JOIN Weather W2 
WHERE W2.RecordDate = DATE_ADD(W1.RecordDate, INTERVAL 1 DAY)
AND W2.Temperature > W1.Temperature
ORDER BY W2.Id