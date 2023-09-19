#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:string_param>')
def print_string(string_param):
    print(string_param)
    return f"Printed: {string_param}"

@app.route('/count/<int:int_param>')
def count(int_param):
    numbers = '\n'.join(str(i) for i in range(int_param + 1))
    return f"Counting from 0 to {int_param}:\n{numbers}"

@app.route('/math/<int:num1><operation><int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Division by zero is not allowed."
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation. Supported operations: +, -, *, div, %"
    
    return f"{num1} {operation} {num2} = {result}"

if __name__ == '__main__':
    app.run(debug=True)
