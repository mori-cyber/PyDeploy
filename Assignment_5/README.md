# How to Deploy Python API in the Liara Server:

1- First, we install Docker
```
[https://desktop.docker.com/mac/main/arm64/Docker.dmg?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module&_gl=1*1fa7fm*_ga*MjAxOTg3MDcyOC4xNzEyODE4MTM0*_ga_XJWPQMJYHQ*MTcxMzIyMDMzNy4yLjAuMTcxMzIyMDMzNy42MC4wLjA.](https://www.docker.com/get-started/)
```
2- We make a folder (for example Assignment_5) <br>
3- In this folder, we create two files, 
- [x] requirements.txt
- [x]  Dockrfile <br>
4- We create an app folder inside the previous folder and put the Python file and database in it. <be>
- [X] main.py
- [X] todo.db <br>
 5- We build an attractive Docker image:
```
docker build -t morteza .
```
6- We run a container from the image:
```
docker run -d -p 80:80 morteza
```
## Two methods for deploy in Liara:
- [x] a- Deployment with a browser.
- [x] b- Deployment with Liara CLI. <br>
## We used the Liara CLI method As follows:
```
npm install -g @liara/cli
liara login
liara deploy --platform docker --port 80
```
The important point is that Liana must be installed in the path of your code 
folder and the installation and deployment operations must be done in the cmd environment.


