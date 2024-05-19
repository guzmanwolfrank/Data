import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt
import os
import warnings
import boto3
from botocore.exceptions import NoCredentialsError

# Ignore warnings
warnings.filterwarnings("ignore")

# Set seaborn color palette to 'viridis'
sns.set_palette('Blues')

# File path to the CSV file
file_path = 'https://raw.githubusercontent.com/guzmanwolfrank/Data-SQL/main/BankSQL/data/datagen/banking_data.csv'

# Read CSV file into pandas DataFrame
df = pd.read_csv(file_path)

# Connect to SQLite database (or create it)
conn = sqlite3.connect('banking_data.db')

# Convert DataFrame to SQL
df.to_sql('banking_data', conn, if_exists='replace', index=False)

# Function to run SQL query and return the result as a DataFrame
def run_query(query):
    return pd.read_sql_query(query, conn)

# Define SQL queries with corresponding questions
queries = [
    ("SELECT * FROM banking_data LIMIT 10;", "Select first 10 rows"),  # 1. Select first 10 rows
    ("SELECT COUNT(*) AS Total_Transactions FROM banking_data;", "Count the number of rows"),  # 2. Count the number of rows
    ("SELECT DISTINCT TransactionType FROM banking_data;", "Select distinct transaction types"),  # 3. Select distinct transaction types
    ("SELECT AVG(Amount) AS Avg_Amount FROM banking_data;", "Calculate the average transaction amount"),  # 4. Calculate the average transaction amount
    ("SELECT State, COUNT(*) AS Transaction_Count FROM banking_data GROUP BY State;", "Count number of transactions per state"),  # 5. Count number of transactions per state
    ("SELECT Currency, AVG(Amount) AS Avg_Amount FROM banking_data GROUP BY Currency;", "Average transaction amount per currency"),  # 6. Average transaction amount per currency
    ("SELECT TransactionDate, Amount FROM banking_data ORDER BY Amount DESC LIMIT 5;", "Top 5 transactions by amount"),  # 7. Top 5 transactions by amount
]

# Execute queries and store the results
results = [run_query(query[0]) for query in queries]

# Close the connection
conn.close()

# Create visualizations using seaborn
sns.set(style="whitegrid", palette="Blues")

# Save Seaborn images as JPEG files
output_folder = "output_images"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Generate and save Seaborn plots
for i, (query, question) in enumerate(queries, 1):
    plt.figure(figsize=(10, 6))
    if i == 6:
        plt.figure(figsize=(12, 6))
        sns.distplot(results[i-1]['Avg_Amount'], color='blue')
        plt.title("Distribution of Average Transaction Amount per Currency")
        plt.xlabel("Average Transaction Amount")
        plt.ylabel("Density")
        image_path = os.path.join(output_folder, "output.png")
    else:
        if len(results[i-1].columns) == 1:  # If there's only one column
            sns.barplot(data=results[i-1], x=results[i-1].columns[0], y=results[i-1].index, palette="Blues")
            plt.xlabel(results[i-1].columns[0])
        else:
            sns.barplot(data=results[i-1], x=results[i-1].columns[0], y=results[i-1].columns[1], palette="Blues")
            plt.xlabel(results[i-1].columns[0])
            plt.ylabel(results[i-1].columns[1])
        plt.title(question)
        image_path = os.path.join(output_folder, f"plot_{i}.jpg")
        if i == 5:  # Rotate x-axis labels for query 5 plot
            plt.xticks(rotation=90)
    plt.savefig(image_path)
    plt.close()

# Generate HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Banking Data Project</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Roboto', sans-serif;
            background-color: #ffffff;
            color: #000000;
            display: flex;
            flex-wrap: wrap;
            flex-direction: row;
            font-size: 22px;
        }
         nav  {
            background-color: #000000;
            color: #000000;
            min-width: 100%;
            text-align: left;
            font-size: 32px;
            position: fixed;
        }
        nav ul {
            list-style-type: none;
            margin: 0;
            padding: 20px;
            color: #ffffff;
            width: 100%;
            background-color: #000000;
        }
        nav ul li {
            display: inline-block;
            margin-right: 10px;
            text-decoration: none;
            color: #ffffff;
            background-color: #000000;
        }
        nav ul li a {
            color: #ffffff;
            text-decoration: none;
            background-color: #000000;
        }
        a {
            color: grey;
            text-decoration: none;
        }
        a:hover {
            color: darkgrey;
        }
        a:visited {
            color: grey;
        }
        a:active {
            color: grey;
        }
        h1 {
            color: #333;
        }
        h2, h3, h4 {
            color: #444;
        }
        h5 {
            font-size: 36px;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border: 1px solid #ddd;
        }
        .container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
        }
        .column {
            width: 40%;
            margin-bottom: 80px;
            float: left;
        }
        .column2 {
            width: 40%;
            margin-bottom: 40px;
            float: right;
        }
        .column3 {
            width: ;
            margin-bottom: 40px;
            margin-top:40px;
            margin: 50px;
        }
        .query {
            margin-bottom: 20px;
        }
        .query-title {
            font-size: 18px;
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
        }
        .query-result {
            border-collapse: collapse;
            width: 80%;
            font-size: 14px;
        }
        .query-result th, .query-result td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        .query-result th {
            background-color: #f2f2f2;
        }
        .query-image {
            margin-top: 20px;
        }
        .query-image img {
            max-width: 100%;
        }
    </style>
</head>
<body>
 <nav>
            <div>
                <ul>
                            <li><a href="#">BankSQL >>  Short Term Credit Transactions Data Analysis</a></li>
                </ul>
            </div>
        </nav>
    <div class="row">
        <div class="column3">
           <br>
           <br>
           <br>
           <br>
           <br>
            <h1>Banking Data Project</h1>
  <p>  Wolfrank Guzman >> @guzmanwolfrank: Github >> email: guzmanwolfrank@gmail.com >> c: 917.443.1411 <p>
            <h2>Overview</h2>
            <p>This project demonstrates the process of transforming a CSV file into a Looker Dashboard and SQL database.
                We can run queries on the data, and visualize these queries using Seaborn and Looker.</p>
            <p>Additionally, the project generates an HTML file with the Looker dashboard embedded, which can be placed
                in an AWS S3 bucket for easy access and sharing.</p>
            <h2>Project Description</h2>
        <p>This project performs Data Analysis for SQLBank in order to better understand flagged accounts in the corporation's transactions database.</p>
        <p>The corporation, SQL Bank, wishes to attract investors for an IPO but first need to clean and fix their accounting, sales and credit systems.</p>
        <p>Recently, their internal systems have flagged 100 transactions for suspicious activity along with transacting while not paying on time, and also a few accounts somehow transacting while in suspended or terminated state.</p>
        <p>SQLBank's clients tend to be Vendors, Retail and Private-- who wholesale short term credit and issue payment systems to their own customers.</p>
        <p>The payment systems take Cryptocurrencies, USD Cash and VendorBucks. VendorBucks are white-labeled credit cards issued by the Vendors to their customers. The Vendors then borrow money from SQL Bank in order to furnish credit and loans to their clients.</p>
        <p>Before making decisions, the Board has requested the Data Team to come up with unique Looker Dashboards using CSV files and SQL.</p>
        <p>Here, we create a Python script that Transforms the Flagged Transaction Data CSV into SQL, then runs queries which are visualized in Seaborn. We then use the CSV Data to make a Dashboard using Google Looker.</p>
        <p>We can then embed the Dashboard into an HTML file with pertinent project data and analysis. This HTML site is then downloaded and stored in an Amazon Web Services S3 Bucket for storage.</p>
        <p>Analyzing Flagged Data and making a dashboard and running SQL queries -- SQLBank, wishes to get a better understanding of their issues and how to solve them.</p>

        <h2>Project Features</h2>
        <ul>
            <li><strong>Data Transformation:</strong> Reads data from a CSV file and transforms it into a format suitable for analysis.</li>
            <li><strong>SQL Integration:</strong> Loads the transformed data into an SQLite database and runs various SQL queries.</li>
            <li><strong>Data Visualization:</strong> Uses Seaborn to create visual representations of the query results.</li>
            <li><strong>Looker Dashboard:</strong> CSV Data is Loaded into Looker dashboard for interactive data exploration.</li>
            <li><strong>HTML Generation:</strong> Generates an HTML file embedding the Looker dashboard.</li>
            <li><strong>Cloud Integration:</strong> The generated HTML file can be uploaded to an AWS S3 bucket for online access.</li>
        </ul>

        <h2>Project Structure</h2>
        <ul>
            <li><code>Dashboard/</code>: Contains the Dashboard PDF and a Sample Image. A markdown format file with the links and embed text are also stored here.</li>
            <li><code>data/</code>: Contains the datagen folder in which the backup jupyter notebook and CSV Data file are stored. A test file is also store.</li>
            <li><code>Notebooks/</code>: Project Code. Includes Python script (SQLHTML.ipynb) for data transformation, SQL operations, and visualization and HTML code. This script also contains code to send to AWS S3 Bucket.</li>
            <li><code>output_images/</code>: Stores generated output images from Seaborn plots and other images from the project.</li>
            <li><code>SQL</code>: Project Jupyter notebook to generate visuals and analyze the SQL data using Python and Seaborn. This folder also contains the SQL queries in a text file.</li>
            <li><code>README.md</code>: Project documentation.</li>
            <li><code>banking_data_analysis.html</code>: Project HTML with embedded Looker Dashboard.</li>
            <li><code>Requirements.txt</code>: Project requirements and modules needed.</li>
        </ul>

        <hr>

        <h2><a href="#">Jupyter Notebook</a></h2>
        <h2><a href="https://lookerstudio.google.com/s/uC0WU8zs5_I">Looker Dashboard</a></h2>
        <h2><a href="#">Data</a></h2>

        <hr>

        <h3>Prerequisites</h3>
        <ul>
            <li>Python 3.x</li>
            <li>Pandas</li>
            <li>SQLite3</li>
            <li>Seaborn</li>
            <li>Matplotlib</li>
            <li>Looker SDK</li>
            <li>AWS CLI (for S3 integration)</li>
        </ul>

            <h2>Data Dictionary</h2>
            <p>The CSV file contains the following columns related to the Banking CSV File:</p>
            <ul>
                <li><strong>TransactionID</strong>: Unique identifier for each transaction</li>
                <li><strong>AccountID</strong>: Unique identifier for each account</li>
                <li><strong>TransactionDate</strong>: Date of the transaction</li>
                <li><strong>Amount</strong>: Amount of money moved in the transaction</li>
                <li><strong>TransactionType</strong>: Type of transaction (e.g., deposit, withdrawal)</li>
                <li><strong>Description</strong>: Description of the transaction</li>
                <li><strong>First Name</strong>: First name of the account holder</li>
                <li><strong>Last Name</strong>: Last name of the account holder</li>
                <li><strong>VendorID</strong>: Unique identifier for each vendor</li>
                <li><strong>FeeID</strong>: Unique identifier for each fee</li>
                <li><strong>FeePayable</strong>: Amount of fee payable</li>
                <li><strong>Card</strong>: Type of card used (e.g., Virtual, Physical)</li>
                <li><strong>MCC GroupName</strong>: Merchant Category Code group name</li>
                <li><strong>Channel</strong>: Channel through which the transaction was made</li>
                <li><strong>CardState</strong>: State of the card (e.g., active, inactive)</li>
                <li><strong>CardToken</strong>: Tokenized representation of the card</li>
            </ul>
        </div>
        <div class="column3">
        <h5> Looker Dashboard </h5> 
<iframe width="1500px" height="1500px" src="https://lookerstudio.google.com/embed/reporting/d1e85f0d-9a43-4aab-ba44-d898cfa25feb/page/ZfY0D" frameborder="0" style="border:0" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"></iframe>            <h2>SQL Queries</h2>
            <img src="https://raw.githubusercontent.com/guzmanwolfrank/Data-SQL/main/BankSQL/output_images/sqlqueries.png"   width="60%" height="60%" alt="me">  

      <br>               
              <img src="https://raw.githubusercontent.com/guzmanwolfrank/Data-SQL/main/BankSQL/output_images/plot_5.jpg" width="50%" height="50%" alt="me">
              <img src="https://raw.githubusercontent.com/guzmanwolfrank/Data-SQL/main/BankSQL/output_images/plot_3.jpg" width="50%" height="50%" alt="me">
              <img src="https://raw.githubusercontent.com/guzmanwolfrank/Data-SQL/main/BankSQL/output_images/currencytransact.png" width="50%" height="50%" alt="me">
              <br>
              
              
            <h2> AWS S3 Upload </h2> 
                      
                  <img src="https://raw.githubusercontent.com/guzmanwolfrank/Data-SQL/main/BankSQL/output_images/awsupload.png"   width="60%" height="60%" alt="me">  
                      
            <h2>Findings</h2>
            
              
              <p><strong>i.</strong> We can see that Florida had the highest number overall of transactions while USD CASH had the highest average transaction amount per currency group.</p>
        <p>SQLBank can now look into how to make sure the Florida flagged transactions can be reduced. Next steps can include running a Florida specific report on account status, late payments, and root causes for flagged transactions in the region.</p>
        <p><strong>ii.</strong> The average transaction amount that was flagged was around $3,000 dollars.</p>
        <p>SQLBank can now investigate further as to why this amount is the most common amongst flagged accounts. Next month a SQL Query can be run as to focus on transactions in this bandwidth.</p>
        <p><strong>iii.</strong> Transfers had the highest amounts per transaction but Withdrawals were the most frequent.</p>
        <p>This is problematic as flagged withdrawals offer the least chance of recouping losses or fraudulent charges and transactions. We can now check our data and dashboard and see which regions had the highest withdrawals.</p>
        <p><strong>iv.</strong> The Dashboard reveals that the least problematic region for SQLBank is the West Coast.</p>
        <p>A manager from the Fraud team will be sent out to the California Branches along with the SouthWestern regions to investigate how things are run better there and why there are less flagged transactions. By contrasting business practices in the West Coast to the more problematic Eastern seaboard clients, SQLBank looks to bridge the gap within their flagged transactions and fraud departments.</p>

        <h2>Conclusion</h2>
        <p>In conclusion, our analysis of the banking and money movement data reveals some interesting insights. Florida emerged as the state with the highest number of transactions overall, indicating a significant volume of financial activity in the region. Additionally, USD CASH stood out with the highest average transaction amount per currency group, suggesting that transactions involving this currency tend to be larger on average.</p>
        <p>Furthermore, the dominance of Withdrawal as the most popular transaction type highlights a common financial behavior among account holders. This finding underscores the importance of understanding customer preferences and behaviors to tailor financial services effectively.</p>
        <p>Overall, this project demonstrates the value of data analysis in uncovering patterns and trends within financial datasets, providing valuable insights that can inform business strategies and decision-making processes.</p>

        <h2>License</h2>
        <p>MIT License</p>
        <p>Copyright (c) 2024 Wolfrank Guzman</p>

            
"""

# Close the HTML content
html_content += """
</div>
</body>
</html>
"""

# Save HTML content to a file
html_file_path = "banking_data_analysis.html"
with open(html_file_path, "w") as html_file:
    html_file.write(html_content)

print(f"HTML file saved to: {os.path.abspath(html_file_path)}")



# AWS S3 Upload
def upload_to_s3(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified, file_name is used
    :return: True if file was uploaded, else False
    """
    # AWS credentials
    aws_access_key_id = 'YOUR_AWS_ACCESS_KEY'
    aws_secret_access_key = 'YOUR_AWS_SECRET_KEY'
    
    
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except NoCredentialsError:
        print("Credentials not available")
        return False
    return True

# Set the parameters for the S3 upload
bucket_name = 'your-bucket-name'
file_to_upload = html_file_path
s3_object_name = 'banking_data_analysis.html'

# Upload the file to S3
upload_successful = upload_to_s3(file_to_upload, bucket_name, s3_object_name)
if upload_successful:
    print(f"File successfully uploaded to S3 bucket '{bucket_name}' as '{s3_object_name}'")
else:
    print("File upload failed")
