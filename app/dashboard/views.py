# app/home/views.py

from flask import abort, render_template
from flask_login import current_user, login_required

from . import dashboard

@dashboard.route('/')
@login_required
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('dashboard/dashboard2.html', title="Welcome")

# Hande the Admin Dashboard for the admin users
@dashboard.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

    return render_template('dashboard/admin_dashboard.html', title="Dashboard")