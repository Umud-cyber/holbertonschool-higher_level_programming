-- Let's group and count number of thr=e grouped soceres
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
