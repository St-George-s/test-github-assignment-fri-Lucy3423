DESCRIBE ALL TABLES;

SELECT AVG(valuation), comicTitle
FROM Comic
WHERE valuation => (
    SELECT AVG(valuation)
    FROM Comic
) + 300
GROUP BY comicID;
