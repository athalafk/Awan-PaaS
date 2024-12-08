from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Halaman utama dengan form HTML
@app.route('/')
def home():
    return render_template('index.html')

# API untuk operasi kalkulasi
@app.route('/calculate', methods=['POST'])
def calculate():
    operation = request.form.get('operation')
    a = float(request.form.get('a', 0))
    b = float(request.form.get('b', 0))

    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        if b == 0:
            return jsonify(error="Cannot divide by zero"), 400
        result = a / b
    else:
        return jsonify(error="Invalid operation"), 400

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
