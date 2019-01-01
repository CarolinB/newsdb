#!/usr/bin/env python

"""
Database Code for the News Database:
3 functions that print the answers to the following questions -
1) Return the three articles with the most views
2) Return the authors whose articles got the most views
3) Return the days when more than 1 percent of all requests led to errors
"""


import psycopg2
from datetime import datetime

DBNAME = "news"


def get_3_most_popular_articles():
    # Return the three articles with the most views
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""
        SELECT
                a.title,
                COUNT(a.id) AS count
        FROM articles a
        JOIN log l ON l.path = CONCAT('/article/', a.slug)
        GROUP BY a.id
        ORDER BY count DESC
        LIMIT 3
        """)
    most_popular_3articles = c.fetchall()
    db.close()
    print("Most popular 3 articles of all time: \n")
    x = 0
    while x < len(most_popular_3articles):
        print("\"" + str(most_popular_3articles[x][0])
              + "\"" + " - "
                + str(most_popular_3articles[x][1]) + " views")
        x = x+1


def get_authors_with_most_views():
    # Return the authors whose articles got the most views
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""
        SELECT
                auth.name, COUNT(auth.id) AS views
        FROM authors auth
        JOIN articles a ON (a.author = auth.id)
        JOIN log l ON (l.path = CONCAT('/article/', a.slug))
        GROUP BY auth.id
        ORDER BY views DESC;
        """)
    authors_most_views = c.fetchall()
    db.close()
    print("\nMost popular article authors of all time: \n")
    x = 0
    while x < len(authors_most_views):
        print(str(authors_most_views[x][0])
              + "\"" + " - "
                + str(authors_most_views[x][1]))
        x = x+1


def convert_date(datevalue):
        strDate = str(datevalue)
        objDate = datetime.strptime(strDate, '%Y-%m-%d')
        format_date = datetime.strftime(objDate, '%b %d, %Y')
        return format_date


def get_days_errors_higher_1percent():
    # Return the days when more than 1% of all requests led to errors
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""
        SELECT
                to_char(DAY,'FMMonth DD, YYYY'),
                round(errorfraction * 100,2) AS percentage
        FROM
                (SELECT
                        time::DATE AS day,
                        (COUNT(CASE WHEN status <> '200 OK'
                                THEN 1 END)::decimal)
                        / (COUNT(*)::decimal) AS errorfraction
                FROM log
                GROUP BY day) AS errorsperday
        WHERE errorfraction > 0.01;""")
    errors_higher_1percent = c.fetchall()
    db.close()
    print("\nDays with more than 1% of all requests leading to errors: \n")

    x = 0
    while x < len(errors_higher_1percent):
        date = errors_higher_1percent[x][0]
        percent = errors_higher_1percent[x][1]
        print(str(date) + " - " + str(percent))
        x = x+1


get_3_most_popular_articles()
get_authors_with_most_views()
get_days_errors_higher_1percent()


print('\nI wish you a very happy new year!! :)')
