import os
import sys
import re

transactions = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    print("=" * 40)
    print("      🐍 PURE PYTHON FINANCE APP 🐍      ")
    print("=" * 40)
    print(" 1. Log a New Expense")
    print(" 2. Log a New Income")
    print(" 3. View Statement & Financial Dashboard")
    print(" 4. Use Financial Calculator")
    print(" 5. Exit Application")
    print("=" * 40)

def add_transaction(is_expense=True):
    clear_screen()
    title = "EXPENSE" if is_expense else "INCOME"
    print(f"--- LOG NEW {title} ---")
    
    item = input("Enter description/name: ").strip()
    if not item:
        print("❌ Description cannot be blank.")
        input("\nPress Enter to return...")
        return

    try:
        amount = float(input("Enter amount ($): "))
        if amount <= 0:
            print("❌ Amount must be greater than zero.")
            input("\nPress Enter to return...")
            return
    except ValueError:
        print("❌ Invalid number format.")
        input("\nPress Enter to return...")
        return

    category = input("Enter category (e.g., Food, Salary, Rent): ").strip()
    
    transactions.append({
        "type": "Expense" if is_expense else "Income",
        "item": item,
        "amount": amount,
        "category": category if category else "General"
    })
    print(f"\n✅ {title} successfully registered!")
    input("\nPress Enter to return to main menu...")

def view_dashboard():
    clear_screen()
    print("--- FINANCIAL DASHBOARD & STATEMENT ---")
    if not transactions:
        print("\n[ No transaction logs found. Your balance is $0.00 ]")
        input("\nPress Enter to return...")
        return

    total_income = 0.0
    total_expense = 0.0

    print(f"{'TYPE':<10} | {'DESCRIPTION':<15} | {'CATEGORY':<12} | {'AMOUNT':<10}")
    print("-" * 55)
    
    for tx in transactions:
        print(f"{tx['type']:<10} | {tx['item']:<15} | {tx['category']:<12} | ${tx['amount']:>8.2f}")
        if tx['type'] == "Income":
            total_income += tx['amount']
        else:
            total_expense += tx['amount']
            
    net_balance = total_income - total_expense
    
    print("-" * 55)
    print(f"Total Income:   ${total_income:.2f}")
    print(f"Total Expenses: ${total_expense:.2f}")
    print(f"Net Balance:    ${net_balance:.2f}")
    print("-" * 55)
    input("\nPress Enter to return to main menu...")

def run_calculator():
    clear_screen()
    print("--- PYTHON RUNTIME CALCULATOR ---")
    print("Type a math problem (e.g., 500 + 120 - 45) and press Enter.")
    print("Type 'q' to go back.\n")
    
    while True:
        expr = input("Calculate: ").strip()
        if expr.lower() == 'q':
            break
        try:
            clean_expr = re.sub(r'[^0-9+\-*/.]', '', expr)
            if not clean_expr:
                print("❌ Invalid mathematical input.")
                continue
            res = eval(clean_expr, {"__builtins__": None}, {})
            print(f"Result: {float(res)}\n")
        except ZeroDivisionError:
            print("❌ Error: Division by zero is undefined.\n")
        except Exception:
            print("❌ Syntax Error: Check your math formulation.\n")

def main():
    while True:
        clear_screen()
        show_menu()
        choice = input("Select an option [1-5]: ").strip()
        
        if choice == '1':
            add_transaction(is_expense=True)
        elif choice == '2':
            add_transaction(is_expense=False)
        elif choice == '3':
            view_dashboard()
        elif choice == '4':
            run_calculator()
        elif choice == '5':
            clear_screen()
            print("Goodbye! Thank you for using pure Python.")
            sys.exit()
        else:
            print("❌ Choice out of bounds. Select 1 to 5.")
            input("\nPress Enter to retry...")

if __name__ == "__main__":
    main()
