from cs50 import SQL

db = SQL("sqlite:///movies.db")


toprint = db.execute("SELECT COUNT(title) FROM movies WHERE year = 2000")
print(toprint)