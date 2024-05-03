- [x] We Write a Counter App
    - [ ]  Here is a sample **Counter app ([Online Demo](https://gallery.flet.dev/counter/))**
- [x] Deploy it 🚀 using docker 🐳 on Liara
- [ ] 
#### For deploy in liara following this steps:
- [ ]  create Dockerfile(https://docs.streamlit.io/deploy/tutorials/docker) for me:
 ```
# app/Dockerfile

FROM python

WORKDIR /Assignment_8_1
RUN git clone https://github.com/mori-cyber/PyDeploy.git .

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

COPY  . .

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]

 ```
- [ ]  Create a requirements.txt file
      

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
