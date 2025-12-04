-- Let's group and count number of thr=e grouped soceres
SELECT score, COUNT(*) AS number
GROUP BY score
ORDER BY score DESC;
