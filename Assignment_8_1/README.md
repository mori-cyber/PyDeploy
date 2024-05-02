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
      
## for deploy in liara run these steps:

- [ ] created an image with docker:
```
docker build -t python.
```
 - [ ] We run a container:
```
docker run -d -p 80:80 python
```
 - [ ] login in liara:
 ```
for ubuntu first run this command: curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bas
and this command:  nvm install 20
liara login
```
 - [ ] then deploy that Python API in Liara:
```
liara deploy 
```
####Note: Before any deployment in Liara, you need to register on the Liara website and create a Docker platform.
```
https://docs.liara.ir/cli/install/
```
output is :
https://streamlit123.liara.run/
