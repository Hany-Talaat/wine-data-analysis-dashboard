from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


# Load dataset
df = pd.read_csv('data/Wine_data.csv')


# Basic cleaning
df['country'] = df['country'].fillna(df['country'].mode()[0])
df['price'] = df['price'].fillna(df['price'].mean())

df['province'] = df['province'].fillna('Unknown')


# Italy analysis
df_italy = df[df['country'] == 'Italy']

italy_summary = (
    df_italy
    .groupby('province')[['price', 'points']]
    .mean()
    .nlargest(5, 'points')
    .reset_index()
)


# Convert data to long format
df_melted = italy_summary.melt(
    id_vars=['province'],
    value_vars=['price', 'points'],
    var_name='Metric',
    value_name='Value'
)


# Create Plotly figure
fig = px.bar(
    df_melted,
    x="province",
    y="Value",
    color="Metric",
    barmode="group",
    title="Average Wine Price vs. Rating Points Across Top Italian Provinces"
)


# Create Dash application
app = Dash(__name__)


app.layout = html.Div(
    children=[
        html.H1(
            "Italian Wine Dashboard",
            style={'textAlign': 'center'}
        ),

        html.Div(
            "Interactive comparison of average price and quality score for top Italian wine provinces.",
            style={
                'textAlign': 'center',
                'marginBottom': '20px'
            }
        ),

        dcc.Graph(
            id='italy-wine-graph',
            figure=fig
        )
    ]
)


if __name__ == '__main__':
    app.run(debug=True)
