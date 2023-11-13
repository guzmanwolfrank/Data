## SQL: Salary Data

![avgsal](https://github.com/guzmanwolfrank/SQL/assets/29739578/b161b907-2b5c-46a6-b4e3-21ab12414a54)

## Project Description

In this SQL project we combine Python and SQL while generating fictional data using the Faker module. We will generate information for a fictional survey which details salaries, survey questions, age and other data to then analyze and look for patterns in the data.


        Software: SQL, Python 3.11, VS Code, Jupyter Notebook
        Languages: SQL, Python
        Modules: Faker, Seaborn, Pandas, SQLite3, Matplotlib

## To view the project code and Jupyter notebook, click [here](https://github.com/guzmanwolfrank/Data-SQL/blob/main/SQLSalaryData/RandomData.ipynb)


## Goals 
To practice using SQL Queries to solve problems and analyze randomly generated data.  Another goal was to simply use the Faker module and see how flexible it is generating data for 
visualization purposes.  Generating Fake data is also useful in algorithmic research when running algorithms multiple times to find patterns in random sequences. 

## Initial Queries for SQLite 

High Earners: Identify and analyze individuals earning above $200,000.

Top Earner: Determine the individual with the highest salary and their occupation.

Youngest Worker: Identify the youngest individual in the dataset and their details.

Occupation Salaries: Calculate and analyze average salaries for each occupation.

Top 10 Paying Occupations: Rank and analyze the top 10 highest-paying occupations.

Education Level vs. Salary: Analyze the relationship between education level and average salary.

Job Satisfaction by State: Calculate and analyze average job satisfaction scores for each state.


 
##  Data Dictionary
**Variable** |    **Value**    | **Meaning**
---|---|---
*RecordID* | Float | The id number of the entry or record
*First* |String| First Name
*Last* | String | Last Name
*Sex* | String  | Sex
*Age* | Float | Age
*Occupation* | String | Occupation
*Country of Birth* | String | Country of Birth
*Education* | String | Education 
*Salary*| Float | Salary
*Email*| String | Email
*Years of Experience*| Float | Years of Experience 
*Avg Salary for Occupation*| Float | Average salary for the occupation 
*State*| String | State
*Satisfaction Score*| Float | Number from 1 to 10 defining the satisfaction of the employee 
*Work Location*| String | Location 


## Project Planning / Process 

Acquire: Acquire the data by using Faker Module and generating the data in Python within a Pandas Dataframe.  <br/> 
Prepare:  Prepare the data by cleaning, filtering n/a values, and sorting the data. 
Explore:  I plan to use Seaborn and SQLite Python module to explore and visualize the information.  I am using SQL Queries via SQLite in order to answer my initial queries. 

## Exploring the Data 
![sqlitequerieslabor](https://github.com/guzmanwolfrank/Data-SQL/assets/29739578/9fa4981c-8f90-4816-8615-54180a503756)

![occupationschart](https://github.com/guzmanwolfrank/Data-SQL/assets/29739578/45513aaf-d5c1-405b-9f39-d53e5bd40c90)

*Note:  Here we see the consequence of using a fake data generator module such as Faker but will reap the benefit in having random data, visualized. 
![sqlqueries2](https://github.com/guzmanwolfrank/Data-SQL/assets/29739578/4503c161-c674-4a00-bb8f-625b0398894d)


## Findings 

## Conclusion 

## Tech Stack / Requirements 

pandas==2.0.3 <br/> 
random==3.10 <br/>
faker==19.6.1 <br/>
seaborn==0.12.2 <br/>
matplotlib.pyplot==3.7.2 <br/>
sqlite3==3.43.1 <br/>


## Badges
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


## License
[MIT](https://choosealicense.com/licenses/mit/)



