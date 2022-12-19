import csv
from collections import defaultdict
from datetime import datetime

def calculate_balances(transactions_file):
    # Create a dictionary to store the balances for each customer
    balances = defaultdict(int)
    
    # Create a dictionary to store the minimum, maximum, and ending balances for each customer and month,
    # make customer ID key
    monthly_balances = defaultdict(lambda: defaultdict(int))
    
    #open transactons to read them
    with open(transactions_file, 'r') as f:
        reader = csv.reader(f)
        
        # Iterate through each transaction
        for row in reader:
            # Get the customer ID, date, and amount for the transaction
            customer_id = row[0]
            date = datetime.strptime(row[1], '%m/%d/%Y')
            amount = int(row[2])
            
            # Update the balance for the customer
            balances[customer_id] += amount
            
            #get MM and YYYY for transaction
            month = date.month
            year = date.year
            
            # Update the minimum, maximum, and ending balances for the customer and month
            monthly_balances[customer_id][(month, year)]['min'] = min(balances[customer_id], monthly_balances[customer_id][(month, year)]['min'])
            monthly_balances[customer_id][(month, year)]['max'] = max(balances[customer_id], monthly_balances[customer_id][(month, year)]['max'])
            monthly_balances[customer_id][(month, year)]['end'] = balances[customer_id]
    
    # Print the results in MM YYYY format
    for customer_id in monthly_balances:
        for (month, year) in monthly_balances[customer_id]:
            min_balance = monthly_balances[customer_id][(month, year)]['min']
            max_balance = monthly_balances[customer_id][(month, year)]['max']
            end_balance = monthly_balances[customer_id][(month, year)]['end']
            print(f"{customer_id}, {month}/{year}, {min_balance}, {max_balance}, {end_balance}")

calculate_balances('transactions.csv')

