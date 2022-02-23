from flask import Flask
app = Flask(__name__)


def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__}{args}")
        result = function(args[0], args[1], args[2])
        print(f"It returned: {result}")
    return wrapper


@app.route("/")
@logging_decorator
def a_function(a, b, c):
    return a * b * c


if __name__ == "__main__":
    app.run(debug=True, port=9874)

a_function(1, 2, 3)
