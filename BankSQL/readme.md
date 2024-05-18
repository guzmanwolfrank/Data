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
- `Notebooks/`: Includes Python script for data transformation, SQL operations, and visualization.  
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




