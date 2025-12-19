def clean_data(df):
    """
    Performs basic data cleaning:
    - Remove duplicates
    - Handle missing values
    """

    cleaning_report = {}

    # Remove duplicate rows
    initial_rows = df.shape[0]
    df = df.drop_duplicates()
    cleaning_report["duplicates_removed"] = initial_rows - df.shape[0]

    # Missing values count
    missing_values = df.isnull().sum().to_dict()
    cleaning_report["missing_values"] = missing_values

    # Fill missing numeric values with median
    for col in df.select_dtypes(include=["number"]).columns:
        df[col].fillna(df[col].median(), inplace=True)

    # Fill missing categorical values with mode
    for col in df.select_dtypes(include=["object"]).columns:
        df[col].fillna(df[col].mode()[0], inplace=True)

    return df, cleaning_report
