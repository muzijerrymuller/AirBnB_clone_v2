from flask import Flask, render_template

app = Flask(__name__)

@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    # Determine if the number is odd or even
    if n % 2 == 0:
        result = "even"
    else:
        result = "odd"

    # Render the result using a template
    return render_template('number_odd_or_even.html', number=n, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
