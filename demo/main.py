import pandas as pd
from qplex.library.qmodel import QModel
from itertools import product
import re


# Helper function to build the demo df based on the ones downloaded from the internet
def build_demo_df():
    data = pd.read_csv('data/stock_data.csv')
    temp = pd.DataFrame()
    temp['Period'] = data['date'].unique()
    column_list = data['Name'].unique()
    temp = set_columns(data, temp, column_list)
    refactored_df = pd.DataFrame(columns=temp.columns.tolist())
    years = ['2013-02', '2013-03', '2013-04', '2013-05', '2013-06', '2013-07', '2013-08', '2013-09', '2013-10',
             '2013-11', '2013-12', '2014-01', '2014-02', '2014-03', '2014-04', '2014-05', '2014-06', '2014-07',
             '2014-08', '2014-09', '2014-10', '2014-11', '2014-12', '2015-01', '2015-02', '2015-03', '2015-04',
             '2015-05', '2015-06', '2015-07', '2015-08', '2015-09', '2015-10', '2015-11', '2015-12', '2016-01',
             '2016-02', '2016-03', '2016-04', '2016-05', '2016-06', '2016-07', '2016-08', '2016-09', '2016-10',
             '2016-11', '2016-12', '2017-01', '2017-02', '2017-03', '2017-04', '2017-05', '2017-06', '2017-07',
             '2017-08', '2017-09', '2017-10', '2017-11', '2017-12', '2018-01']
    year_index = 0
    years_len = len(years)
    for index in temp.index:
        if year_index > years_len - 1:
            break
        if re.match(rf"^{years[year_index]}.*", temp.loc[index, 'Period']):
            refactored_df = pd.concat([refactored_df, temp.iloc[[index]]], ignore_index=True)
            year_index = year_index + 1
    refactored_df.to_csv('data/demo_data.csv', index=False)


def set_columns(data, df, cols):
    refactored_df = pd.concat([df, pd.DataFrame(columns=cols)])
    for col in cols:
        col_to_add = data[data['Name'] == col]['open'].tolist()
        col_size = len(data[data['Name'] == col]['open'].tolist())
        if col_size == 1259:
            refactored_df = refactored_df.assign(**{col: col_to_add})
        else:
            refactored_df.drop([col], axis=1, inplace=True)

    return refactored_df


def get_data(b):
    # build_demo_df()
    data = pd.read_csv('data/demo_data.csv', index_col=0)
    # print(data)
    max_num_shares = (b / data.iloc[-1]).astype(int)
    price = data.iloc[-1]
    monthly_returns = data[data.columns.values.tolist()].pct_change().iloc[1:]
    avg_monthly_returns = monthly_returns.mean(axis=0)
    covariance_matrix = monthly_returns.cov()
    return max_num_shares, price, avg_monthly_returns, covariance_matrix, data.columns.tolist()


# Define budget
budget = 1000
# Define max_risk
max_risk = 1373.85

max_num_shares, price, avg_monthly_returns, covariance_matrix, stocks = get_data(budget)

# Define n -> number of variables
n = len(stocks)
# Create model
print("Creating QModel")
portfolio_model = QModel('portfolio')
# Define variable list
print("Adding variables...", end="")
x = portfolio_model.integer_var_list(n, name=lambda index: stocks[index], ub=max_num_shares, lb=0)
print(" done")
# constraint: cost <= budget
print("Computing cost constraint...", end="")
cost = sum(price[s] * x[index] for index, s in enumerate(stocks))
print(" done")
# constraint: risk <= max_risk
print("Computing risk constraint...", end="")
risk = 0
for i, s1 in enumerate(stocks):
    for j, s2 in enumerate(stocks):
        coefficient = covariance_matrix[s1][s2] * price[s1] * price[s2]
        risk = risk + coefficient * x[i] * x[j]
print(" done")
# Defining Obj: returns
print("Computing return...", end="")
returns = 0
for index, stock in enumerate(stocks):
    returns = returns + avg_monthly_returns[stock] * x[index] * price[stock]
print(" done.")
# Add constraints and Obj to model
# print(risk)
# '''
print("Adding constraints...", end="")
portfolio_model.add_constraint(cost <= budget)
portfolio_model.add_constraint(risk <= max_risk)
portfolio_model.set_objective('max', returns)
print(" done")

print("Solving...", end="")
portfolio_model.solve('quantum', backend='d-wave')
print(" done")
# print(portfolio_model.objective_value)
# print(f"Solution:\n{portfolio_model.print_solution()}")
# '''


