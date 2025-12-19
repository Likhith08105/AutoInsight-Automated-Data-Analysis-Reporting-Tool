# AutoInsight – Automated Data Analysis & AI-Powered Reporting Tool

AutoInsight is a web-based application that allows users to upload CSV datasets and automatically generate meaningful data insights.  
The system performs data analysis, anomaly detection, and provides AI-generated explanations in simple, human-readable language.

This project is designed to demonstrate practical skills in data analysis, machine learning, backend development, containerization, and deployment.

---

## 🚀 Live Demo
🔗 https://autoinsight.onrender.com

---

## 📌 Features
- Upload structured CSV datasets
- Automatic data loading and preprocessing
- Basic exploratory data analysis (EDA)
- Anomaly detection using Isolation Forest
- AI-generated insights in plain English
- Clean and professional user interface
- Fully Dockerized application
- Deployed on Render cloud platform

---

## 🛠 Tech Stack
- **Backend:** Python, Flask  
- **Data Analysis:** Pandas, NumPy  
- **Machine Learning:** Scikit-learn (Isolation Forest)  
- **AI Insights:** LLM-based text generation  
- **Frontend:** HTML, CSS  
- **Containerization:** Docker  
- **Deployment:** Render  
- **Version Control:** Git, GitHub  

---

## 📂 Project Structure

AutoInsight/
│
├── app/
│ ├── main.py # Application routes and workflow
│ └── services/ # Data processing & ML logic
│
├── templates/ # HTML templates
├── static/ # CSS styles
├── uploads/ # Uploaded CSV files
│
├── Dockerfile # Docker configuration
├── requirements.txt # Python dependencies
├── run.py # Application entry point
├── .env # Environment variables
└── README.md


---

## ⚙️ How It Works
1. User uploads a CSV file through the web interface  
2. The backend loads and cleans the dataset  
3. Exploratory analysis is performed  
4. Anomaly detection identifies unusual records  
5. AI generates insights in plain, easy-to-understand language  
6. Results are displayed in a structured report format  

---

## 🐳 Docker Support
The entire application is containerized using Docker to ensure consistent behavior across environments.

Render automatically builds and runs the Docker container during deployment.

---

## ▶️ Run Locally (Optional)
```bash
git clone https://github.com/your-username/AutoInsight-Automated-Data-Analysis-Reporting-Tool.git
cd AutoInsight
pip install -r requirements.txt
python run.py
