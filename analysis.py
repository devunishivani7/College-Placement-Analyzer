def correlation_analysis(df):

    print("Correlation Analysis:")

    print(
        df.corr(numeric_only=True)
    )


def employability_score(df):

    df["Employability"] = (
        df["Coding"]
        + df["Aptitude"]
        + df["Communication"]
    ) / 3

    print()

    print("Employability Scores:")

    print(
        df[[
            "Name",
            "Employability"
        ]]
    )

    return df