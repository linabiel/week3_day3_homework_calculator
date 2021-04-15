from flask import render_template
from app import app
from modules.calculator import Calculator

@app.route('/calculator/add/<num1>/<num2>')
def add(num1, num2):
    calculator = Calculator()
    return render_template('calculator.html', result=calculator.add(num1, num2))

@app.route('/calculator/divide/<num1>/<num2>')
def devide(num1, num2):
    calculator = Calculator()
    return render_template('calculator.html', result=calculator.divide(num1, num2))

@app.route('/calculator/multiply/<num1>/<num2>')
def multiply(num1, num2):
    calculator = Calculator()
    return render_template('calculator.html', result=calculator.multiply(num1, num2))

@app.route('/calculator/subtract/<num1>/<num2>')
def subtract(num1, num2):
    calculator = Calculator()
    return render_template('calculator.html', result=calculator.subtract(num1, num2))


