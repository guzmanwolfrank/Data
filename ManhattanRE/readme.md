# Analyzing Manhattan Rolling Sales Data from November 2022 to October 2023 using Python and Seaborn
Data Project by
#### Wolfrank Guzman <br/>
GitHub: [guzmanwolfrank](#) <br/>
Website: [guzmanwolfrank.com](#) <br/>

#

![westidecrop](https://github.com/guzmanwolfrank/Data-SQL/assets/29739578/257bdaee-d986-4ed8-8d1a-a9dca04a81e3)

## Project Overview:

This project aims to analyze and visualize Manhattan Rolling Sales Data from November 2022 to October 2023 using Python and Seaborn. The data will be extracted from the NYC Open Data website and preprocessed to ensure its cleanliness and consistency. Subsequently, exploratory data analysis techniques will be employed to uncover patterns and trends within the data. Finally, insightful visualizations will be created using Seaborn to effectively communicate the findings to a wider audience.


### To view the project's Jupyter notebook, click [here](#).

## Data Description:

The Manhattan Rolling Sales Data comprises information on properties that have sold in the last twelve-month period in Manhattan, categorized under tax classes 1, 2, and 4. Key attributes within the dataset include the property's neighborhood, building type, square footage, and other relevant details.   Sales Data as of 11/8/2023


## Tools and Technologies:

Python: A versatile programming language widely used for data analysis and manipulation.

Seaborn: A Python library for data visualization that provides a high-level interface for creating aesthetically pleasing and informative plots.

## Links 

https://www.nyc.gov/site/finance/taxes/property-rolling-sales-data.page

https://www.nyc.gov/assets/finance/jump/hlpbldgcode.html


## Project Objectives:

Gain insights into the distribution of property sales across different neighborhoods in Manhattan.

Identify trends in property sales based on building type and square footage.

Analyze the relationship between property sales and other relevant factors, such as neighborhood characteristics and economic indicators.

Create compelling visualizations to effectively communicate the findings to a non-technical audience.

## Project Deliverables:

A comprehensive data analysis report documenting the findings and insights extracted from the data.

A collection of interactive visualizations using Seaborn to illustrate the key trends and patterns observed within the data.

A presentation summarizing the project's methodology, findings, and implications for understanding property sales in Manhattan.


## Goals 

Our goal is to use SQL queries to help analyze sales data from different neighborhoods across Manhattan. 

## Initial Questions 

The  initial questions we hope to explore and answer are:

        # Query 1: Number of properties sold per neighborhood? 

     
        
        # Query 2: What is the distribution of Sale Prices by Building Category? 
        
  

        # Query 3:  What is the Sales distribution over Time? 



        # Query 4: What is the Sales Price distribution by Neighborhood? 

      

        # Query 5: What is the number of properties sold by tax class?
    
         

        # Query 6: What is the Average GROSS SF by Neighborhood?
        
      
    

## Data Dictionary
**Variable** |    **Value**    | **Meaning**
---|---|---
*Date* | Datetime object | The year of the data source
*SizeRank* | Float | A rank number is assigned to States.  The number 1 is the hihgest ranked state according to population and size. 
*State* | String | Name of state 
*ZHVI Value* | Float | A measure of the typical home value and market changes across a given region and housing type. It reflects the typical value for homes in the 35th to 65th percentile range. 


## Exploring the Data 

        # SQL Queries 

        We will use SQL Queries to explore the data within the ZHVI file and dataframe we build off of it. 

        In order to do so, we must the load the CSV data into a SQLite Database and connect to the database.  

<br/>

Here is a list of SQL Queries for analysis:

        # Query 1: Number of properties sold per neighborhood? 

        query1 = """
        SELECT NEIGHBORHOOD, COUNT(*) AS num_sales
        FROM sales_data
        GROUP BY NEIGHBORHOOD
        ORDER BY num_sales DESC
        """
        
        # Query 2: What is the distribution of Sale Prices by Building Category? 
        
        query2 = """
        SELECT BLDGCAT, SALE_PRICE
        FROM sales_data
        WHERE SALE_PRICE IS NOT NULL;      
        """

        # Query 3:  What is the Sales distribution over Time? 

        query3 = """
        SELECT SALE_DATE, SALE_PRICE
        FROM sales_data
        WHERE SALE_PRICE IS NOT NULL;
        """

        # Query 4: What is the Sales Price distribution by Neighborhood? 

        query4 = """
        SELECT NEIGHBORHOOD, SALE_PRICE
        FROM sales_data
        WHERE SALE_PRICE IS NOT NULL;
        """

        # Query 5: What is the number of properties sold by tax class?
        query5 = """
        SELECT TAXCLP, COUNT(*) AS num_sales
        FROM sales_data
        GROUP BY TAXCLP;
        """
       

        # Query 6: What is the Average GROSS SF by Neighborhood?
        
        query6 = """
        SELECT NEIGHBORHOOD, AVG(GROSSSF) AS avg_gross_sf
        FROM sales_data
        GROUP BY NEIGHBORHOOD;
        """

    



## Seaborn Visualizations 

We can use the output of the SQL Queries to construct visualizations such as histograms of the data we have cleaned and queried.

![chart5](https://github.com/guzmanwolfrank/Data-SQL/assets/29739578/36d6666c-ba4f-4c10-ac51-c548a6b55afe)


## Findings 
Our analysis revealed compelling trends and findings: <br/>

Home values have witnessed a substantial increase over time, indicating the robust growth of the real estate market.<br/>

We observed a concentration of top-tier homes in a select few states, with mid-range priced homes becoming scarcer.<br/>

Surprisingly, Montana emerged as the state with the highest overall change in top-tier home values since 2019.<br/>


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
