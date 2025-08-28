--Write a query to select track names that 
--start with 'S' and end with 'e'.

select track_name
from Tracks
where track_name like "S%e";


--Select albums released after 2010, displaying the album 
--name and a calculation of how many years ago they were released.
select album_name,
2024 - release_year as years_since_release
From Albums;
 

SELECT artist_name, 
length(artist_name) as length_of_name
FROM Artists 
WHERE length_of_name <= 5;