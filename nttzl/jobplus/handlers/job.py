from flask import Blueprint,request,current_app,render_template
from jobplus.models import Job

job = Blueprint('job',__name__, url_prefix='/job')

@job.route('/')
def index():
    page = request.args.get('page',1,type=int)
    pagination = Job.query.order_by(Job.created_ad.desc()).paginate{
        page = page,
        per_page = current_app.config[INDEX_PER_PAGE],
        error_out = False
        }
    return render_template('job/index.html',pagination=pagination,active='job')

