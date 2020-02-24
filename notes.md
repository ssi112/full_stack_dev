## Full-Stack Developer

Tech stack we'll be gaining proficiency in:

* Python 3
* Flask
* PostgresSQL
* psycopg2 (wrapper around libpq)
* SQLAlchemy
* Flask-SQLAlchemy

Required Software

* CLI: Terminal or GitBash
* Python (version 3.7 or later)
* PIP
* Code Editor
* Web Browser

### PostgreSQL CLI

Start psql with a connection to dbname. Optionally useanother user than current user: 

`psql` `<dbname> [<username>]`

Logging in connects to default DB (ssi112 in my case).  To show the current search path you can use the following command:

`SHOW search_path;`

And to put the new schema in the path, you could use:

`SET search_path TO myschema;`

On local installation: `set search_path to sakila;`

Or if you want multiple schemas: `SET search_path TO myschema, public;`

Otherwise, will need to enter full DB and schema to access tables.

`select * from ssi112.sakila.actor`

**Other PSQL commands:**

Connect to a specific DB when logging in:  `psql <dbname>`

Once logged in connect to a specifc DB: `\c` `<dbname>`

List all DBs on server `\l`

Show table info (can set the search path first to eliminate the schema): `\d sakila.actor`

`SET search_path TO sakila;`

Now show all DB tables: `\dt`

Quit the CLI: `\q`

**Typical Default Connection Settings**

Connection Setting | Default
-------------------- | --------------
Host | localhost (aka, 127.0.0.1)
Port | 5432
Username | postgres
Password | (None)








