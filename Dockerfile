FROM python.3.12-slim 

WORKDIR /app

COPY main.py functions.py ./

CMD ["python", "main.py"]