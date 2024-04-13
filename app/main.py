from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def survey_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def survey_result():
    q1 = int(request.form['q1'])
    q2 = int(request.form['q2'])
    q3 = int(request.form['q3'])
    score = q1 + q2 + q3
    message = "You're in tune with spiritual matters, or emotions and love"
    if score > 6:
        message = "You dislike reason or logic, wisdom, and intellect!"
    elif score > 3:
        message = "You lack conviction you spineless ninny"
    return render_template('index.html', score=score, message=message)

if __name__ == '__main__':
    app.run(debug=True)
