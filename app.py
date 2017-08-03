from flask import Flask, request, redirect, url_for
from flask import render_template
from squawkgen import *

app = Flask(__name__)

@app.route('/index.html', methods=['GET','POST'])
def index():
    online = parse_whazzup(download_whazzup())
    if request.method == 'POST':
        user_input = request.form['callsign'].upper()
        assign_squawk(user_input)
        return redirect(url_for('index'))
    return render_template('index.html',
                           assigned_squawk=assigned_squawk,
                           online=online)

if __name__ == '__main__':
    app.run()
