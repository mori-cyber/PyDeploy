### In this task, we use the SQLAlchemy package to connect my  PostgreSQL database to my FastAPI project.
### We have designed a database with student and course tables.
### We have designed a database with two tables. Student and course. Student includes the following columns:
- [ ] ID
- [ ] first name
- [ ] last name
- [ ] average
- [ ] graduated
###  The course includes:
- [ ] ID
- [ ] name
- [ ]  units
### We need to Pull the PostgreSQL docker image:
```
docker pull postgres
```
### We need to Run the PostgreSQL docker container:
```
docker run -p 5432:5432 --name some-postgres -e POSTGRES_PASSWORD=morteza -e POSTGRES_USER=mori -e POSTGRES_DB=db -d postgres
```
### AND Change SQLAlchemy database url variable for example:
```
SQLALCHEMY_DATABASE_URL = "postgresql://mori:morteza@localhost:5432/db"
```


