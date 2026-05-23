from preprocessing import (
    load_data,
    clean_data
)

from analysis import (
    correlation_analysis,
    employability_score
)

from visualisation import (
    show_heatmap,
    show_histogram,
    show_scatter
)


df = load_data()

df = clean_data(df)

correlation_analysis(df)

show_heatmap(df)

show_histogram(df)

show_scatter(df)

df = employability_score(df)