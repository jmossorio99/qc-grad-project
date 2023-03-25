import pandas as pd


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


def get_data(budget):
    data = pd.read_csv('data/stock_data.csv')
    refactored_df = pd.DataFrame()
    refactored_df['Period'] = data['date'].unique()
    column_list = data['Name'].unique()
    refactored_df = set_columns(data, refactored_df, column_list)
    refactored_df.set_index('Period', inplace=True)
    print(refactored_df)
    max_num_shares = (budget / refactored_df.iloc[-1]).astype(int)


get_data(1000)
