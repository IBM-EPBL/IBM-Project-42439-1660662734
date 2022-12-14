from flask import Flask, render_template , request , redirect
app = Flask(__name__)

users = [
   {"name":"Arun","email":"jadduarun29@gmail.com","password":"arun2002"}
]

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/about")
def about():
   return render_template("about.html")

@app.route("/signin" ,methods = ['POST', 'GET'])
def signin():
   if request.method == 'POST':
      user_email = request.form['email']
      user_password = request.form['password']
      for user in users:
         if user["email"] == user_email:
            if user["password"] == user_password:
               return redirect("/home")
               
   
   return render_template("signin.html")

@app.route("/signup" ,methods = ['POST', 'GET'])
def signup():
   if request.method == 'POST':
      user_name = request.form['name']
      user_email = request.form['email']
      user_password = request.form['password']
      users.append({"name":user_name , "email":user_email , "password":user_password})
      return redirect("/home")

   return render_template("signup.html")

@app.route("/home")
def home():
   return render_template("home.html")

@app.route("/users")
def user():
   return users

if __name__ == '__main__':
   app.run(debug = True)
