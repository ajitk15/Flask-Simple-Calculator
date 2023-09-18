from flask import Flask, render_template, request, jsonify

app = Flask("__name__")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/math", methods=['POST'])
def math():
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if ops == 'add':
            r = num1 + num2
            result = "The sum of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'subtract':
            r = num1 - num2
            result = "The subtract of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'multiply':
            r = num1 * num2
            result = "The multiply of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'divide':
            r = num1 / num2
            result = "The divide of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        
        return render_template('results.html', result=result)



"""
curl --location 'https://lemon-author-lfpbg.pwskills.app:5000/webapimath' \
--header 'Content-Type: application/json' \
--data '{
    "operation":"add",
    "num1":100,
    "num2":20
}'
"""
@app.route("/webapimath", methods=['POST'])
def math_webapi():
    if(request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if ops == 'add':
            r = num1 + num2
            result = "The sum of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'subtract':
            r = num1 - num2
            result = "The subtract of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'multiply':
            r = num1 * num2
            result = "The multiply of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'divide':
            r = num1 / num2
            result = "The divide of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        
        return jsonify(result)


if __name__ == "__main__":
    app.run("0.0.0.0")