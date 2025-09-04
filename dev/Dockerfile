FROM python:3.9-slim

WORKDIR /app

# Copy requirements.txt from current directory
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy all other files from current directory
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]