# app/home/views.py

from flask import render_template
from flask_login import login_required

from . import dashboard

@dashboard.route('/')
@login_required
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('dashboard/dashboard2.html', title="Welcome")

#
