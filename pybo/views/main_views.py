from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
bp=Blueprint('main', __name__, url_prefix='/')
from pybo.models import Question
@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return render_template('main/main.html')
@bp.route('/introduce')
def introduce():
    return render_template('introduce.html')
@bp.route('/drink')
def drink():
    return render_template('drink.html')
@bp.route('/dessert')
def dessert():
    return render_template('dessert.html')
@bp.route('question/question_list')
def question():
    return redirect(url_for('question._list'))
@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question=Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)