'''
demo_psycopg2_basic_use.py - basic usage of psycopg2

database was previously created using psql

Reference: https://www.psycopg.org/docs/usage.html
'''

import psycopg2

# connect to Postgres server
conn = psycopg2.connect('dbname=todoapp')

cursor = conn.cursor()

# open a cursor
cur = conn.cursor()

# set search path to public
cur.execute("SET search_path TO public;")

# drop table if it exists
cur.execute("DROP TABLE IF EXISTS todos;")

# recreate the todos table
# use tripple quotes for multiline text
cur.execute("""
    CREATE TABLE todos (
    id serial PRIMARY KEY,
    description VARCHAR NOT NULL
    );
    """)

# create a simple record
cur.execute("INSERT INTO todos (id, description) VALUES (1, 'Completed');")


# create a record using string interpolation
cur.execute("INSERT INTO todos (id, description) VALUES (%s, %s);", (2, 'Yaw Zaa'))

'''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
From psycopg2 documentation (link above)

Warning: Never, never, NEVER use Python string concatenation (+) or string
parameters interpolation (%) to pass variables to a SQL query string.
Not even at gunpoint.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''

# create a record using string parameters and passing a dictionary
insert_sql = "INSERT INTO todos (id, description) VALUES (%(id)s, %(description)s);"

insert_data = {
    'id': 3,
    'description': 'work in progress'
}

cur.execute(insert_sql, insert_data)

# commit transactions
conn.commit()


####################################################
# fetchall()
# Fetch all (remaining) rows of a query result, returning them as a list of tuples.
# An empty list is returned if there is no more record to fetch.

####################################################
# fetchmany( size )
# Fetch the next set of rows of a query result, returning a list of tuples.
# An empty list is returned when no more rows are available.

####################################################
# fetchone()
# Fetch the next row of a query result set, returning a single tuple, or
# None when no more data is available:
# An empty list is returned when no more rows are available.


# --------------------------------------------
# fetch all the results of the above inserts
cur.execute("SELECT * from todos;")

# returns a list of tuples
result = cur.fetchall()
print("\n--------------------------------------------------------")
for row in result:
    print("id: {} - description: {}".format(row[0], row[1]))

# commit transactions
conn.commit()

# must explicitly close the cursor and connection
cur.close()
conn.close()



