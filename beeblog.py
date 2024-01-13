from flask import Flask, render_template, flash, url_for, redirect
from form import RegForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '0348ab3865cd4ec6bde82c17ecc79c05'

posts = [
    {
        'username': 'Ola23',
        'title': 'My first blog',
        'date': '12 April',
        'content': 'This is my first blog'
    },
    {
        'username': 'Kez23',
        'title': 'My second blog',
        'date': '12 March',
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
        flash(f'Account { form.username.data } Created Succesfully!', 'success')
        return redirect(url_for('home'))
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

if __name__ == '__main__':
    app.run(debug=True)
