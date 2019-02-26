from flask import render_template,request,redirect,url_for, abort
from . import main

from .forms import UpdateProfile,CommentForm,AddPitchForm
from .. import db,photos
from ..models import Comment,Pitch,User
from flask_login import login_required, current_user
# import markdown2 

@main.route('/', methods = ['GET', 'POST'])
def index():
  title="Kweriiii"
  all_pitches = Pitch.get_pitches()
  
  return render_template('index.html',title=title, pitches = all_pitches)

@main.route('/home', methods = ['GET', 'POST'])
@login_required
def home():
    form = AddPitchForm()
    
    if form.validate_on_submit():
        category = form.category.data

        pitch = form.content.data

        new_pitch = Pitch(content=pitch, category = category)
        new_pitch.save_pitch()

        return redirect(url_for('main.home'))

    all_pitches = Pitch.get_pitches()

    title = 'cause'    
    return render_template('pitches.html', title = title, pitch_form = form, pitches = all_pitches)

