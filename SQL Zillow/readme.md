# SQL: Zillow 

![download](https://github.com/guzmanwolfrank/SQL/assets/29739578/d03867fe-9822-40ed-b670-83ba3501df99)


## Project Description

Here we analyze Zillow Housing Data to check for highest cost locations, market trends and other patterns. 

This SQL project takes us through Python programming, SQL data cleansing, data analysis and data presentation via dashboard.  

To view the project Jupyter notebook, click [here](https://github.com/guzmanwolfrank/SQL/blob/main/SQL%20Zillow/ZillowProject.ipynb).

## Goals 

Our goal is to use SQL queries to help analyze data from Zillow's Top Tier Housing Data. Our goals are to see what changes have occured on Top Tier Home Values in all 50 states and Washington DC.


## Initial Questions 

Some of the  initial questions we hope to explore and answer are:

        What are the average home values by state in September 2019?  

        What are the average home values by state in Septemberr 2023? 

        What states have the highest change in ZHVI? 

        What are the top 5 states in terms of Highest Average Top Tier Home Values? 

      




## Data Dictionary
**Variable** |    **Value**    | **Meaning**
---|---|---
*Date* | Datetime object | The year of the data source
*SizeRank* | Float | A rank number is assigned to States.  The number 1 is the hihgest ranked state according to population and size. 
*State* | String | Name of state 
*ZHVI Value* | Float | A measure of the typical home value and market changes across a given region and housing type. It reflects the typical value for homes in the 35th to 65th percentile range. 


## Project Planning 

    Acquire
    Prepare
    Explore
    Model 

## Exploring the Data 

        # SQL Queries 

        We will use SQL Queries to explore the data within the ZHVI file and dataframe we build off of it. 

        In order to do so, we must the load the CSV data into a SQLite Database and connect to the database.  

<br/>

Here is a list of SQL Queries for analysis:

![queries](https://github.com/guzmanwolfrank/Data-SQL/assets/29739578/4557ae9a-5547-4727-945d-18aa375493c0)

## Seaborn Visualizations 

We can use the output of the SQL Queries to construct visualizations such as histograms of the data we have cleaned and queried.

![visuals](https://github.com/guzmanwolfrank/Data-SQL/assets/29739578/be0040bb-ac21-4af3-a1ba-b40926449c43)


## Findings 
We ran 7 SQL Queries using SQLite and Python to realize that home values, in Zillow's Top Tier Home Value Data have risen dramatically.

We also learned on Chart 5, a histogram, that the amount of mid range priced homes is dwindling. Homes across the Top Tier are becoming more expensive and concentrating in a handful of states.

![chart5](https://github.com/guzmanwolfrank/Data-SQL/assets/29739578/36d6666c-ba4f-4c10-ac51-c548a6b55afe)

Chart 4 also taught us some new developments, surprisingly to some, Montana has had the highest overall change in Top Tier Home Value across the United States dating back to 2019.

![chart4](https://github.com/guzmanwolfrank/Data-SQL/assets/29739578/9e04d0cd-f8c4-497e-9db0-ba36117672e5)

Overall, using SQLite, SQL Queries and Python we were able to analyze Zillow Top Tier Home Data for emerging trends and specific locations with higher values.


## Conclusion 


## Tech Stack 
seaborn==0.12.2 <br/>
pandas==2.0.3 <br/>
matplotlib==3.7.2 <br/>
numpy==1.25.2  <br/>

    Software: SQL,Google Looker, Streamlit, GoogleSheets, Python 3.11, VS Code, Jupyter Notebook
    Languages: SQL, Python
    Modules: Seaborn, Pandas, SQLite3, Matplotlib


## Badges 

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


## License 
[MIT](https://choosealicense.com/licenses/mit/)
