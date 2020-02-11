from flask import render_template, flash, redirect
from app import app
from app.forms import ContactMeForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Imran'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Web App Home', user=user, posts=posts)
@app.route('/home')
def home():
    return render_template('index.html')
@app.route('/about')
def about(): 
    return render_template('about.html')
@app.route('/contactme', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def contactme():
    form = ContactMeForm()
    if form.validate_on_submit():
        flash('Thanks for sending a message, I will reply as soon as possible.')
        print('This worked I think')
        #flash('Thanks for sending your message firstname={} lastname={}, I appreciate you reaching out'.format(form.firstname.data, form.lastname.data))
        return redirect('/index')
    return render_template("contactme.html", title='Contact Me', form=form)
    

