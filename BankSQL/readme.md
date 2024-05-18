# BANK SQL 

# Banking and Money Movement Data Project

This project demonstrates the process of transforming a CSV file into a Looker Dashboard and SQL database.  We can run queries on the data, and visualize these queries in Seaborn and Looker. 
#
The project then creates a HTML file, with the Looker dashboard embedded,  which we can then place in a AWS S3 bucket.  





## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
  - [1. CSV to SQL Database](#1-csv-to-sql-database)
  - [2. Running SQL Queries](#2-running-sql-queries)
  - [3. Looker Dashboard](#3-looker-dashboard)
  - [4. SSIS and SSIR Reports](#4-ssis-and-ssir-reports)
- [Spreadsheet Columns Reference](#spreadsheet-columns-reference)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project takes a CSV file containing banking and money movement data and converts it into a SQL database using Python and SQLite. SQL queries are then run on the database to extract meaningful insights. Visualizations are created using Looker Dashboard, and reports are generated using SQL Server Integration Services (SSIS) and SQL Server Reporting Services (SSIR).

## Features

- Convert CSV file to SQL database
- Run SQL queries on the database
- Visualize data with Looker Dashboard
- Generate reports with SSIS and SSIR

## Setup

### Prerequisites

- Python 3.x
- SQLite
- Looker
- SSIS
- SSIR

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/banking-data-project.git
    cd banking-data-project
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. CSV to SQL Database

Run the following script to convert the CSV file into a SQLite database:

```python
import pandas as pd
import sqlite3

# Load CSV into DataFrame
df = pd.read_csv('data/banking_data.csv')

# Connect to SQLite database (or create it)
conn = sqlite3.connect('data/banking_data.db')

# Convert DataFrame to SQL
df.to_sql('banking_data', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

```

### 2. Running SQL Queries

Run SQL queries on the SQLite database using the following script:

```python
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('data/banking_data.db')
cursor = conn.cursor()

# Sample query
query = "SELECT * FROM banking_data WHERE amount > 1000"
result = cursor.execute(query).fetchall()

# Print the result
for row in result:
    print(row)

# Close the connection
conn.close()
```
### 3. Looker Dashboard

To visualize the data, I used Looker.  
## The Looker Dashboard can be found here (link#). 

### 4. SSIS and SSIR Reports

Generated reports using SSIS and SSIR. 

## You can view SSIS and SSIR here (link#)


For detailed instructions on creating and running reports, refer to the [SSIS Documentation]
(https://docs.microsoft.com/en-us/sql/integration-services/sql-server-integration-services) and [SSIR Documentation](https://docs.microsoft.com/en-us/sql/reporting-services/create-deploy-and-manage-mobile-and-paginated-reports).

## Spreadsheet Columns Reference

The CSV file contains the following columns related to banking and money movement:

- `TransactionID`: Unique identifier for each transaction
- `AccountID`: Unique identifier for each account
- `TransactionDate`: Date of the transaction
- `Amount`: Amount of money moved in the transaction
- `TransactionType`: Type of transaction (e.g., deposit, withdrawal)
- `Description`: Description of the transaction
- `First Name`: First name of the account holder
- `Last Name`: Last name of the account holder
- `VendorID`: Unique identifier for each vendor
- `FeeID`: Unique identifier for each fee
- `FeePayable`: Amount of fee payable
- `Card`: Type of card used (e.g., Virtual, Physical)
- `MCC GroupName`: Merchant Category Code group name
- `Channel`: Channel through which the transaction was made
- `CardState`: State of the card (e.g., active, inactive)
- `CardToken`: Tokenized representation of the card

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before you start.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

