from flask import Flask, render_template, request
from compute import calculate

app = Flask(__name__)

class Question:
    q_id = -1
    question = ""
    yes = ""
    no = ""
    qtype = ""
    oneOption = -1

    def __init__(self, q_id, question, yes, no, oneOption, qtype):
        self.q_id = q_id
        self.question = question
        self.yes = yes
        self.no = no
        self.oneOption = oneOption
        self.qtype = qtype

    def pertains(self):
        if self.oneOption == 1:
            return self.yes
        elif self.oneOption == 2:
            return self.no

q1 = Question(1, "Do you like to read?", "yes", "no", 1, 'a')
q2 = Question(2, "Do you like to run?", "yes", "no", 1, 'f')
q3 = Question(3, "Do you consider yourself a considerate person?", "yes", "no", 1, 'b')
q4 = Question(4, "Do you like children", "yes", "no", 1, 'd')
q5 = Question(5, "Do you think you are a hard working person?", "yes", "no", 1, 'j')
q6 = Question(6, "Do you care about the environment?", "yes", "no", 1, 'i')
q7 = Question(7, "Do you consider yourself artistic", "yes", "no", 1, 'e')
q8 = Question(8, "Do you like taking photos?", "yes", "no", 1, 'h')
q9 = Question(9, "Do you like to study", "yes", "no", 1, 'g')

questions_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9]
r_value = ''

@app.route('/index')
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/quiz", methods = ['GET', 'POST'])
def quiz():
    return render_template("quiz.html", questions_list = questions_list)

# @app.route("/submitquiz", methods=['POST', 'GET'])
@app.route("/submitquiz", methods=['POST', 'GET'])
def submit():
    points = {}
    types = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for i in types:
        points[i] = 0

    for question in questions_list:
        question_id = str(question.q_id)
        question_type = str(question.qtype)
        selected = request.form[question_id]
        count = question.pertains()
        if selected == count:
            points[question_type] = 1
    use = ""
    for k, t in points.items():
        use += str(t)
    return render_template("submitquiz.html", r_value = calculate(use))

    # value = request.form['option']
    # return (value)

if __name__ == "__main__":
    app.run(debug=True)