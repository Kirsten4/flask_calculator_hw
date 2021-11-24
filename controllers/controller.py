from flask import render_template
from app import app
from modules.inputs import calculator


@app.route('/')
def index():
    return render_template('index.html',title='Calculator',calculator=calculator)

@app.route('/add/<num1>/<num2>')
def add_num(num1,num2):
    num1 = int(num1)
    num2 = int(num2)
    result = calculator.add()
    return render_template('result.html',title='Result', result=result)

@app.route('/subtract/<num1>/<num2>')
def subtract_num(num1,num2):
    num1 = int(num1)
    num2 = int(num2)
    result = calculator.subtract()
    return render_template('result.html',title='Result', result=result)

@app.route('/multiply/<num1>/<num2>')
def multiply_num(num1,num2):
    num1 = int(num1)
    num2 = int(num2)
    result = calculator.multiply()
    return render_template('result.html',title='Result', result=result)

@app.route('/divide/<num1>/<num2>')
def divide_num(num1,num2):
    num1 = int(num1)
    num2 = int(num2)
    result = calculator.divide()
    return render_template('result.html',title='Result', result=result)