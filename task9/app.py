from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    student = {
        "name": "Иван",
        "group": "ИС-21",
        "age": 19
    }

    subjects = [
        "Python",
        "Веб-программирование",
        "Базы данных",
        "Алгоритмы"
    ]

    return render_template(
        "index.html",
        student=student,
        subjects=subjects
    )


if __name__ == "__main__":
    app.run(debug=True)