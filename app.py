from flask import Flask, render_template, request, redirect
from db import insert_round, get_rounds

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        course_id = int(request.form['course_id'])
        date = request.form['date']
        score = int(request.form['score'])
        insert_round(course_id, date, score)
        return redirect('/')
    
    rounds = get_rounds()
    return render_template("index.html", rounds=rounds)

if __name__ == '__main__':
    app.run(debug=True)
