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


