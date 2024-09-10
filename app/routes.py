from flask import Blueprint, render_template, flash, redirect, url_for
from .forms import EmailForm
from .models import Email
from . import db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    form = EmailForm()
    if form.validate_on_submit():
        email = form.email.data
        # メールアドレスがすでに存在しないか確認
        existing_email = Email.query.filter_by(email=email).first()
        if existing_email is None:
            new_email = Email(email=email)
            db.session.add(new_email)
            db.session.commit()
            flash('登録が完了しました！', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('このメールアドレスは既に登録されています。', 'danger')
    return render_template('home.html', form=form)