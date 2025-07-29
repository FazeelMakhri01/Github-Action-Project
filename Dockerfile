FROM python:3.10-slim

WORKDIR /app

COPY app.py .
RUN pip install requests

ENTRYPOINT ["python", "app.py"]   #somechanges
