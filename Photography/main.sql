<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 09b5c8d (Mock DB Test)
SELECT name
FROM Clients
WHERE client_id IN (
    SELECT client_id
    FROM Bookings
    WHERE event_type = 'Wedding'
);
<<<<<<< HEAD
=======
DESCRIBE ALL TABLES;

-- Find the latest photo taken by any photographer.
SELECT title, date_taken
FROM Photos
WHERE date_taken IN (
    SELECT MAX(date_taken)
    FROM Photos
);

 

-- List the photographers who have never had a booking.
-- SELECT name
-- FROM Photographers
-- WHERE photographer_id IN (
--     SELECT date_booked
--     FROM Bookings
--     WHERE date_booked = NULL
-- );   


SELECT name
FROM Photographers
WHERE photographer_id IN (
    SELECT photographer_id
    FROM Bookings
    WHERE date_booked LIKE NULL
);



-- -- Identify clients who have booked a 'Wedding' event
-- SELECT name
-- FROM Clients 
-- WHERE client_id IN (
--     SELECT client_id
--     FROM Bookings
--     WHERE event_type LIKE "Wedding"
-- );

-- -- Count the number of photos taken by photographers with more than 5 years of experience.

-- SELECT COUNT(photographer_id)
-- FROM Photos
-- WHERE photographer_id IN (
--     SELECT photographer_id
--     FROM Photographers
--     WHERE experience_years > 5
-- );
>>>>>>> 92972dc (mostly finished 2020, working on 23)
=======
DESCRIBE ALL TABLES;
>>>>>>> 77a9bcf (Mock DB Test)
=======
>>>>>>> 09b5c8d (Mock DB Test)
