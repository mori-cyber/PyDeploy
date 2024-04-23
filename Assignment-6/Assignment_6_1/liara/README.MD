In this task, we first created a POSTGRESQL database in Liara.
Then we used  THAT link to connect to this database.
- [ ]  created an image with docker:
```
docker build -t my_fastapi .
```
then we run a container:
```
docker run -d -p 80:80 fastapi_6
```
then login in liara:
```
liara login
```
then deploy that python api in liara:
```
liara deploy --platform docker --port 80
'''

