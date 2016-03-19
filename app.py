from flask import Flask, render_template, request, redirect, Quandl

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/graph', methods=['POST'])
def graph():
    symbol = request.form['ticker']

    return render_template('graph.html',ticker=symbol)

if __name__ == "__main__":
    app.run(debug=True)
