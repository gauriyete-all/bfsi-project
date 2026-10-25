from datetime import datetime
from models import db, User, Income, Expense, Budget, SavingsGoal, FinancialReport
from ai_engine import AIFinancialEngine
import json
SCENARIOS_META = {
    'salaried': {
        'name': 'Alex Vance',
        'email': 'alex.vance@finflow.io',
        'title': 'Senior Software Engineer (Salaried Professional)',
        'currency': '$',
        'target_savings': 1200.0,
        'description': 'Stable monthly income from corporate tech. Overspends on high-end dining and entertainment. Needs 50/30/20 structure and disciplined saving trajectory.'
    },
    'student': {
        'name': 'Maya Lin',
        'email': 'maya.lin@campus.edu',
        'title': 'Undergraduate Student (Allowance & Part-Time)',
        'currency': '$',
        'target_savings': 150.0,
        'description': 'Constrained $850/mo allowance + campus tutoring. Balances meal plans, textbooks, and social outings. Needs micro-savings and strict discretionary caps.'
    },
    'freelancer': {
        'name': 'Leo Ortiz',
        'email': 'leo.ortiz@designcraft.studio',
        'title': 'Independent Product Designer (Variable Income)',
        'currency': '$',
        'target_savings': 1500.0,
        'description': 'Variable monthly income across 3-4 active enterprise clients ($3,200 – $6,800). Manages project tool expenses, quarterly tax reserves, and a 6-month emergency buffer.'
    },
    'household': {
        'name': 'Elena & David Foster',
        'email': 'foster.family@homeportal.net',
        'title': 'Dual-Income Household Managers (Family of 4)',
        'currency': '$',
        'target_savings': 1800.0,
        'description': 'Shared family income of $8,400 across two salaried roles. Coordinates large groceries, utilities, children education, and healthcare. Needs unified monthly reports.'
    }
}
def load_scenario_data(scenario_key):
    """
    Clears current active user or retrieves/creates the user for the chosen scenario,
    then populates rich, realistic incomes, expenses, budgets, goals, and monthly report.
    """
    if scenario_key not in SCENARIOS_META:
        scenario_key = 'salaried'
