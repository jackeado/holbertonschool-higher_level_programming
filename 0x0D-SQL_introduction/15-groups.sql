--  lists the number of records with the same score in the table
SELECT score, COUNT(*) AS number from second_table GROUP BY score ORDER BY number DESC;
