from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/departments')
def departments():
    return render_template('departments.html')


@app.route('/employees')
def employees():
    return render_template('employees.html')


if __name__ == '__main__':
    app.run(debug=True)

