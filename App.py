from os import name
from flask import Flask,render_template

color_green="success"
color_blue="primary"
color_gray="secondary"
color_yellow="warning"
color_red="danger"
color_white="light"


app=Flask(__name__)



@app.route("/")
def main():

    return render_template("index.html",nav_bar_color=color_green)

@app.route("/automation")
def automation():

    return render_template("automation.html",nav_bar_color=color_yellow)


@app.route("/python")
def python():

    return render_template("python.html",nav_bar_color=color_blue)


if __name__ == "__main__":

    app.run(debug=False,host="0.0.0.0",port="8000")