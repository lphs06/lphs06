#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def index():
    return 'sitemap'

@app.route('/about')
def about():
    return 'event details'

@app.route('/login', methods=['GET', 'POST'])
def login(user):
    if request.method == 'POST':
        authenticate(user)
    else:
        show_the_login_form():
@app.route('/register', methods=['GET' 'POST'])
def register():
    def submit():
        if request,method == 'POST' and form.validates():
            add_update_db(user)
        else:
            register()

@app.route('/contact')
def contact():
    return 'contact page'

if __name__ == '__main__':
    app.run()

#class User(object):
#    def __init__(self):
#        self.name = self

def add_update_db(user):
    return 'db updates'

def set_cookie():
    return 'a cookie has been set'

def authenticate(user):
    return 'authenticate function'
