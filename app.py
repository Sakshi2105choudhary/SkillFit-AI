from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('page.html')   

@app.route('/selfie', methods=['POST'])
def selfie():
    name = request.form['name']
    role = request.form['role']
    language = request.form['language']

    return render_template('selfie.html', name=name, role=role, language=language)

@app.route('/interview', methods=['POST'])
def interview():
    name = request.form['name']
    role = request.form['role']
    language = request.form['language']

    questions = {
        "English": "What safety precautions do you follow while working?",
        "Hindi": "आप काम करते समय कौन-कौन सी सुरक्षा सावधानियाँ रखते हैं?",
        "Kannada": "ನೀವು ಕೆಲಸ ಮಾಡುವಾಗ ಯಾವ ಸುರಕ್ಷತಾ ಕ್ರಮಗಳನ್ನು ಅನುಸರಿಸುತ್ತೀರಿ?"
    }

    question = questions.get(language, questions["English"])

    return render_template('interview.html', question=question, name=name, role=role)

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    role = request.form['role']
    answer = request.form['answer']

    if "safety" in answer.lower():
        result = "Job Ready"
    else:
        result = "Needs Training"

    return render_template('result.html', name=name, role=role, answer=answer, result=result)

if __name__ == '__main__':
    app.run(debug=True)