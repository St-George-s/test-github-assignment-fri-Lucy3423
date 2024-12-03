DESCRIBE ALL TABLES;
-- return the gnome name and the total quantity sold of that type as 'total gnomes sold'

SELECT G.gnomeName, COUNT(*) as 'Total gnomes sold'
FROM Gnome G, GnomePurchase GP
JOIN Gnome ON G.gnomeID = GP.gnomeID
WHERE G.description LIKE '%solar%'
GROUP BY G.gnomeName;


SELECT gnomeName, MAX(unitPrice)