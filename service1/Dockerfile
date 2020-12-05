FROM python:3.7
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["gunicorn", "--workers=2", "-b", "0.0.0.0:5000", "app:app"]
COPY . .
