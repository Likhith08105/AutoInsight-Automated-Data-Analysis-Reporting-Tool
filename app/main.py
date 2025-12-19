from flask import Blueprint, render_template, request
import os

# Service imports
from app.services.data_loader import load_csv
from app.services.data_cleaning import clean_data
from app.services.eda import generate_eda
from app.services.anomaly_detection import detect_anomalies
from app.services.llm_insights import generate_ai_insights

# -------------------------
# Blueprint MUST be defined BEFORE routes
# -------------------------
main_bp = Blueprint("main", __name__)

UPLOAD_FOLDER = "uploads"


@main_bp.route("/")
def home():
    return render_template("upload.html")


@main_bp.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")

    if not file or not file.filename.endswith(".csv"):
        return "Invalid file. Please upload a CSV file.", 400

    # Ensure uploads folder exists
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    df = load_csv(file_path)
    cleaned_df, cleaning_report = clean_data(df)
    eda_report = generate_eda(cleaned_df)
    final_df, anomaly_report = detect_anomalies(cleaned_df)
    ai_insights = generate_ai_insights(eda_report, anomaly_report)

    return render_template(
        "report.html",
        cleaning_report=cleaning_report,
        eda_report=eda_report,
        anomaly_report=anomaly_report,
        ai_insights=ai_insights
    )

