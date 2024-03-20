import requests
from flask import Flask,render_template,url_for
from flask import request as req


App = Flask(__name__)
@App.route("/",methods=["GET","POST"])
def Index():
    return render_template("index.html")

@App.route("/Summarize",methods=["GET","POST"])
def Summarize():
    if req.method== "POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": f"Bearer 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"}

        data=req.form["data"]

        maxL=int(req.form["maxL"])
        minL=maxL//4
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs":data,
            "parameters":{"min_length":minL,"max_length":maxL},
        })[0]
        
        return render_template("index.html",result=output["summary_text"])
    else:
        return render_template("index.html")
if __name__ == "__main__":
    App.run(debug=True)