FROM python:3-slim
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PYTHONUNBUFFERED=TRUE
WORKDIR /app
EXPOSE ${PORT}
RUN apt update && apt-get install -y build-essential libssl-dev libffi-dev python3-dev
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./src /app
RUN adduser -u 1000 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser
CMD gunicorn main:app -b :${PORT} -k uvicorn.workers.UvicornH11Worker --reload
