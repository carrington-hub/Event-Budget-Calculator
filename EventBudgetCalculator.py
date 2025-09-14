#!/usr/bin/env python3
"""
carrington_assignment5.py
Author: Carrington Davis
Simple Event Budget Calculator - step 2
This file adds catering and decoration cost functions.
"""

import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def venue_rental_cost(rental_rate, days):
    """Calculate total venue cost."""
    return rental_rate * days


# NEW FUNCTION: catering cost
def catering_cost(cost_per_person, number_of_attendees):
    """
    Calculate catering cost.
    cost_per_person: dollars per person
    number_of_attendees: how many people will attend
    returns: total catering cost
    """
    return cost_per_person * number_of_attendees


# NEW FUNCTION: decoration cost
def decoration_cost(cost_per_table, number_of_attendees, seats_per_table=6):
    """
    Calculate decoration cost.
    cost_per_table: cost to decorate one table
    number_of_attendees: total guests
    seats_per_table: how many seats per table (default = 6)

    Uses ceiling division to make sure we don't undercount tables.
    Example: 13 attendees / 6 per table = 2.17 → needs 3 tables.
    """
    number_of_tables = (number_of_attendees + seats_per_table - 1) // seats_per_table
    total_cost = cost_per_table * number_of_tables
    return total_cost, number_of_tables


# quick test block
if __name__ == "__main__":
    # Venue test
    venue_total = venue_rental_cost(200, 3)
    logger.info("Venue total: %s", venue_total)

    # Catering test
    catering_total = catering_cost(20, 120)
    logger.info("Catering total (120 attendees): %s", catering_total)

    # Decoration test
    decoration_total, tables = decoration_cost(15, 120)
    logger.info("Decoration total: %s (tables: %s)", decoration_total, tables)

    print("---- Quick Test Results ----")
    print("Venue:", venue_total)
    print("Catering:", catering_total)
    print("Decorations:", decoration_total, f"({tables} tables)")

# Budget Calculator - Improved Version
# Author: Carrington Davis

def get_income():
    while True:
        try:
            income = float(input("Enter your monthly income: $"))
            if income < 0:
                print("Income cannot be negative. Please try again.")
                continue
            return income
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_expenses():
    expenses = {}
    while True:
        name = input("Enter expense name (or 'done' to finish): ").strip()
        if name.lower() == "done":
            break
        try:
            amount = float(input(f"Enter cost for {name}: $"))
            if amount < 0:
                print("Expense cannot be negative. Try again.")
                continue
            expenses[name] = amount
        except ValueError:
            print("Invalid input. Please enter a number.")
    return expenses

def calculate_balance(income, expenses):
    total_expenses = sum(expenses.values())
    balance = income - total_expenses
    return total_expenses, balance

def display_summary(income, expenses, total_expenses, balance):
    print("\n--- Budget Summary ---")
    print(f"Monthly Income: ${income:.2f}")
    print("Expenses:")
    for name, cost in expenses.items():
        print(f"  - {name}: ${cost:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Balance: ${balance:.2f}")

def main():
    print("Welcome to the Budget Calculator!")
    income = get_income()
    expenses = get_expenses()
    total_expenses, balance = calculate_balance(income, expenses)
    display_summary(income, expenses, total_expenses, balance)

if __name__ == "__main__":
    main()
