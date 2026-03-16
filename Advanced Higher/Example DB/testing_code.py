def display_movie_names(cur):
    sql = """
    SELECT movieName FROM movies;    
    """
    cur.execute(sql)
    rows = cur.fetchall()

    print("")
    print('Fetching all movie names \n')
    for movieName in rows:
        print(f"Movie: {movieName}")

def display_movie_genres(cur):
    sql = """
    SELECT genre FROM movies;
"""
    cur.execute(sql)
    rows = cur.fetchall()

    print("")
    print("Fetching all genres")

    for genre in rows:
        print(f"Genre: {genre}")
