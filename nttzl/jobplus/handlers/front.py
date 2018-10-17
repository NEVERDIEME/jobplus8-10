from flask import Blueprint,render_template,url_for,redirect,flash
from jobplus.forms import RegisterForm,LoginForm
from jobplus.models import User,db,Job

front = Blueprint('front',__name__)

@front.route('/')
def index():
    return render_template('index.html')

@front.route('/login')
def login():
    return render_template('login.html')

@front.route('/companyregister',methods=['GET','POST'])
def companyregister():
    form = RegisterForm()
    form.name.label = 'CompanyName'
    if form.validate_on_submit():
        company_user = form.create_user()
        company_user.role = User.ROLE_COMPANY
        db.session.add(company_user)
        db.session.commit()
        flash('register success','sucess')
        return redirect(url_for('.login'))
    return render_template('companyregister.html',form=form)

@front.route('/userregister',methods=['GET','POST'])
def userregister():
    form = RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('register success','success')
        return redirect(url_for('.login'))
    return render_template('userregister.html',form=form)
