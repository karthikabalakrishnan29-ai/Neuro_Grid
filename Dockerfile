# 1. Base Image - Python 3.9 use panrom
FROM python:3.9-slim

# 2. Working Directory set panrom
WORKDIR /app

# 3. Dependencies-a copy panni install panrom
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Motha project code-aiyum copy panrom
COPY . .

# 5. Environment variables set panrom
ENV PYTHONUNBUFFERED=1

# 6. API and Dashboard ports-a expose panrom
EXPOSE 8000 8501

# 7. Start command (FastAPI and Streamlit-a onna run panna oru script create pannalam)
CMD ["python", "run_app.py"]