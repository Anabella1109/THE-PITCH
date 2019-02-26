from flask import render_template,request,redirect,url_for, abort
from . import main

from .forms import UpdateProfile,CommentForm,AddPitchForm
from .. import db,photos
from ..models import Comment,Pitch,User
from flask_login import login_required, current_user
# import markdown2 

@main.route('/')
def index():
  title="Kweriiii"
  return render_template('index.html',title=title)

@main.route('/home', methods = ['GET', 'POST'])
@login_required
def home():
    form = AddPitchForm()
    
    if form.validate_on_submit():
        category = form.my_category.data

        pitch = form.pitch.data

        new_pitch = Pitch(pitch_content=pitch, pitch_category = category, user = current_user)
        new_pitch.save_pitch()

        return redirect(url_for('main.home'))

    all_pitches = Pitch.get_pitches()

    title = 'cause'    
    return render_template('pitches.html', title = title, pitch_form = form, pitches = all_pitches)

