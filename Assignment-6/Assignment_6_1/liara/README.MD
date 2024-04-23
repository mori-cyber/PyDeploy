In this task, we first created a POSTGRESQL database in Liara.
Then we used  THAT link to connect to this database.
- [ ]  created an image with docker:
```
docker build -t my_fastapi .
```
- [x] we run a container:
```
docker run -d -p 80:80 fastapi_6
```
- [x] then login in liara:
```
liara login
```
- [x] then deploy that python api in liara:

```
liara deploy --platform docker --port 80
```
output is

