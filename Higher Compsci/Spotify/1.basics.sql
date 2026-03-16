SELECT *
FROM Albums;


--Write a query to display all albums 
--released before the year 2010.

SELECT *
from Albums
where release_year < 2010;

--Write a query to select artist names from the Artists table 
--where the artist_id is less than 10
select artist_name
from Artists
where artist_id < 10;