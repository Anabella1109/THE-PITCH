from flask import render_template, redirect, url_for, flash, request
from . import auth
from ..models import User
from .. import db
from flask_login import login_user
from .forms import LoginForm,RegistrationForm
from flask_login import login_user,logout_user,login_required
# from ..email import mail_message