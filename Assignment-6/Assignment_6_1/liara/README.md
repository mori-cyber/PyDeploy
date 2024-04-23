In this task, we first created a PostgreSQL database in Liara.<br>
Then we used  that link to connect to this database.
- [ ]  created an image with docker:
```
docker build -t my_fastapi.
```
- [x] we run a container:
```
docker run -d -p 80:80 fastapi_6
```
- [x] then login in liara:
```
liara login
```
- [x] then deploy that Python API in Liara:

```
liara deploy --platform docker --port 80
```
output is:
```
![screencapture-fastapi-6-liara-run-docs-2024-04-24-00_04_47](https://github.com/mori-cyber/PyDeploy/assets/65276280/a872d341-ec8e-46ed-878c-6ae28eeaa420)

```

