DESCRIBE ALL TABLES;

-- 1
SELECT Episode.episodeTitle , Show.showName, Episode.maxViewers, Episode.episodeDate
FROM Episode
JOIN Timeslot ON Episode.showID = Timeslot.showID
JOIN Show ON Timeslot.showID = Show.showID
GROUP BY Episode.episodeTitle;
-- 2
SELECT Show.showName AS 'Show', Episode.episodeTitle AS 'Episode'
FROM Show
JOIN Episode ON Show.showID = Episode.showID
WHERE Episode.episodeDate LIKE '2024-12-%';


-- 3
UPDATE Timeslot
SET endTime = '19:30'
FROM Show
WHERE Show.showID = TimeSlot.showID AND (Show.showName = 'Star Cooks' AND Timeslot.airDate = '2024-12-24');

-- 4
SELECT Show.showName, COUNT(ViewerRating.ratingValue) AS 'TotalRatings'
FROM Show
JOIN TimeSlot ON Show.showID = TimeSlot.showID
JOIN Episode ON TimeSlot.showID = Episode.showID
JOIN ViewerRating ON Episode.episodeID = ViewerRating.episodeID
GROUP By Show.showName
ORDER BY COUNT(ViewerRating.ratingValue) DESC;