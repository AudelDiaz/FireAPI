FROM python:3.9-slim
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PYTHONUNBUFFERED=TRUE
WORKDIR /app
EXPOSE ${PORT}
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./src /app
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser
CMD gunicorn main:app -b :${PORT} -k uvicorn.workers.UvicornH11Worker --reload
