from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')

        if not email or len(email) < 3:
            flash('Email must be greater than 3 characters', category='error')
        elif not password or len(password) < 4:
            flash('Password must be greater than 4 characters', category='error')
        else:
            flash('Login successfully!', category='success')
        print(password, email)
        
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return render_template('logout.html')


@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        data = request.form
        name = data.get('firstName')
        email = data.get('email')
        password1 = data.get('password1')
        password2 = data.get('password2')

        if not name or len(name) <= 2:
            flash("Name must be greater than 2 characters", category='error')
        elif not email or len(email) < 3:
            flash('Email must be greater than 3 characters', category='error')
        elif not password1 or len(password1) < 4:
            flash('Password must be greater than 4 characters', category='error')
        elif not password2 or len(password2) < 4:
            flash('Password must be greater than 4 characters', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        else:
            flash('Account successfully created!', category='success')
            # Perform additional actions such as saving the user to the database
            # return redirect(url_for('home'))
        print("Name from form:", name)


    return render_template('sign_up.html')
