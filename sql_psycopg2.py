import psycopg2

# connect to chinook database

connection = psycopg2.connect(database="chinook")
cursor = connection.cursor()

#cursor.execute('SELECT * FROM "Artist"')
cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s',[51])
cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

#fetch the results

results = cursor.fetchall()

# fetch the single result
# result = cursor.fetchone()

connection.close()

for result in results:
    print(result)