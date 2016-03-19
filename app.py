from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure
from bokeh.embed import components 
import Quandl, requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph', methods=['POST'])
def graph():
    symbol = request.form['ticker']
    print("Symbol %s" % symbol)
    api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/%s.json' % symbol
    session = requests.Session()
    session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
    raw_data = session.get(api_url)
    TOOLS = 'box_zoom,box_select,resize,reset,hover,wheel_zoom'
    plot = figure(tools=TOOLS, title='Data from Quandle WIKI set', x_axis_label='date', x_axis_type='datetime')
    script, div = components(plot)
    return render_template('graph.html', script=script, div=div, ticker=symbol)

if __name__ == "__main__":
    app.run(port=33507)
#    app.run(host='0.0.0.0', debug=True)
