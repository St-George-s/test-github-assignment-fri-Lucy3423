DESCRIBE ALL TABLES;

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



 SELECT forename, surname, AVG(cost) AS [Average Job Cost] 
 FROM   Customer, Car, Job 
 WHERE  Customer.customerID = Car.customerID AND 
             Car.regNo = Job.regNo 
 GROUP BY surname, Customer.customerID
 ORDER BY AVG(cost) DESC; 