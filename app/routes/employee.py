from flask import Blueprint, render_template
from app.models.employee import Employee

bp = Blueprint('employees', __name__)


@bp.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return render_template('employees.html', employees=employees)
