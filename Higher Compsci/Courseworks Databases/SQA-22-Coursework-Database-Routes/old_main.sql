-- counts the number of walkers for a each route

-- SELECT R.routeID, COUNT(W.walkerNO)
-- FROM Walk W
-- JOIN Route R ON W.routeID = R.routeID
-- GROUP BY R.routeID;

-- SELECT Walker.forename, Walker.surname, Planner.plannerNo
-- FROM Planner, Walker, Route
-- JOIN Walker ON Walk.walkerNO = Walker.walkerNO
-- JOIN Route ON Walk.routeID = Route.routeID
-- JOIN Route ON Planner.plannerNo = Route.plannerNo;


-- SELECT Planner.forename, Planner.surname, Planner.plannerNo, COUNT(Walker.walkerNO) AS 'Total participants'
-- FROM Planner 
-- JOIN Route ON Planner.plannerNo = Route.plannerNo
-- JOIN Walk ON Route.routeID = Walk.routeID
-- JOIN Walker on Walk.walkerNO = Walker.walkerNO
-- GROUP BY Planner.forename, Planner.surname, Planner.plannerNo
-- ORDER BY COUNT(Walker.walkerNO) DESC;

-- find the longest route

SELECT MAX(distance)
FROM Route;

SELECT Walker.walkerNO, Walker.forename, Walker.surname, Walker.telNO
FROM Walker
JOIN Walk ON Walker.walkerNO = Walk.walkerNO
JOIN Route on Walk.routeID = Route.routeID
WHERE Route.distance = (
    SELECT MAX(distance)
    FROM Route
)
GROUP BY Walker.walkerNO, Walker.forename, Walker.surname, Walker.telNO
ORDER BY Walker.walkerNO ASC;