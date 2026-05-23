import matplotlib.pyplot as plt
import seaborn as sns


def show_heatmap(df):

    corr = df.corr(numeric_only=True)

    sns.heatmap(
        corr,
        annot=True
    )

    plt.title("Correlation Heatmap")

    plt.show()


def show_histogram(df):

    plt.hist(df["CGPA"])

    plt.title("CGPA Distribution")

    plt.xlabel("CGPA")

    plt.ylabel("Frequency")

    plt.show()


def show_scatter(df):

    plt.scatter(
        df["Coding"],
        df["Placed"]
    )

    plt.title("Coding vs Placement")

    plt.xlabel("Coding Score")

    plt.ylabel("Placed")

    plt.show()