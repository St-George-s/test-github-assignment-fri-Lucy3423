-- CREATE DATABASE SwimClbuDB;
USE SwimClbuDB;

-- CREATE TABLE Centre (
--     centreID INT NOT NULL PRIMARY KEY,
--     centerName VARCHAR(40) NOT NULL,
--     centerType VARCHAR(20) NOT NULL
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


CREATE TABLE Member (
    memberNo INT NOT NULL PRIMARY KEY,
    firstName VARCHAR(20) NOT NULL,
    lastName VARCHAR(20) NOT NULL,
    address VARCHAR(20) NOT NULL,
    town VARCHAR(20) NOT NULL,
    postcode VARCHAR(10) NOT NULL
)

CREATE TABLE Booking (
    classCode VARCHAR(10) NOT NULL,
    memberNo INT NOT NULL,
    startDate DATE NOT NULL,
    numberOfSessions INT NOT NULL,
    numberInParty INT NOT NULL,
    FOREIGN KEY (classCode) REFERENCES Class(classCode),
    FOREIGN KEY (memberNo) REFERENCES Member(memberNo)
)