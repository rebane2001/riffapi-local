FROM python:3.11.3-slim
RUN mkdir /app
ADD riffapi-local.py /app
WORKDIR /app
RUN pip install Flask
EXPOSE 5144/tcp
CMD ["python3", "riffapi-local.py"]