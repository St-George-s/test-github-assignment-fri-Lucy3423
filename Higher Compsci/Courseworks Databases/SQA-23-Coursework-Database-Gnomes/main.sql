DESCRIBE ALL TABLES;
-- return the gnome name and the total quantity sold of that type as 'total gnomes sold'

SELECT gnomeName, COUNT(*)
FROM Gnome;