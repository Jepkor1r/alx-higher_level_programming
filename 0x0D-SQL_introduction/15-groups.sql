-- Lists the number of records with the same score in the table
SELECT COUNT(DISTINCT score) AS number
FROM second_table
ORDER BY score DESC, number DESC;
