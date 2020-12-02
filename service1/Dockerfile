FROM python:3.7
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["/usr/local/bin/python3", "app.py"]
