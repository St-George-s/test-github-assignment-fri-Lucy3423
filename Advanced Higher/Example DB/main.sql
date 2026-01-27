DROP TABLE IF EXISTS movies;

CREATE TABLE IF NOT EXISTS movies(
  id INT PRIMARY KEY AUTO_INCREMENT,
  movieName VARCHAR(100) NOT NULL,
  director VARCHAR(25) NOT NULL,
  genre VARCHAR(20) NOT NULL
);



INSERT INTO movies(movieName, director, genre) VALUES ('Frozen', "Jennifer Lee", "comedy");
INSERT INTO movies(movieName, director, genre) VALUES ("Nemo", "Andrew Stanton", "comedy");
INSERT INTO movies(movieName, director, genre) VALUES ("Love Actually", "Richard Curtis", "romance");

SELECT * FROM movies;
