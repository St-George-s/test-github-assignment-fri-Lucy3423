DESCRIBE ALL TABLES;

-- 2c
SELECT comicTitle, issue, publisherName, AVG(valuation) AS 'valuation'
FROM Comic
JOIN Publisher ON Comic.publisherID = Publisher.publisherID
WHERE valuation > (
    SELECT AVG(valuation)
    FROM Comic
) + 300
GROUP BY comicID;


-- 2d
SELECT characterName, SUM(valuation) as "Total Valuation"
FROM Comic
JOIN ComicCharacter ON Comic.comicID = ComicCharacter.comicID
JOIN CharacterInfo ON ComicCharacter.characterID = CharacterInfo.characterID
WHERE characterName LIKE "%Duck%" AND mainCharacter = 1
GROUP BY characterName
ORDER BY SUM(valuation) DESC;


-- 2e
SELECT comicTitle, issue, publisherName, SUM(valuation * 2) AS [Double Price]
FROM Comic, Publisher, Series, CharacterInfo, ComicCharacter
WHERE Series.seriesName = "The OK Seven"
AND characterName = "Starlordly"
AND Comic.publisherID = Publisher.publisherID
AND Comic.seriesID = Series.seriesID
AND Comic.comicID = ComicCharacter.comicID
AND CharacterInfo.characterID = ComicCharacter.characterID
GROUP BY Series.seriesID;










