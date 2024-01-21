from flask import render_template, flash, url_for, redirect
from beeblog import app, db, bcrypt
from beeblog.form import RegForm, LoginForm
from beeblog.models import User, Post

    

posts = [
    {
        'username': 'Ola23',
        'title': 'My first blog',
        'date_created': '12 April',
        'content': 'This is my first blog'
    },
    {
        'username': 'Kez23',
        'title': 'My second blog',
        'date_created': '12 March',
        'content': 'This is my second blog'
    },
    {
        'username': 'Remi04 ',
        'title': 'My third blog',
        'date': '16 August',
        'content': 'This is my third blog'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account Created Succesfully!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login not successful', 'danger')
            # return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)