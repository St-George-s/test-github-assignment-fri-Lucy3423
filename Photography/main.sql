SELECT name
FROM Clients
WHERE client_id IN (
    SELECT client_id
    FROM Bookings
    WHERE event_type = 'Wedding'
);
