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


### SQLAlchemy

SQLAlchemy offers multiple ways of interacting with DB. 

* Can interact with Engine layer and send SQL statements to DB.
* Can create Python objects and send SQL expressions to DB.
* Use the ORM (highest level)

**Good Design Practice (Opinion)**

Interacting with databases using good design practice:

* Keep your code Pythonic. Work in classes and objects as much as possible.
* Makes switching to a different backend easy in the future.
 * Avoid writing raw SQL until absolutely necessary

**Layers of SQLAlchemy**

![Abstraction Layers](md_img/sqlalchemy-layers-of-abstraction.png  "Layers")

* DBAPI (uses psycopg2 under the hood)
* The [Dialect](https://docs.sqlalchemy.org/en/13/dialects/)
* The [Connection Pool](https://docs.sqlalchemy.org/en/13/core/pooling.html)
* The [Engine](https://docs.sqlalchemy.org/en/13/core/engines.html)
* SQL Expressions
* SQLAlchemy ORM (optional)

_Can use SQLAlchemy to communicate with DB using any of the three layers of abstraction: ORM, Expressions level, or use the DBAPI level._

**The Dialect** - abstracts away the specific database system we are using so we do not need to use SQL specific to that DBMS. Makes it possible to interact with any DBMS.

**Connection Pooling** - don't need to open/close DB connections manually.

* Handles dropped connections
* Avoids many small calls to the DB
* Avoids opening and closing connections for every change

**The Engine** - don't need to open/close DB connections manually. Lowest level of abstraction - similar to using psycopg2. The Engine in SQLAlchemy refers to both _itself, the Dialect and the Connection Pool_, which all work together to interface with our database.

![Engine Structure](md_img/sqla_engine_arch.png  "Engine Structure")

**SQL Expressions** - use Python objects to create SQL expressions. Although, they require you to know SQL they are a step above and avoid writing SQL string compositions in your code.


**SQL ORM** - Highest level of abstraction. Create Python classes that map to DB objects. Wraps the Expressions and Engine layer.

