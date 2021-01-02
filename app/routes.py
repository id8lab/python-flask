from app import app
###############################################
#          Import some packages               #
###############################################
from flask import Flask, render_template, request
from forms import ContactForm
from forms import NewsLetterForm
import pandas as pd

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Michael'}
    return render_template('index.html', title='Home', user=user)

###############################################
#       Render Contact page                   #
###############################################
@app.route('/contactus', methods=["GET","POST"])
def get_contact():
    form = ContactForm()
    if request.method == 'POST':
        name =  request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        res = pd.DataFrame({'name':name, 'email':email, 'subject':subject ,'message':message}, index=[0])
        res.to_csv('./contactusMessage.csv')
        return render_template('contact.html', form=form)
    else:
        return render_template('contact.html', form=form)

###############################################
#       Render News letter page               #
###############################################
@app.route('/newsletter', methods=["GET","POST"])
def get_newsletter():
    form = NewsLetterForm()
    if request.method == 'POST':
        name =  request.form["name"]
        email = request.form["email"]
        res = pd.DataFrame({'name':name, 'email':email}, index=[0])
        res.to_csv('./newsletter.csv')
        return render_template('newsletter.html', form=form)
    else:
        return render_template('newsletter.html', form=form)