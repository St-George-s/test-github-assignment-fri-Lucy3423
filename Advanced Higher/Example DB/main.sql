DROP TABLE IF EXISTS movies;

CREATE TABLE IF NOT EXISTS movies(
  id INT PRIMARY KEY AUTO_INCREMENT,
  movieName VARCHAR(100) NOT NULL,
  director VARCHAR(25) NOT NULL,
  genre VARCHAR(20) NOT NULL
);



INSERT INTO movies(movieName, director, genre) VALUES ('Frozen', "Jennifer Lee", "comedy");
INSERT INTO movies(movieName, director, genre) VALUES ("Frozen 2", "Jennifer Lee", "comedy");

INSERT INTO movies(movieName, director, genre) VALUES ("Finding Nemo", "Andrew Stanton", "comedy");
INSERT INTO movies(movieName, director, genre) VALUES ("Finding Dory", "Andrew Stanton", "comedy");

INSERT INTO movies(movieName, director, genre) VALUES ("Love Actually", "Richard Curtis", "romance");
INSERT INTO movies(movieName, director, genre) VALUES ("About Time", "Richard Curtis", "romance");


-- insert values from chatgpt
INSERT INTO movies (movieName, director, genre) VALUES
-- Action
("Die Hard", "John McTiernan", "action"),
("The Avengers", "Joss Whedon", "action"),
("Mission Impossible", "Brian De Palma", "action"),
("Casino Royale", "Martin Campbell", "action"),
("The Bourne Identity", "Doug Liman", "action"),
("Black Panther", "Ryan Coogler", "action"),
("The Batman", "Matt Reeves", "action"),
("300", "Zack Snyder", "action"),
("Skyfall", "Sam Mendes", "action"),
("Edge of Tomorrow", "Doug Liman", "action"),

-- Sci-Fi
("Ex Machina", "Alex Garland", "sci-fi"),
("Gravity", "Alfonso Cuaron", "sci-fi"),
("Elysium", "Neill Blomkamp", "sci-fi"),
("Minority Report", "Steven Spielberg", "sci-fi"),
("Ready Player One", "Steven Spielberg", "sci-fi"),
("The Fifth Element", "Luc Besson", "sci-fi"),
("Looper", "Rian Johnson", "sci-fi"),
("District 9", "Neill Blomkamp", "sci-fi"),
("Oblivion", "Joseph Kosinski", "sci-fi"),
("Tenet", "Christopher Nolan", "sci-fi"),

-- Comedy
("Dumb and Dumber", "Peter Farrelly", "comedy"),
("Anchorman", "Adam McKay", "comedy"),
("Mean Girls", "Mark Waters", "comedy"),
("The Mask", "Chuck Russell", "comedy"),
("Ghostbusters", "Ivan Reitman", "comedy"),
("Napoleon Dynamite", "Jared Hess", "comedy"),
("The Intern", "Nancy Meyers", "comedy"),
("Yes Man", "Peyton Reed", "comedy"),
("Crazy Rich Asians", "Jon Chu", "comedy"),
("School of Rock", "Richard Linklater", "comedy"),

-- Romance
("A Star Is Born", "Bradley Cooper", "romance"),
("The Fault in Our Stars", "Josh Boone", "romance"),
("Notting Hill", "Roger Michell", "romance"),
("The Proposal", "Anne Fletcher", "romance"),
("Silver Linings Playbook", "David O Russell", "romance"),
("Crazy Stupid Love", "Glenn Ficarra", "romance"),
("Me Before You", "Thea Sharrock", "romance"),
("Dear John", "Lasse Hallstrom", "romance"),
("While You Were Sleeping", "Jon Turteltaub", "romance"),
("The Vow", "Michael Sucsy", "romance"),

-- Horror
("The Ring", "Gore Verbinski", "horror"),
("Insidious", "James Wan", "horror"),
("The Babadook", "Jennifer Kent", "horror"),
("Saw", "James Wan", "horror"),
("The Nun", "Corin Hardy", "horror"),
("The Shining", "Stanley Kubrick", "horror"),
("Halloween", "John Carpenter", "horror"),
("Scream", "Wes Craven", "horror"),
("The Exorcist", "William Friedkin", "horror"),
("Paranormal Activity", "Oren Peli", "horror"),

-- Drama
("The Green Mile", "Frank Darabont", "drama"),
("Good Will Hunting", "Gus Van Sant", "drama"),
("The Social Network", "David Fincher", "drama"),
("The Pianist", "Roman Polanski", "drama"),
("12 Years a Slave", "Steve McQueen", "drama"),
("American Beauty", "Sam Mendes", "drama"),
("Parasite", "Bong Joon Ho", "drama"),
("The Departed", "Martin Scorsese", "drama"),
("The Wolf of Wall Street", "Martin Scorsese", "drama"),
("Oppenheimer", "Christopher Nolan", "drama"),

-- Animation
("Coco", "Lee Unkrich", "animation"),
("Ratatouille", "Brad Bird", "animation"),
("Inside Out", "Pete Docter", "animation"),
("Zootopia", "Byron Howard", "animation"),
("Frozen Fever", "Jennifer Lee", "animation"),
("How to Train Your Dragon", "Chris Sanders", "animation"),
("Despicable Me", "Pierre Coffin", "animation"),
("Kung Fu Panda", "Mark Osborne", "animation"),
("Finding Mr Fox", "Wes Anderson", "animation"),
("The Incredibles", "Brad Bird", "animation"),

-- Thriller
("Se7en", "David Fincher", "thriller"),
("Gone Girl", "David Fincher", "thriller"),
("Shutter Island", "Martin Scorsese", "thriller"),
("The Silence of the Lambs", "Jonathan Demme", "thriller"),
("Prisoners", "Denis Villeneuve", "thriller"),
("Nightcrawler", "Dan Gilroy", "thriller"),
("The Girl with the Dragon Tattoo", "David Fincher", "thriller"),
("Zodiac", "David Fincher", "thriller"),
("No Country for Old Men", "Joel Coen", "thriller"),
("The Prestige", "Christopher Nolan", "thriller");


-- more movies based on director rather than just genre - also chatgpt generated
INSERT INTO movies (movieName, director, genre) VALUES

-- Quentin Tarantino
("Pulp Fiction", "Quentin Tarantino", "crime"),
("Kill Bill Vol 1", "Quentin Tarantino", "action"),
("Inglourious Basterds", "Quentin Tarantino", "war"),
("Django Unchained", "Quentin Tarantino", "western"),

-- Steven Spielberg
("Jurassic Park", "Steven Spielberg", "adventure"),
("E.T.", "Steven Spielberg", "sci-fi"),
("Saving Private Ryan", "Steven Spielberg", "war"),
("Catch Me If You Can", "Steven Spielberg", "drama"),

-- Martin Scorsese
("Taxi Driver", "Martin Scorsese", "drama"),
("Raging Bull", "Martin Scorsese", "drama"),
("Casino", "Martin Scorsese", "crime"),
("Gangs of New York", "Martin Scorsese", "crime"),

-- Tim Burton
("Beetlejuice", "Tim Burton", "fantasy"),
("Edward Scissorhands", "Tim Burton", "fantasy"),
("Charlie and the Chocolate Factory", "Tim Burton", "family"),
("Sleepy Hollow", "Tim Burton", "horror"),

-- Greta Gerwig
("Lady Bird", "Greta Gerwig", "drama"),
("Little Women", "Greta Gerwig", "drama"),
("Barbie", "Greta Gerwig", "comedy"),

-- Wes Anderson
("The Grand Budapest Hotel", "Wes Anderson", "comedy"),
("Moonrise Kingdom", "Wes Anderson", "drama"),
("The Royal Tenenbaums", "Wes Anderson", "comedy"),
("Asteroid City", "Wes Anderson", "comedy"),

-- Jordan Peele
("Us", "Jordan Peele", "horror"),
("Nope", "Jordan Peele", "sci-fi"),

-- Christopher McQuarrie
("Jack Reacher", "Christopher McQuarrie", "action"),
("Mission Impossible Fallout", "Christopher McQuarrie", "action"),
("Mission Impossible Rogue Nation", "Christopher McQuarrie", "action");



SELECT * FROM movies;


SELECT movieName, director, genre
FROM movies
WHERE genre = 'romance';
