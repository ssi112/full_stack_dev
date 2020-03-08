# Full Stack Developer

### Note this is the Nanodegree offered by Udacity and NOT the free foundation course

<a href="https://www.udacity.com/">
  <img src="https://s3-us-west-1.amazonaws.com/udacity-content/rebrand/svg/logo.min.svg" width="300" alt="Udacity logo">
</a>

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Intro](#intro)
- [Project 1](#project1)
- [License](#license)

## Intro
This nano-degree is designed to enable learners to build database backed APIs and web applications.

* Design and build a database for a software application
* Create and deploy a database-backed web API (Application Programming Interface)
* Secure and manage user authentication and access control for an application backend
* Deploy a Flask-based web application to the cloud using Docker and Kubernetes

#### Migrations

* `flask db init` setup migrations for the app
* `dropdb todoapp -p 5433` drop the db (so flask-migrate can be aware of it)
* `createdb todoapp -p 5433` create db
* `flask db migrate` migrate the db
* `flask db upgrade` run upgrade
* `flask db downgrade` rollback upgrade

## Project 1 <a name="project1"></a>
Create a booking site Fy-yur that facilitates bookings between artists who can play at venues, and venues who want to book artists.

* [Starter code](https://github.com/udacity/FSND/tree/master/projects/01_fyyur/starter_code) with overview, structure, instructions and criteria.
* The rubric for this project can be found [here](https://review.udacity.com/#!/rubrics/2653/view)

Most of the code for this project is in place. It needs the data models built to access a PostgreSQL database using SQLAlchemy.

Refer to the starter code project for specifics instructions and requirements.

## License
The contents of this repository are covered under the [MIT License](mit_license.md)
