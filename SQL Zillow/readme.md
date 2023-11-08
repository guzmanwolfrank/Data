# SQL: Zillow 

![download](https://github.com/guzmanwolfrank/SQL/assets/29739578/d03867fe-9822-40ed-b670-83ba3501df99)


## Project Description

Here we analyze Zillow Housing Data to check for highest cost locations, market trends and other patterns. 

This SQL project takes us through Python programming, SQL data cleansing, data analysis and data presentation via dashboard.  

### To view the project's Jupyter notebook, click [here](https://github.com/guzmanwolfrank/SQL/blob/main/SQL%20Zillow/ZillowProject.ipynb).

## Goals 

Our goal is to use SQL queries to help analyze data from Zillow's Top Tier Housing Data. Our goals are also to see what changes have occured on Top Tier Home Values in all 50 states and Washington DC.


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



## Findings 
Our analysis revealed compelling trends and findings: <br/>

Home values have witnessed a substantial increase over time, indicating the robust growth of the real estate market.<br/>

We observed a concentration of top-tier homes in a select few states, with mid-range priced homes becoming scarcer.<br/>

Surprisingly, Montana emerged as the state with the highest overall change in top-tier home values since 2019.<br/>

![chart5](https://github.com/guzmanwolfrank/Data-SQL/assets/29739578/36d6666c-ba4f-4c10-ac51-c548a6b55afe)

![chart4](https://github.com/guzmanwolfrank/Data-SQL/assets/29739578/9e04d0cd-f8c4-497e-9db0-ba36117672e5)



## Conclusion 
In this project, we embarked on a journey to explore Zillow's Top Tier Home Value data with the goal of understanding market trends, changes in home values, and emerging patterns in the real estate market. Through a combination of Python programming, SQL queries, data cleansing, and visualization, we delved into the dataset to uncover valuable insights.

Average Home Values: We examined the average home values by state in both September 2019 and September 2023, allowing us to observe the evolving landscape of top-tier home values over time.

Change in ZHVI: We identified the states with the highest changes in Zillow Home Value Index (ZHVI) to gain insights into which regions experienced the most significant shifts in property values.

Top 5 States with Highest Average Top Tier Home Values: We determined the top five states with the highest average top-tier home values, shedding light on the most sought-after real estate markets.


In conclusion, we've unlocked valuable information about top-tier home values, changes in ZHVI, and the evolving real estate market, paving the way for more informed decision-making in the world of real estate.

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
