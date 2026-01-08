DROP TABLE IF EXISTS movies;


CREATE TABLE IF NOT EXISTS movies(
  id INT PRIMARY KEY AUTO_INCREMENT,
  movieName VARCHAR(100) NOT NULL,
  genre VARCHAR(20) NOT NULL
);

INSERT INTO movies(movieName, genre) VALUES ('Frozen', "comedy");
INSERT INTO movies(movieName,genre) VALUES ('Nemo', 'comedy');

SELECT * FROM movies;