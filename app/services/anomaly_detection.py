from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    """
    Detects anomalies using Isolation Forest
    """

    # Select only numeric columns
    numeric_df = df.select_dtypes(include=["number"])

    # If no numeric columns, skip anomaly detection
    if numeric_df.empty:
        return df, {
            "anomalies_detected": 0,
            "message": "No numeric columns available for anomaly detection"
        }

    model = IsolationForest(
        n_estimators=100,
        contamination=0.05,
        random_state=42
    )

    # Fit and predict
    anomaly_labels = model.fit_predict(numeric_df)

    # -1 indicates anomaly
    df["anomaly"] = anomaly_labels
    anomaly_count = (anomaly_labels == -1).sum()

    report = {
        "anomalies_detected": int(anomaly_count),
        "total_records": df.shape[0]
    }

    return df, report
