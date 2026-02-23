-- CREATE DATABASE SwimClubDB;
-- USE SwimClubDB;

-- CREATE TABLE Centre (
--     centreID INT NOT NULL PRIMARY KEY,
--     centreName VARCHAR(40) NOT NULL,
--     centreType VARCHAR(20) NOT NULL
-- )

-- CREATE TABLE Class (
--     classCode VARCHAR(4) NOT NULL PRIMARY KEY,
--     className VARCHAR(40) NOT NULL,
--     centreID INT NOT NULL,
--     level INT NOT NULL,
--     termStartDate DATE,
--     sessionType VARCHAR(12) NOT NULL,
--     startTime TIME NOT NULL,
--     pricePerPerson DECIMAL(6,2) NOT NULL,
--     FOREIGN KEY (centreID) REFERENCES Centre(centreID) 
-- )


-- CREATE TABLE Member (
--     memberNo INT NOT NULL PRIMARY KEY,
--     firstName VARCHAR(20) NOT NULL,
--     lastName VARCHAR(20) NOT NULL,
--     address VARCHAR(60) NOT NULL,
--     town VARCHAR(20) NOT NULL,
--     postcode VARCHAR(10) NOT NULL    
-- )

-- CREATE TABLE Booking ( 
--   classCode VARCHAR(4) NOT NULL, 
--   memberNo INT NOT NULL, 
--   startDate DATE NOT NULL, 
--   numberOfSessions INT NOT NULL, 
--   numberInParty INT NOT NULL, 
--   PRIMARY KEY (memberNo, classCode, startDate), 
--   FOREIGN KEY (memberNo) REFERENCES Member(memberNo), 
--   FOREIGN KEY (classCode) REFERENCES Class(classCode) 
-- ); 

-- INSERT INTO Centre VALUES(101, "Edinburgh Meadowbank", "leisure"); 
-- INSERT INTO Centre VALUES(115, "Glasgow Kelvinhall", "university"); 
-- INSERT INTO Centre VALUES(132, "St Andrews Community Hub", "community"); 
-- INSERT INTO Centre VALUES(148, "Fort William Leisure", "leisure"); 
-- INSERT INTO Centre VALUES(169, "Portree Sports Hall", "community"); 


-- INSERT INTO Class (classCode, className, centreID, level, sessionType, startTime, pricePerPerson) 
-- VALUES ("ED01", "Beginner Breaststroke", 101, 1, "Term", "16:00:00", 8.50); 
-- INSERT INTO Class VALUES ("ED04", "Improver Front Crawl", 101, 2, "2025-09-01", "Term", "17:00:00", 10.00); 
-- INSERT INTO Class (classCode, className, centreID, level, sessionType, startTime, pricePerPerson) 
-- VALUES ("GL02", "Lane Training", 115, 5, "Drop-in", "18:30:00", 6.75); 
-- INSERT INTO Class (classCode, className, centreID, level, sessionType, startTime, pricePerPerson) 
-- VALUES ("SA03", "Water Confidence", 132, 1, "Intensive", "10:30:00", 12.00); 
-- INSERT INTO Class VALUES ("FW01", "Stroke Development", 148, 3, "2025-09-08", "Term", "15:30:00", 9.25); 
-- INSERT INTO Class VALUES ("FW02", "Junior Club Prep", 148, 4, "2025-09-15", "Term", "16:15:00", 9.95); 
-- INSERT INTO Class (classCode, className, centreID, level, sessionType, startTime, pricePerPerson) 
-- VALUES ("PR05", "Family Splash", 169, 1, "Drop-in", "11:00:00", 5.50); 
-- INSERT INTO Class (classCode, className, centreID, level, sessionType, startTime, pricePerPerson) 
-- VALUES ("GL07", "Masters Fitness", 115, 5, "Term", "19:30:00", 11.75); 

-- INSERT INTO Member VALUES (201, "Leila", "Gordon", "7 Elmtree Way", "Paisley", "PA1 9GP"); 
-- INSERT INTO Member VALUES (218, "Phoebe", "Kaur", "64 Main Road", "Hamilton", "ML11 1SW"); 
-- INSERT INTO Member VALUES (233, "Rebecca", "Jones", "121 Main Street", "Greenock", "PA16 1JK"); 
-- INSERT INTO Member VALUES (247, "Omar", "Sharif", "31 Pike Place", "Perth", "PH1 3KT"); 
-- INSERT INTO Member VALUES (252, "Naomi", "Lowden", "5 Admiral Way", "Gourock", "PA19 1UX"); 
-- INSERT INTO Member VALUES (269, "Alba", "McKay", "34a Newton Road", "Dalkeith", "EH22 1FD"); 

-- INSERT INTO Booking VALUES ("FW02", 233, "2025-09-22", 4, 1); 
-- INSERT INTO Booking VALUES ("ED04", 247, "2025-09-29", 6, 2); 
-- INSERT INTO Booking VALUES ("ED01", 247, "2025-10-06", 4, 1); 
-- INSERT INTO Booking VALUES ("PR05", 218, "2025-10-04", 1, 4); 
-- INSERT INTO Booking VALUES ("PR05", 233, "2025-10-11", 1, 2); 
-- INSERT INTO Booking VALUES ("ED04", 201, "2025-10-06", 5, 2); 
-- INSERT INTO Booking VALUES ("GL02", 218, "2025-10-02", 1, 1); 
-- INSERT INTO Booking VALUES ("GL07", 218, "2025-10-16", 6, 1); 
-- INSERT INTO Booking VALUES ("ED01", 233, "2025-10-13", 4, 3); 

 
-- 1 list all classes
-- SELECT * 
-- FROM Class


-- 2 each member total spent perperson where total is >= 120, order DESC
-- SELECT m.lastName, SUM(numberInParty * pricePerPerson * numberOfSessions) AS totalSpend
-- FROM Member m
-- JOIN Booking b ON b.memberNo=m.memberNo
-- JOIN Class c ON c.classCode=b.classCode
-- GROUP BY m.lastName
-- HAVING SUM(numberInParty * pricePerPerson * numberOfSessions) >= 120
-- ORDER BY totalSpend DESC;

-- 3 For each Centre, show average pricePerPerson (rounded to 2 d.p.). Show only averages > £9.00. 
-- SELECT centerName, ROUND(AVG(pricePerPerson), 2) as AvgPricePerPerson
-- FROM Centre centre
-- JOIN Class class ON centre.centreID=class.centreID
-- GROUP BY centre.centreID
-- HAVING AvgPricePerPerson > 9.00;

-- 4 List classes at centres that are not type university. 
-- SELECT className, centerName
-- FROM Class 
-- JOIN Centre ON Class.centreID=Centre.centreID
-- WHERE centreType <> "university"; 
--          Doesn't work

-- 5 Show Members who have between 2 and 4 bookings (inclusive). 
-- SELECT m.memberNo, COUNT(b.memberNo) as NumBookings
-- FROM Booking b 
-- JOIN Member m ON b.memberNo=m.memberNo
-- GROUP BY m.memberNo
-- HAVING NumBookings >= 2 AND NumBookings <= 4;

-- 6 List surname, postcode and town for Members whose town sorts alphabetically between “E” and “M”, ordered by town.
-- SELECT lastName, postcode, town
-- FROM Member 
-- -- ANSWER
-- WHERE town BETWEEN "E" AND "M"
-- ORDER BY town;

-- 7 List className and sessionType where sessionType is in ("Drop-in", "Term", "Intensive"). 
SELECT className, sessionType
FROM Class
HAVING sessionType IN ("Drop-in", "Term", "Intensive")
ORDER BY sessionType ASC;