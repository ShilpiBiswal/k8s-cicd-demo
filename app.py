from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    students = [
        {'name': 'Aarav', 'roll': 101, 'marks': 92, 'grade': 'A'},
        {'name': 'Diya', 'roll': 102, 'marks': 88, 'grade': 'B+'},
        {'name': 'Kabir', 'roll': 103, 'marks': 95, 'grade': 'A+'},
        {'name': 'Ishita', 'roll': 104, 'marks': 79, 'grade': 'B'},
    ]
    return render_template('dashboard.html', students=students)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

