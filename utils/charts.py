import plotly.graph_objects as go


def score_gauge(score, title):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,

            title={"text": title},

            gauge={
                "axis": {"range": [0, 100]},

                "bar": {"color": "green"},

                "steps": [

                    {"range": [0, 50], "color": "#ffcccc"},

                    {"range": [50, 80], "color": "#fff4b3"},

                    {"range": [80, 100], "color": "#ccffcc"}

                ]
            }
        )
    )

    fig.update_layout(
        height=300,
        margin=dict(l=10, r=10, t=40, b=10)
    )

    return fig
