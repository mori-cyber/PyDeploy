In the continuation of the website project, in this work, we learned docker-compose and how to work with it.


##Docker
```
docker pull postgres
docker run -p 5432:5432 --name some-postgres -e POSTGRES_PASSWORD=password -e POSTGRES_USER=username -e POSTGRES_DB=db_postgres -d postgres
docker build -t my_web_app .
docker run --rm -p 5432:5432 -p 8080:5000 -v $(pwd):/myapp my_web_app
```
##Docker Network
```
docker network create my_networks
docker build -t my_web_app .
docker run --network my_network --name some-postgres -e POSTGRES_PASSWORD=password -e POSTGRES_USER=username -e POSTGRES_DB=db_postgres -d
```
```
docker run --rm --network my_network --name my_web_app -p 8080:5000 -v $(pwd):/myapp my_web_app
```
##Docker compose
```
docker build -t my_web_app .
docker compose up -d
docker compose stop
docker compose down

```
