import requests,random,string,os,json
from functools import wraps
from flask import render_template,request,session,redirect,flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_mail import Mail,Message
from pkg.models import db, User



from pkg import app


@app.route('/admin_dashboard/')
def admin_dashboard():
    return render_template('admin/admindashboard.html',title='admin_dashboard')
