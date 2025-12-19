# 1. Base image (Python)
FROM python:3.11-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy requirements first (for caching)
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy project files
COPY . .

# 6. Expose Flask port
EXPOSE 5000

# 7. Run the app
CMD ["python", "run.py"]
