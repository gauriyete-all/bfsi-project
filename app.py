import os
import json
from datetime import datetime
from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS
from models import db, User, Income, Expense, Budget, SavingsGoal, FinancialReport
from ai_engine import AIFinancialEngine
from scenarios import load_scenario_data, SCENARIOS_META
app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = 'finflow-secret-personal-finance-advisor-key-2026'
# Configure SQLite Database
db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'finance.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db.init_app(app)
def get_active_user():
    """Returns currently selected user from session or defaults to Salaried Pro."""
    user_id = session.get('active_user_id')
    if user_id:
        user = db.session.get(User, user_id)
        if user:
            return user
    
    # Check if any user exists
    user = User.query.filter_by(scenario_key='salaried').first()
    if not user:
        user = load_scenario_data('salaried')
    session['active_user_id'] = user.id
    return user
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/api/scenarios/list', methods=['GET'])
def list_scenarios():
    return jsonify({
        'status': 'success',
        'scenarios': SCENARIOS_META
    })
@app.route('/api/user/active', methods=['GET'])
def get_user():
    user = get_active_user()
    return jsonify({
        'status': 'success',