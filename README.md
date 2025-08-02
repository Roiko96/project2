# game scoreboard – project

author: roi taba  
course: devops – technion 2025

## description

this is a simple flask web app to manage game scores.  
the user can add new scores, delete players, sort them by key and also see the average score.  
the app includes basic html (index.html) and can be run locally, with docker, or deployed to aws elastic beanstalk.

no css or frontend styling, only the logic and one template.
### hope eli will like it :) 
---


## run with docker

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
