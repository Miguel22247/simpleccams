from flask import request, redirect, url_for
from flask import render_template

from app import app
from app.squawkgen import parse_whazzup, download_whazzup, assign_squawk, assigned_squawk

@app.route('/', methods=['GET','POST'])
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
