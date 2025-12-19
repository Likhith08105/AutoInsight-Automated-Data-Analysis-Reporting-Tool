def generate_eda(df):
    """
    Generates basic EDA summary
    """

    eda_report = {
        "shape": df.shape,
        "columns": list(df.columns),
        "data_types": df.dtypes.astype(str).to_dict(),
        "summary_stats": df.describe().to_dict()
    }

    return eda_report
