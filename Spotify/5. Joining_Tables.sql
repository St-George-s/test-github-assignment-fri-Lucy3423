-- SELECT * 
-- FROM Tracks 
-- WHERE album_id IN (
--   SELECT album_id 
--   FROM Albums 
--   WHERE release_year > 2018
--  );

-- SELECT T.track_name, A.album_name 
-- FROM Tracks T, Albums A
-- WHERE T.album_id = A.album_id 
-- AND A.release_year < 2020;

-- SELECT T.track_name, A.album_name 
-- FROM Tracks T 
-- JOIN Albums A ON T.album_id = A.album_id 
-- WHERE A.release_year > 2015;

-- SELECT A.artist_name, COUNT(T.track_id) 
-- FROM Artists A 
-- JOIN Tracks T ON A.artist_id = T.artist_id 
-- GROUP BY A.artist_name;


-- find all track names for Lizzo by using an equi join between Tracks and Artists
-- SELECT T.track_name
-- FROM Tracks T, Artists A
-- JOIN Tracks on A.artist_id = T.artist_id
-- WHERE A.artist_name = "Coldplay"
-- GROUP BY T.track_name;

-- Select track names and their respective genres by using an equi join
-- between Tracks and Genres

-- SELECT T.track_name, G.genre_name
-- FROM Tracks T, Genres G
-- JOIN Tracks on G.genre_id = T.genre_id
-- GROUP BY T.track_name;

-- Count the number of tracks in each genre for 2017 by using an equi join
-- among Tracks, Albums and Genres

SELECT T.track_name, COUNT(G.genre_id) as 'Genre Count'
FROM Albums A, Tracks T, Genres G
JOIN Tracks on T.album_id = A.album_id
JOIN Genres on T.genre_id = G.genre_id
WHERE A.release_year < 2020
GROUP BY T.track_name;

-- join the track ids
-- join the genre ids 