# 1️⃣ Use a lightweight Python base image
# FROM python:3.11-slim

# # 2️⃣ Set working directory inside container
# WORKDIR /app

# # 3️⃣ Copy requirements first (for caching)
# COPY requirements.txt .

# # 4️⃣ Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # 5️⃣ Copy the rest of the backend code
# COPY ./app /app

# # 6️⃣ Expose port for FastAPI
# EXPOSE 8000

# # 7️⃣ Start the FastAPI server
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]




FROM python:3.12-slim

WORKDIR /app

COPY app/ .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py", "interactive"]
