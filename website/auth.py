from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return render_template('logout.html')


@auth.route('/sign_up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.form
        print(data)
    return render_template('sign_up.html')