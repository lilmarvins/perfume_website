import requests,random,string,os,json
from functools import wraps
from flask import render_template,request,session,redirect,flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_mail import Mail,Message


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