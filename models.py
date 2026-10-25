from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
def utcnow_clean():
    return datetime.now(timezone.utc)
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    scenario_key = db.Column(db.String(50), default='custom') # salaried, student, freelancer, household, custom
    persona_title = db.Column(db.String(150), default='Personal Account')
    currency = db.Column(db.String(10), default='$')
    monthly_target_savings = db.Column(db.Float, default=500.0)
    created_at = db.Column(db.DateTime, default=utcnow_clean)
    # Relationships
    incomes = db.relationship('Income', backref='user', cascade='all, delete-orphan', lazy=True)
    expenses = db.relationship('Expense', backref='user', cascade='all, delete-orphan', lazy=True)
    budgets = db.relationship('Budget', backref='user', cascade='all, delete-orphan', lazy=True)
    savings_goals = db.relationship('SavingsGoal', backref='user', cascade='all, delete-orphan', lazy=True)
    reports = db.relationship('FinancialReport', backref='user', cascade='all, delete-orphan', lazy=True)
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'scenario_key': self.scenario_key,
            'persona_title': self.persona_title,
            'currency': self.currency,
            'monthly_target_savings': self.monthly_target_savings,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S') if self.created_at else None
        }
class Income(db.Model):
    __tablename__ = 'incomes'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    source = db.Column(db.String(150), nullable=False) # e.g. "Acme Corp Tech", "Client Alpha Design", "Family Contribution"
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), default='Salary') # Salary, Freelance, Allowance, Investment, Bonus, Other
    frequency = db.Column(db.String(50), default='Monthly') # Monthly, Bi-Weekly, Milestone, One-Time