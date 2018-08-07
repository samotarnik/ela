FROM python:3.7.0-slim-stretch

WORKDIR /ela

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ela.py .

CMD [ "python", "/ela/ela.py" ]
