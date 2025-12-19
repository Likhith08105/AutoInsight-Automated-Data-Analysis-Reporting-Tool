import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_ai_insights(eda_report, anomaly_report):
    """
    Generate AI insights using LLaMA via Groq API
    """

    prompt = f"""
    You are a data analyst.

    Dataset shape: {eda_report['shape']}
    Columns: {eda_report['columns']}
    Anomalies detected: {anomaly_report['anomalies_detected']}
    Total records: {anomaly_report['total_records']}

    Provide:
    1. Key insights from the dataset
    2. Possible reasons for anomalies
    3. Simple recommendations
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content
