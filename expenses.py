# 1.This is a Dictionary -perfect for labeled data
monthly_expenses = {"Rent":1200,
                    "Groceries":400,
                    "Internet":60,
                    "Gym":50,
                    "Streaming":30}
# 2. A function to calculate the total and check the budget
def analyze_spending (expenses_dict,budget_limit):
    total = sum(expenses_dict.values())
    print(f"Total Spending:${total}")
    if total>budget_limit:
        print("Warning: You are over budget!")
    else:
        print("Looking good!You are within budget.")
        return total
# 3. Running the function with a $1500 limit
analyze_spending(monthly_expenses,1500)
