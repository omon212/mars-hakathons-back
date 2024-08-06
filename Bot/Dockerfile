FROM python:3.9-slim

WORKDIR /bot

COPY . /bot

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
