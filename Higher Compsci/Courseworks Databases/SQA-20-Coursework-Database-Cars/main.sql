DESCRIBE ALL TABLES;

-- a query to calcuate the total earnings across all five garages on 19 January 2020



SELECT garageName, SUM(cost) AS "Total Sales"
FROM Garage
JOIN Job on Garage.garageID = Job.garageID
WHERE Job.dateOut = "19-Jan-20"
GROUP BY garageName;


-- a query to display details of car with most days in garage

SELECT MAX(dateOut - dateIN) AS "Number of Days", Car.regNo, garageName
FROM Car
JOIN Job ON Car.regNo = Job.regNo
JOIN Garage ON Job.garageID = Garage.garageID
GROUP BY garageName;

-- SELECT SUM(dateOut - dateIN) AS "Number of Days", Car.regNo, garageName
-- FROM Car
-- JOIN Job ON Car.regNo = Job.regNo
-- JOIN Garage ON Job.garageID = Garage.garageID
-- GROUP BY garageName
-- ORDER BY SUM(dateOut - dateIN) DESC
-- LIMIT BY 1;

-- need to use subquery to obtain the max number of days.

-- testing the following query

SELECT forename, surname, AVG(cost) AS [Average Job Cost]
FROM Customer, Car, Job
WHERE Customer.customerID = Car.customerID AND
 Car.regNo = Job.regNo
GROUP BY Customer.customerID
ORDER BY AVG(cost) DESC;







































-- select the garage name and the total sales
-- the data to look for is 19-Jan-20
-- using the Garage and Job databases
-- look at the cost of the job and if the dateOut is equal to the date we are looking at then add that to the total 


-- SELECT G.garageName, SUM(J.cost) as 'Total Sales (£)'
-- FROM Garage G
-- JOIN Job J on G.garageID = J.garageID
-- WHERE J.dateOut = '19-Jan-20'
-- GROUP BY G.garageName;


-- car that spent max time there 
-- Number of days regNo garageName

-- num days = date out - in JOB
-- car regNO - pk from CAR  
-- garage id 


-- SELECT SUM(J.dateOut - J.dateIN) as 'Number of Days', J.regNO, G.garageName
-- FROM Job J
-- JOIN Car C on C.regNO = J.regNO
-- JOIN Garage G on G.garageID = J.garageID
-- GROUP BY G.garageName, J.regNO
-- ORDER BY SUM(J.dateOut - J.dateIN) desc;

-- SELECT dateIN, dateOut, dateOut - dateIN, datediff(dateIn, dateOUT) FROM Job;



--  SELECT forename, surname, AVG(cost) AS [Average Job Cost] 
--  FROM   Customer, Car, Job 
--  WHERE  Customer.customerID = Car.customerID AND 
--              Car.regNo = Job.regNo 
--  GROUP BY surname, Customer.customerID
--  ORDER BY AVG(cost) DESC; 