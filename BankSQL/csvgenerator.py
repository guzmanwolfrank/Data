import csv
import random
from faker import Faker
import os

# Initialize Faker
fake = Faker()

# Define the number of records to generate
num_records = 100

# Define possible values for certain fields
transaction_types = ['deposit', 'withdrawal']
card_types = ['Virtual', 'Physical']
card_states = ['active', 'inactive']
channels = ['online', 'branch', 'ATM']

# Define the output CSV file path
output_file = 'fake_banking_data.csv'

# Open a CSV file for writing
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow([
        'TransactionID', 'AccountID', 'TransactionDate', 'Amount', 'TransactionType', 
        'Description', 'First Name', 'Last Name', 'VendorID', 'FeeID', 'FeePayable', 
        'Card', 'MCC GroupName', 'Channel', 'CardState', 'CardToken'
    ])
    
    # Write the fake data rows
    for _ in range(num_records):
        transaction_id = fake.uuid4()
        account_id = fake.uuid4()
        transaction_date = fake.date_this_year()
        amount = round(random.uniform(10.0, 1000.0), 2)
        transaction_type = random.choice(transaction_types)
        description = fake.sentence()
        first_name = fake.first_name()
        last_name = fake.last_name()
        vendor_id = fake.uuid4()
        fee_id = fake.uuid4()
        fee_payable = round(random.uniform(1.0, 50.0), 2)
        card = random.choice(card_types)
        mcc_group_name = fake.company()
        channel = random.choice(channels)
        card_state = random.choice(card_states)
        card_token = fake.credit_card_number()

        writer.writerow([
            transaction_id, account_id, transaction_date, amount, transaction_type, 
            description, first_name, last_name, vendor_id, fee_id, fee_payable, 
            card, mcc_group_name, channel, card_state, card_token
        ])

# Get the absolute path of the CSV file
file_path = os.path.abspath(output_file)
print(f"Fake data generated and saved to '{file_path}'.")

