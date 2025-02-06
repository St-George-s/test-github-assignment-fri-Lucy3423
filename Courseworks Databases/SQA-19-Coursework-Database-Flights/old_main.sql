-- DESCRIBE ALL TABLES;
-- SELECT childTicket
-- FROM Booking;

-- John Smith, Customer ID - GR01932, has asked for a copy of the tax he has paid on
-- flight QH182. The tax for a booking is calculated as follows:
--  adults pay £5.50
--  children pay £2.00
--  concessions pay £1.50

SELECT c.forename, c.surname, 
    SUM(b.adultTicket * 5.5 + b.childTicket * 2.0 + b.concessionTicket * 1.5) AS 'Tax (£)'
FROM customer c
JOIN booking b ON c.customerID=b.customerID
WHERE c.customerID = 'GR01932';

-- display the forename and surname
-- calculate the sum of the children booked
-- limit by one after printing them out in descending order

-- customer - forename and surname and customerID
-- link to the customerID in booking

-- option 1
SELECT c.forename, c.surname
FROM customer c
JOIN booking b ON c.customerID = b.customerID
GROUP BY c.forename, c.surname
ORDER BY b.childTicket DESC;









-- 1
SELECT C.forename, C.surname, SUM(B.childTicket * 2.00 + B.adultTicket * 5.50 + B.concessionTicket * 1.50) AS 'Tax (£)'
FROM Customer C
JOIN Booking B ON C.customerID = B.customerID
JOIN Flight F ON B.flightID = F.flightID
WHERE C.customerID = 'GR01932' AND F.flightID = 'QH182';

-- 2
SELECT C.forename, C.surname
FROM Customer C
JOIN Booking B ON C.customerID = B.customerID
WHERE childTicket
 = (
    SELECT MAX(childTicket)
    FROM Booking 
 );

-- 3
