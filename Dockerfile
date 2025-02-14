FROM python:3.13-slim

WORKDIR /app

WORKDIR app/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY backendpython_reservation/ . 

EXPOSE 8000
CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port","8000"]

#docker build -t videogames_python_backend.