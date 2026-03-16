-- worksheet three
-- Update the genre of a track in the Tracks table to a
-- new genre.

Update Genres
SET genre_name = "Rock"
WHERE genre_id = 1;

select *
from Genres
where genre_id = 1;