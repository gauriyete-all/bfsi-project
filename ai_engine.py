import os
import json
from datetime import datetime
class AIFinancialEngine:
    """
    AI Financial Planning & Advisor Engine.
    Provides intelligent financial health scoring, adaptive budget generation,
    overspending anomaly detection, and interactive conversational guidance.
    """
    @staticmethod
    def calculate_health_score(incomes, expenses, budgets, savings_goals):
        """
        Calculates a financial health score from 0 to 100 based on 4 pillars:
        1. Savings Rate (0-30 pts)
        2. Budget Adherence (0-30 pts)
        3. Essential vs Discretionary Balance (0-20 pts)
        4. Emergency Reserve / Goal Momentum (0-20 pts)
        """
        total_income = sum(i.amount for i in incomes)
        total_expense = sum(e.amount for e in expenses)
        
        if total_income <= 0:
            return {
                'score': 50,
                'rating': 'Neutral',
                'color': '#94A3B8',
                'breakdown': {'savings_rate': 10, 'budget_adherence': 15, 'essential_balance': 15, 'goals': 10},
                'summary': 'Add your monthly income sources to calculate your personalized financial health score.'
            }
        # 1. Savings Rate Score (0 - 30)
        net_savings = max(0, total_income - total_expense)
        savings_rate = (net_savings / total_income) * 100
        if savings_rate >= 25:
            score_savings = 30
        elif savings_rate >= 20:
            score_savings = 26
        elif savings_rate >= 15:
            score_savings = 21
        elif savings_rate >= 10:
            score_savings = 16
        elif savings_rate >= 5:
            score_savings = 10
        else:
            score_savings = 4
        # 2. Budget Adherence Score (0 - 30)
        # Sum expenses by category
        cat_spending = {}