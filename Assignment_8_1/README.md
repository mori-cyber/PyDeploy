- [x] We Write a Counter App
    - [ ]  Here is a sample **Counter app ([Online Demo](https://gallery.flet.dev/counter/))**
- [x] Deploy it 🚀 using docker 🐳 on Liara
For deploy in liara following this steps:
- [ ]  create Dockerfile for me:
 ```
 # app/Dockerfile

FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]

 ```
- [ ]  Create a requirements.txt file
- [ ]   created an image with docker:
```
docker build -t my_fastapi.
```
 - [ ] We run a container:
```
docker run -d -p 80:80 fastapi_6
```
 - [ ] then login in liara:
 ```
liara login
```
 - [ ] then deploy that Python API in Liara:
```
liara deploy --platform docker --port 80
```
