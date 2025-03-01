from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(app)

logged_in = None# this might be the user.id or None

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String(50), nullable = False)

with app.app_context(): db.create_all()

@app.route("/")
def index():
    global logged_in

    users = Users.query.all()
    logged_in_user = Users.query.get_or_404(logged_in) if logged_in else None
    return render_template("index.html", users = users, logged_in_user = logged_in_user)

@app.route("/sign-up", methods = ["POST", "GET"])
def sign_up():
    if request.method == "POST":
        username = request.form["username_box"]
        password = request.form["password_box"]
        password_again = request.form["password_again_box"]

        is_username_used = Users.query.filter_by(username = username).first()

        if is_username_used:
            return render_template("sign_up.html", username_exist = True, username = username, password = password, password_again = password_again)

        if password == password_again:
            
            try:
                user = Users(username = username, password = password)
                db.session.add(user)
                db.session.commit()
            except: return "There was an error signing up for you"
            return redirect("/")
        return render_template("sign_up.html", password_password_again = True, username = username, password = password, password_again = password_again)
    else:
        return render_template("sign_up.html")

@app.route("/log-in", methods = ["POST", "GET"])
def log_in():
    global logged_in

    if request.method == "POST":
        username = request.form["username_box"]
        password = request.form["password_box"]
        
        user = Users.query.filter_by(username = username, password = password).first()
        if user:
                
            if username == user.username:
                if password == user.password:
                
                    logged_in = user.id
                    return redirect("/")
                            
        return render_template("log_in.html", wrong_username_password = True, username = username, password = password)
    else:
        return render_template("log_in.html", wrong_username_password = False)

@app.route("/log-out")
def log_out():
    global logged_in
    
    logged_in = None
    return redirect("/")

@app.route("/update/<int:id>", methods = ["POST", "GET"])
def update(id):
    user = Users.query.get_or_404(id)

    if request.method == 'POST':
        username = request.form['updated_username_box']
        password = request.form['updated_password_box']
        password_again = request.form['updated_password_again_box']
        try:
            user.name = username
            user.password = password if password == password_again else user.password
            db.session.commit()
        except:...
        return redirect('/')
    else:
        if logged_in: 
            return render_template('update.html', user = user, password_place_holder = ''.join(['X' for _ in user.password]))
        else:
            return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    global logged_in
    try:
        if logged_in:
            logged_in = None if logged_in == id else logged_in
            user = Users.query.get_or_404(id)
            db.session.delete(user)
            db.session.commit()
            return redirect('/')
        else:
            return redirect('/')
    except:
        return redirect("/")

app.run(debug = True)

