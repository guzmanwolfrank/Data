# Banking Data Project

## Overview

This project demonstrates the process of transforming a CSV file into a Looker Dashboard and SQL database. We can run queries on the data, and visualize these queries using Seaborn and Looker.

Additionally, the project generates an HTML file with the Looker dashboard embedded, which can be placed in an AWS S3 bucket for easy access and sharing.

## Project Description

This project performs Data Analysis in order to better understand flagged accounts in a corporation's transactions database.  
<br>
The corporation, SQL Bank, wishes to attract investors for an IPO but first need to clean and fix their accounting, sales and credit systems. 
<br>
Recently, their internal systems have flagged 100 transactions for suspicious activity along with transacting while not paying on time, and also a few accounts somehow transacting while 
in suspended or terminated state.  
<br>
SQLBank's clients tend to be Vendors, Retail and Private-- who wholeseale short term credit and 
issue payment systems to their own customers.
<br>

The payment systems take Cryptocurrencies, USD Cash and VendorBucks.  VendorBucks are whitelabeled credit cards issued by the Vendors to their customers.  The Vendors then borrow money from SQL Bank 
in order to furnish credit and loans to their clients.  
<br>
Before making decisions, the Board has requested the Data Team to come up with unique Looker Dashboards using CSV files and SQL. 

Here, we create a Python script that Transforms the Flagged Transaction Data CSV into SQL, then runs queries which are visualized in Seaborn.  We then use the CSV Data to make a Dashboard using Google Looker.  

We can then embed the Dashboard into an HTML file with pertinent project data and analysis.  This HTML site is then downloaded and stored in an Amazon Web Services S3 Bucket for storage. 
<br>

Analyzing Flagged Data and making a dashboard and running SQL queries -- SQLBank, wishes to get a better understanding of their issues and how to solve them.  


## Project Features

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



<hr>

### [Jupyter Notebook](#) 
### [Looker Dashboard](https://lookerstudio.google.com/embed/reporting/d1e85f0d-9a43-4aab-ba44-d898cfa25feb/page/ZfY0D)
### [Data](#)

<hr>




## Visualizations 

# Looker Dashboard 
![image](https://github.com/guzmanwolfrank/Data-SQL/blob/10022a1059a16cbd7b2ba2d4c1aafe56c0fe2075/BankSQL/Dashboard/LookerBankSQL.jpg)

# SQL + Seaborn 

![chart2](https://github.com/guzmanwolfrank/Data-SQL/blob/86a3c797426a8a6252494e3f67c350e8c5ce43c5/BankSQL/output_images/plot_3.jpg)
</br>

![chart3](https://github.com/guzmanwolfrank/Data-SQL/blob/86a3c797426a8a6252494e3f67c350e8c5ce43c5/BankSQL/output_images/plot_5.jpg)
</br>
![chart5](https://github.com/guzmanwolfrank/Data-SQL/blob/86a3c797426a8a6252494e3f67c350e8c5ce43c5/BankSQL/output_images/plot_6.png)
</br>

## Findings 

We can see that Florida had the highest number overall of transactions while USD CASH had the highest average transaction amount per currency group. 

It is also worthy to note that Withdrawal was the most popular transaction type in the data. 




## Conclusion 


In conclusion, our analysis of the banking and money movement data reveals some interesting insights. Florida emerged as the state with the highest number of transactions overall, indicating a significant volume of financial activity in the region. Additionally, USD CASH stood out with the highest average transaction amount per currency group, suggesting that transactions involving this currency tend to be larger on average.

Furthermore, the dominance of Withdrawal as the most popular transaction type highlights a common financial behavior among account holders. This finding underscores the importance of understanding customer preferences and behaviors to tailor financial services effectively.

Overall, this project demonstrates the value of data analysis in uncovering patterns and trends within financial datasets, providing valuable insights that can inform business strategies and decision-making processes.


## License 

MIT License

Copyright (c) [2024] [Wolfrank Guzman]

