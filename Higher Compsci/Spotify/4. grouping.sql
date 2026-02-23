SELECT genre_id, COUNT(*) AS occurence_count
FROM Tracks 
GROUP BY genre_id;

-- How does grouping by genre_id in the 
-- Tracks table affect the count?
SELECT album_id, COUNT(album_id) as album_id_occurence
FROM Albums
GROUP BY album_id;

-- Discuss the use of AVG(duration_ms) in conjunction 
-- with GROUP BY genre_id

SELECT track_name, AVG(duration_ms)
FROM Tracks;
GROUP BY track_name;

-- Calculate the total duration of tracks in each album
SELECT Track_name, SUM(duration_ms) as Duration_ms
FROM Tracks
GROUP BY track_name;



-- Find the album with the longest average trakc duration
SELECT genre_id, MAX(duration_ms)
FROM Tracks
GROUP BY genre_id;