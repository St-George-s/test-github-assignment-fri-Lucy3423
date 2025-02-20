DESCRIBE ALL TABLES;

SELECT Planner.forename, Planner.surname, Planner.plannerNO, COUNT(Walk.walkerNO) as "Total Participants"
FROM Planner
JOIN Route ON Planner.plannerNO = Route.plannerNO
JOIN Walk ON Route.routeID = Walk.routeID
JOIN Walker ON Walk.walkerNo = Walker.walkerNo 
GROUP BY Planner.plannerNO
ORDER BY COUNT(Walker.walkerNo) DESC;

SELECT Walker.walkerNo