from flask import Flask,render_template,request,redirect,session,url_for
from datetime import timedelta
app=Flask(__name__)
app.secret_key="helloworld"
app.permanent_session_lifetime=timedelta(minutes=2)


@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        session.permanent=True
        username=request.form['username']
        session['username']=username
        return redirect(url_for("user"))
    else:
        if "username" in session:
            return redirect(url_for("user"))
        
        return render_template("login.html")



@app.route("/login",methods=["GET","POST"])
def login():
    return render_template("login.html")


@app.route("/user",methods=["GET","POST"])
def user():
    if 'username' in session:
        username=session["username"]
        return render_template("session.html",username=username)

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username",None)
    return redirect(url_for("login"))
if __name__ == "__main__":
    app.run(debug=True)
