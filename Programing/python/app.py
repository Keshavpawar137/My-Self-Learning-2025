
# Flask App Routing Example

from flask import Flask,render_template,request,redirect,url_for,jsonify

## Creating a simple Flask Application
app = Flask(__name__)

#create a routing function
@app.route("/",methods=["GET"])
def Welcome():
    return "<h1>Welcome to Flask</h1>"

@app.route("/index",methods=["GET"])
def index():
    return "<h2>Welcome to index Page</h2>"

#Variable rule 

@app.route("/success/<int:score>")
def success(score):
    return  "The Persion is pass and the score is "+str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return  "The Persion is fail and the score is "+str(score)

@app.route("/form",methods=["GET","POST"])
def form():
   if request.method =="GET":
      return render_template("form.html")
   else:
       maths= float(request.form['maths'])
       science =float(request.form['science'])
       history = float(request.form['history'])
       total= maths+science+history
       average_marks = total/3

       if average_marks>=50:
           res="success"
       else:
           res="fail"

       return redirect(url_for(res,score=average_marks))
           

    #  return render_template("form.html",score=average_marks)

@app.route("/api",methods=["post"])
def calculate_data():
    data= request.get_json()
    a_val=float(data["a"])
    b_val=float(data["b"])
    return jsonify(a_val+b_val)

   
if __name__=="__main__":
    app.run(debug=True)
