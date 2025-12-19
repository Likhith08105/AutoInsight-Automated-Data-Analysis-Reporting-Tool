import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "autoinsight-secret")
    UPLOAD_FOLDER = "uploads"
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10MB limit
