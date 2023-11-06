
# SQL Algo Project

![266731439-4c3c7f68-1202-4f2f-81f9-538b4ca8a21e](https://github.com/guzmanwolfrank/SQL/assets/29739578/eefe1cf6-b8e0-452d-a5fd-d242926b9079)


We created a backtest in our Project. This backtest created a dataframe, which we then created a CSV for. We will import the csv and use SQL commands in SQLite to Query the data. Follow the project in our [jupyter notebook](https://github.com/guzmanwolfrank/SQL/blob/main/AlgoSQL/SQLproject.ipynb).

## Objective

My objective was to run SQL Queries on data in order to analyze the results of the algorithmic backtest. 

We can then discover if the backtest strategy was profitable enough to continue developing and perhaps deploy.  

## Deployment

To deploy this project run the [jupyter notebook](https://github.com/guzmanwolfrank/SQL/blob/main/AlgoSQL/SQLproject.ipynb) in your IDE of choice.  If you are using VSCode, simply download the notebook file and run the notebook with a python kernel. <br/>

Alternatively, you can use Google Drive and [Colaboratory](https://colab.research.google.com/?utm_source=scs-index).  <br/>

In Google Drive in your web browser, open the Jupyter notebook with Colaboratory. Run the cells in this notebook to see:  the data, solutions to questions asked and the results of the backtest. 

## Challenges

A challenge I had was deciding what visualization would help display standard deviation and averages in the simplest form.  

## Solutions 

I found that a seaborn boxplot could help me visualize the daily returns in the simplest format. 

![boxplot](https://github.com/guzmanwolfrank/Data-SQL/assets/29739578/cae641fc-a347-4099-8a8c-41d4963bb8c9)

# Queries 
Some of the SQL (sqlite) Queries involved in analyzing the results in this project are:  

###  What was the average profit per trade?

![carbon (8)](https://github.com/guzmanwolfrank/Data-SQL/assets/29739578/42680be6-f14b-496e-b42e-ebe1122d3a09)

###  Now, let's use a SQL Query to see what the profitable trades look like. 
    How many were there? What were their profit amounts in relation to count? 

![carbon (9)](https://github.com/guzmanwolfrank/Data-SQL/assets/29739578/0ea9022a-8e7e-44f1-91e3-c011f9293039)

### How does the strategy's return percentage compare to the benchmark?

![carbon (10)](https://github.com/guzmanwolfrank/Data-SQL/assets/29739578/7e21922f-c5e2-4568-bbf7-fb31cf25a5cd)

## Conclusion 

In conclusion, after querying results, we see that the algorithmic backtest strategy was more profitable than the benchmark of buy and hold on TQQQ stock.

The standard deviation made it predictable and risk averse, while the signals generated trades that were highly profitable and had limited drawdown and losing trades and days.

The strategy return ended up being $32,000 higher than the benchmark of buy and hold on TQQQ.

A simple buy strategy on a moving average cross was able to beat the volatility and drawdown that TQQQ sustained on a buy and hold approach.

By using SQL queries we were also able to identify certain trades along with analyzing data.


## Tech Stack
seaborn==0.12.2 <br/>
yfinance==0.2.27 <br/>
pandas==2.0.3 <br/>
matplotlib==3.7.2 <br/>
numpy==1.25.2 <br/>


## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)



## License

[MIT](https://choosealicense.com/licenses/mit/)




