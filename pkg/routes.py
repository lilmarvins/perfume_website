import requests,random,string,os,json
from functools import wraps
from flask import render_template,request,session,redirect,flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_mail import Mail,Message
from pkg.models import db, User



from pkg import app

@app.route("/")
def home():
    return render_template("user/dashboard.html" ,title='home')


@app.route('/proddeets/')
def proddeets():
    return render_template("user/proddeets.html",title='Product Details')


@app.route('/store/')
def store():
    return render_template("user/store.html",title='Store')


@app.route('/cart/')
def cart():
    return render_template("user/cart.html",title='cart')


@app.route('/account/')
def account():
    return render_template("user/account.html",title='My Account')

@app.route('/login/', methods=['GET','POST'])
def login():
   if request.method == 'GET':
        return render_template('user/login.html', title="Login")
   else:
        email = request.form.get('email')
        pwd = request.form.get('password')
        if email == '' or pwd =='':
            flash('Both fields must be supplied', category='error')
            return redirect("/login/")
        else:
            user = db.session.query(User).filter(User.email==email).first()
            if user != None :
                stored_hash= user.password
                chk = check_password_hash(stored_hash,pwd)
                if chk == True:
                    
                    session['useronline'] = user.user_id
                    session['role']= user.role

                    if user.role =='Admin':
                        flash('welcome Admin', 'success')
                        return redirect('/')
                    else:
                        flash('welcome to the website', 'success')
                        return redirect('/')
                else:
                    flash('invalid password',category= 'error' )
            else:
                    flash('invalid email', category= 'error')
            return redirect("/login/")
        


@app.route('/signup/', methods=['GET','POST'])
def signup():
  if request.method == 'GET':
        return render_template('user/signup.html',title='Sign up')
  else:
        name= request.form.get('fullname')
        email= request.form.get("email")
        password= request.form.get('password')
        hashed = generate_password_hash(password)
        existing_user = db.session.query(User).filter(User.email==email).first()
        if existing_user != None:
            flash('user already exist please login', category='error')
            return redirect('/login/')
        else:
            user = User(username=name,email=email,password=hashed,role="Customer")
            db.session.add(user)
            db.session.commit()
            userid= user.user_id
            session['useronline']= userid
            return redirect("/")
           