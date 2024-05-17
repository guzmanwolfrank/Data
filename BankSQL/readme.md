# BANK SQL 

# Banking and Money Movement Data Project

This project demonstrates the process of transforming a CSV file into a SQL database using Python and SQLite, and running SQL queries on the database. Additionally, it showcases how to create visualizations with Looker Dashboard and generate reports using SSIS and SSIR.

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
