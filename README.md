# game scoreboard – flask project

author: roi taba  
course: devops – technion 2025

## description

this is a simple flask web app to manage game scores.  
the user can add new scores, delete players, sort them by key and also see the average score.  
the app includes basic html (index.html) and can be run locally, with docker, or deployed to aws elastic beanstalk.

no css or frontend styling, only the logic and one template.

---

## project structure

```
.
├── app.py
├── functions.py
├── templates/
│   └── index.html
├── requirements.txt
├── Dockerfile
└── .elasticbeanstalk/
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

1. init eb:
   ```
   eb init
   ```

2. create env:
   ```
   eb create game-score-env
   ```

3. deploy:
   ```
   eb deploy
   ```

---

## notes

- tested on python 3.12  
- index.html is basic and not styled  
- backend logic only  
- no database or login, just in memory list  
- no css/js used  
