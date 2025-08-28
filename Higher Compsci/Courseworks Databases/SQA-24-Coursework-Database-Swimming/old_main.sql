DESCRIBE ALL TABLES;

-- 2c
SELECT Swimmer.initial, Swimmer.surname, Swimmer.swimCategory, Team.teamName, COUNT(Result.position) as 'Races Won'
FROM Swimmer
JOIN Team ON Swimmer.teamRef = Team.teamRef
JOIN Result ON Swimmer.swimmerID = Result.swimmerID
WHERE Result.position = 1
GROUP BY Swimmer.initial
ORDER BY Swimmer.initial ASC;

-- 2d
SELECT Swimmer.initial, Swimmer.surname, Team.teamName, Event.city, Event.eventDate
FROM Event
JOIN Race ON Event.EventID = Race.EventID
JOIN Result ON Race.raceNumber = Result.raceNumber
JOIN Swimmer ON Result.swimmerID = Swimmer.swimmerID
JOIN Team ON Swimmer.teamRef = Team.teamRef
WHERE (Result.lane = 1 OR Result.lane = 8) AND Result.raceTime = (
    SELECT MIN(raceTime)
    FROM Result);




-- 2e
-- SELECT Team.teamName, COUNT(Result.position) as 'Total medals won'
-- FROM Team
-- JOIN Swimmer ON Team.teamRef = Swimmer.teamRef
-- JOIN Result ON Swimmer.swimmerID = Result.swimmerID
-- WHERE Result.position = 1 OR Result.position = 2 OR Result.position = 3
-- GROUP BY Team.teamName
-- ORDER BY COUNT(Result.position) DESC;

-- SELECT teamName, COUNT(position) AS [Total medals won] 
-- FROM Result, Swimmer, Team 
-- WHERE Result.swimmerID = Swimmer.swimmerID AND Swimmer.teamRef = 
-- Team.teamRef AND (Result.position = 1 OR Result.position = 2 OR Result.position = 3)
-- GROUP BY teamName; 
