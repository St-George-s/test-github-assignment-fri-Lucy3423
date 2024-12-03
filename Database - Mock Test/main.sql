<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

SELECT Event.eventName AS 'Event Name', Shop.name AS 'Shop Name', Event.maxAttendees AS 'Max Attendees', Event.eventDate AS 'Event Date' 
FROM Event
JOIN Shop on Event.shopID = Shop.shopID;

SELECT Shop.name AS 'Shop Name', Event.eventName AS 'Event Name'
FROM Shop
JOIN Event on Shop.shopID = Event.shopID
WHERE Event.eventDate = '2024-12-25';


SELECT *
FROM OpeningTime;


UPDATE OpeningTime 
SET closeTime = '19:00'
WHERE shopID = (
    SELECT Shop.name
    FROM Shop
    JOIN OpeningTime ON Shop.shopID = OpeningTime.shopID
    WHERE Shop.name = 'Zara')
AND OpeningTime.date = '2024-12-24';
=======
DESCRIBE ALL TABLES;
>>>>>>> 6c99ea2 (Mock DB Test)
=======
DESCRIBE ALL TABLES;
>>>>>>> 6c99ea2 (Mock DB Test)
=======
>>>>>>> a8ee91c (Added Class Test)
=======
DESCRIBE ALL TABLES;
>>>>>>> 4b1bb92 (Mock DB Test)
