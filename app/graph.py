from altair import Chart, Tooltip
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    graph = Chart(
        df,
        title=f"{y} by {x} for {target}",
    ).mark_circle(size=100).encode(
        x=x,
        y=y,
        color=target,
        tooltip=Tooltip(df.keys().tolist())
    ).properties(
        background="000000"
    ).configure(
        legend={
            "titleColor": "#AAAAAA",
            "labelColor": "#AAAAAA",
            "padding": 10
        },
        title={
            "color": "#AAAAAA",
            "fontSize": 26,
            "offset": 30
        },
        axis={
            "titlePadding": 20,
            "titleColor": "#AAAAAA",
            "labelPadding": 5,
            "labelColor": "#AAAAAA",
            "gridColor": "#333333",
            "tickColor": "#333333",
            "tickSize": 10
        },
        view={
            "stroke": "#333333"
        }
    )

    return graph
