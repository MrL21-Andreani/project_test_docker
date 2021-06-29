from flask import Flask

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8080)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
