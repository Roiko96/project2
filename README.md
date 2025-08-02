# game scoreboard – flask project

author: roi taba  
course: devops – technion 2025

## description

this is a simple flask web app to manage game scores.  
the user can add new scores, delete players, sort them by key and also see the average score.  
the app includes basic html (index.html) and can be run locally, with docker, or deployed to aws elastic beanstalk.

no css or frontend styling, only the logic and one template.
### hope eli will like it :) 
---

## project structure

```
.
|--- app.py
|--- functions.py
|--- main.py
|--- templates/
│   --- index.html
|--- requirements.txt
|--- Dockerfile
|--- .elasticbeanstalk/
```

---

## how to run locally

1. install flask:
   ```
   pip install -r requirements.txt
   ```

2. run the app:
   ```
   python app.py
   ```

3. open browser:
   ```
   http://localhost:5000
   ```

---

## how to run with docker

1. build image:
   ```
   docker build -t game-scoreboard .
   ```

2. run container:
   ```
   docker run -p 5000:5000 game-scoreboard
   ```

3. open in browser:
   ```
   http://localhost:5000
   ```

---

## how to deploy to aws (elastic beanstalk)

1. open cloud9.

2. create env: flask-dev or something you want and running this commands pls:
   ```
      sudo su
   apt update
   apt upgrade -y
   apt install python3-flask
   mkdir templates
   mv index.html templates/
   cd templates/
   ll -lhtar
   cd ..
   cd ..
   pwd (you need to be at main folder called project2)
   ```
  
3. running the appp:
   ```
   python app.py
   ```
4. go to ec2 sg group of the relevant instance and edit inbound rules and add tcp method connection for 0.0.0.0 port 5000
5. from the ec2 panel scroll right to PIP and copy the public ip and open in new browser and type https://the-pip:5000
6. and that its, enjoyyy! 
---

## notes

- tested on python 3.12  
- index.html is basic and not styled  
- backend logic only !
- no database or login, just in memory list  
- no css/js used  
