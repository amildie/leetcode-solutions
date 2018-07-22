# https://leetcode.com/problems/rank-scores/

SELECT s3.Score AS Score, s4.rank AS Rank
FROM Scores s3
INNER JOIN (
    SELECT s1c, COUNT(s1c) AS rank FROM (
        SELECT DISTINCT s1.Score AS s1c, s2.Score
        FROM Scores s1
        INNER JOIN Scores s2
        ON s1.Score <= s2.Score
        ORDER BY s1.Score ASC
    ) AS T
    GROUP BY s1c
) AS s4
ON s3.Score = s4.s1c
ORDER BY Rank
