import sqlite3 as sl

#create connection to the database named my-test.db
con = sl.connect('movies.db')

#once you have a Connection, you can create a Cursor object and call its execute9) method to preform SQL commands
c = con.cursor()

#get the count of tables with the name
c.execute(''' SELECT count(name) FROM sqlite_master WHERE Type='table' AND name='MOVIES' ''')

#if the count is 1, then table exists
if c.fetchone()[0]==1 :
    print('Table exists.')
else :
    #does not exist, create
    print('Table does not exist')

    #create a table with the primary key, name field of text, and an age field of integer
    with con:
        con.execute("""
            CREATE TABLE MOVIES (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            MovieName TEXT,
            Genre TEXT,
            ReleaseDate INTEGER
        );
    """)

    #create sql to insert data into the table
    sql = 'INSERT INTO MOVIES (id, MovieName, Genre, ReleaseDate) values(?,?,?,?)'
    data = [
        (1, 'Harry Potter and the Sorcerers Stone', 'Fantasy Fiction', 2001),
        (2, 'Harry Potter and the Chamber Of Secrets', 'Fantasy Fiction', 2002),
        (3, 'Harry Potter and the Prisoner of Azkaban', 'Fantasy Fiction', 2004),
        (4, 'Harry Potter and the Goblet Of Fire', 'Fantasy Fiction', 2005),
        (5, 'Harry Potter and the Order Of The Phoenix', 'Fantasy Fiction', 2007),
        (6, 'Harry Potter and the Halfblood Prince', 'Fantasy Fiction', 2009),
        (7, 'Harry Potter and the Deathly Hallows Part 1', 'Fantasy Fiction', 2010),
        (8, 'Harry Potter and the Deathly Hallows Part 2', 'Fantasy Fiction', 2011),
        (9, 'Fantastic Beasts and where to find them', 'Fantasy Fiction', 2016),
        (10, 'Indiana Jones and the Lost Ark', 'Adventure', 1981)
        ]

    #run sql query
    with con:
        con.executemany(sql, data)

        #connect and read back data
with con:
    data = con.execute("SELECT * FROM MOVIES WHERE ReleaseDate >= 2000")
    for row in data:
        print(row)
    data = con.execute("SELECT * FROM MOVIES WHERE ReleaseDate < 2000")
    for row in data:
        print(row)


