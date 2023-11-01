from flask import Flask, render_template
import datetime
import requests

GENDER_API = "https://api.genderize.io"
AGE_API = "https://api.agify.io"
NATIONALITY_API = "https://api.nationalize.io"

app = Flask(__name__)
year = datetime.datetime.now().year

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/<string:name>")
def predictor(name):
    gender_res = requests.get(GENDER_API, params={"name": name}).json()
    age_res = requests.get(AGE_API, params={"name": name}).json()
    nat_res = requests.get(NATIONALITY_API, params={"name": name}).json()["country"]
    return render_template("index.html", year=year, name=name,
                           gender=gender_res["gender"], gender_prob=gender_res["probability"]*100,
                           age=age_res["age"], nat_list=nat_res)


if __name__ == "__main__":
    app.run(debug=True)
