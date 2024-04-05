from dash import Dash, dcc, html, callback, Output, Input
import plotly.express as px
import pandas as pd

# kyusyu.csvデータ
data = {
    'category': ['tops', 'tops', 'tops','tops', 'bottoms', 'bottoms', 'bottoms', 'bottoms'],
    'prefecture': ['Fukuoka', 'Saga', 'Nagasaki', 'Kumamoto', 'Oita', 'Miyazaki', 'Kagoshima', 'Okinawa'],
    'population': [5108507, 812393, 1320055, 1747513, 1131140, 1078313, 1605419, 1485670]
}
df = pd.DataFrame(data)

# Dashアプリを作成
app = Dash(__name__)

# レイアウトを定義
app.layout = html.Div([
    html.H1('kyusyu Dash App'),
    dcc.Dropdown(df.category.unique(), 'tops', id='dropdown'),
    dcc.Graph(
        id='bar-chart',
        figure=px.bar(df, x='prefecture', y='population', title='Kyusyu Bar Chart')
    )
])

# コールバックを定義
@callback(
    Output('bar-chart', 'figure'),
    Input('dropdown', 'value')
)
def update_bar_chart(value):
    dff = df[df.category == value]
    return px.bar(dff, x='prefecture', y='population', title='Kyusyu Bar Chart')

if __name__ == '__main__':
    app.run_server(debug=True)
