from flask import Flask, render_template, url_for, redirect, request
import csv
app = Flask(__name__)
print(__name__)

def write_to_csv(data):
    with open('DB.csv', mode = 'a') as DB:
     email = data["email"]
     subject = data["subject"]
     message= data["message"]
     cFile = csv.writer(DB,delimiter = ',', quotechar = ' ', quoting = csv.QUOTE_MINIMAL)
     cFile.writerow([email,subject,message])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
 error = None
 if request.method == 'POST':
    response= request.form.to_dict()
    write_to_csv(response)
    return redirect('/thankyou.html')
# the code below is executed if the request method
# was GET or the credentials were invalid
 
 else:
    return 'Something went wrong. Try again!'