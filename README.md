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
   docker run -it game-scoreboard
   ```

3. enjoy the code..

---
<img width="166" height="172" alt="Screenshot 2025-08-02 193427" src="https://github.com/user-attachments/assets/8f8d7fff-0f59-4904-bdc3-fa55635fe775" />
<img width="261" height="195" alt="Screenshot 2025-08-02 193414" src="https://github.com/user-attachments/assets/7258a679-a111-4e80-bb53-3b098e349036" />
<img width="354" height="207" alt="Screenshot 2025-08-02 193402" src="https://github.com/user-attachments/assets/cd79efd2-0bdb-408e-b134-546c3e0893d0" />
<img width="167" height="177" alt="Screenshot 2025-08-02 193354" src="https://github.com/user-attachments/assets/e0406e38-f41d-4a62-89b8-17a9688be6b3" />
<img width="209" height="236" alt="Screenshot 2025-08-02 193347" src="https://github.com/user-attachments/assets/4e044f46-c8ac-4e4d-8197-2703baf21a09" />
<img width="351" height="510" alt="Screenshot 2025-08-02 193343" src="https://github.com/user-attachments/assets/5cbe545e-8653-4ec4-a0a8-9400f34389ee" />
<img width="455" height="568" alt="Screenshot 2025-08-02 193338" src="https://github.com/user-attachments/assets/52611c1b-12a7-4c15-8be2-499fc2dca906" />
