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

## how to deploy to aws (elastic beanstalk)

1. open cloud9.

2. create env: flask-dev or something you want and running this commands pls:
   ```
      sudo su
   apt update && apt upgrade -y
   apt install python3-flask / apt install -r requirements.txt
   mkdir templates
   mv index.html templates/
   cd templates/
   ll -lhtar
   cd ..
   pwd (you need to be at main folder called project2)
   ```
  
3. go to ec2 sg group of the relevant instance and edit inbound rules and add tcp method connection for 0.0.0.0 port 5000
  
4. running the appp:
   ```
   python app.py
   ```
5. from the ec2 panel scroll right to PIP and copy the public ip and open in new browser and type http://yourPip:5000
6. and that its, enjoyyy! 
---
## notes

- tested on python 3.12  
- index.html is basic and not styled  
- backend logic only !
- no database or login, just in memory list  
- no css/js used

<img width="1340" height="952" alt="Screenshot 2025-08-02 214613" src="https://github.com/user-attachments/assets/707c952a-0406-4096-ac4e-77d8e796f6d8" />
<img width="553" height="975" alt="Screenshot 2025-08-02 215112" src="https://github.com/user-attachments/assets/24b9d403-21b8-4767-b189-689669fb2348" />
<img width="1289" height="730" alt="Screenshot 2025-08-02 214241" src="https://github.com/user-attachments/assets/935c84a4-7266-4065-ba0c-3082f63da4b4" />
