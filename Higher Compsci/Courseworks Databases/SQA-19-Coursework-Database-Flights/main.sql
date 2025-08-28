DESCRIBE ALL TABLES;

SELECT forename, surname, SUM((Booking.adultTicket * 5.50) + (Booking.childTicket * 2.00) + (Booking.concessionTicket * 1.50)) AS "Tax(£)"
FROM Customer
JOIN Booking On Customer.customerID = Booking.customerID
JOIN Flight on Booking.flightID = Flight.flightID
WHERE Customer.customerID = "GR01932" and Flight.flightID = "QH182"
GROUP BY Customer.customerID;

SELECT forename, surname
FROM Customer
JOIN Booking ON Customer.customerID = Booking.customerID
WHERE childTicket = (
    SELECT MAX(childTicket)
    FROM Booking
);
