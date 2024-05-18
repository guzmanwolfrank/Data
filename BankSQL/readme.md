# Banking Data Project

## Overview

This project demonstrates the process of transforming a CSV file into a Looker Dashboard and SQL database. We can run queries on the data, and visualize these queries using Seaborn and Looker.

Additionally, the project generates an HTML file with the Looker dashboard embedded, which can be placed in an AWS S3 bucket for easy access and sharing.

## Features

- **Data Transformation**: Reads data from a CSV file and transforms it into a format suitable for analysis.
- **SQL Integration**: Loads the transformed data into an SQLite database and runs various SQL queries.
- **Data Visualization**: Uses Seaborn to create visual representations of the query results.
- **Looker Dashboard**: Creates a Looker dashboard for interactive data exploration.
- **HTML Generation**: Generates an HTML file embedding the Looker dashboard.
- **Cloud Integration**: The generated HTML file can be uploaded to an AWS S3 bucket for online access.

## Project Structure

- `data/`: Contains the original CSV file and any additional data files.
- `Notebooks/`: Project Code. Includes Python script for data transformation, SQL operations, and visualization and HTML code.  
- `output_images/`: Stores generated output images from Seaborn plots.
- `README.md`: Project documentation.
- `banking_data_analysis.html`: Project HTML with embedded Looker Dashboard.

### Prerequisites

- Python 3.x
- Pandas
- SQLite3
- Seaborn
- Matplotlib
- Looker SDK
- AWS CLI (for S3 integration)



## Data Dictionary

The CSV file contains the following columns related to the Banking CSV File:

- **TransactionID**: Unique identifier for each transaction
- **AccountID**: Unique identifier for each account
- **TransactionDate**: Date of the transaction
- **Amount**: Amount of money moved in the transaction
- **TransactionType**: Type of transaction (e.g., deposit, withdrawal)
- **Description**: Description of the transaction
- **First Name**: First name of the account holder
- **Last Name**: Last name of the account holder
- **VendorID**: Unique identifier for each vendor
- **FeeID**: Unique identifier for each fee
- **FeePayable**: Amount of fee payable
- **Card**: Type of card used (e.g., Virtual, Physical)
- **MCC GroupName**: Merchant Category Code group name
- **Channel**: Channel through which the transaction was made
- **CardState**: State of the card (e.g., active, inactive)
- **CardToken**: Tokenized representation of the card

## SQL Queries 

queries = [<br> <br>
    # 1. Select first 10 rows <br>("SELECT * FROM banking_data LIMIT 10;", "Select first 10 rows") <br><br>
    # 2. Count the number of rows <br>("SELECT COUNT(*) AS Total_Transactions FROM banking_data;", "Count the number of rows"),  <br><br>
    # 3. Select distinct transaction types <br>("SELECT DISTINCT TransactionType FROM banking_data;", "Select distinct transaction types") <br><br>
    # 4. Calculate the average transaction amount <br>("SELECT AVG(Amount) AS Avg_Amount FROM banking_data;", "Calculate the average transaction amount") <br><br>
    # 5. Count number of transactions per state <br>("SELECT StateID, COUNT(*) AS Transaction_Count FROM banking_data GROUP BY StateID;", "Count number of transactions per state")  <br><br>
    # 6. Average transaction amount per currency <br>("SELECT Currency, AVG(Amount) AS Avg_Amount FROM banking_data GROUP BY Currency;", "Average transaction amount per currency")  <br><br>
     # 7. Top 5 transactions by amount <br>("SELECT TransactionDate, Amount FROM banking_data ORDER BY Amount DESC LIMIT 5;", "Top 5 transactions by amount") <br><br>
]


