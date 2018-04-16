import pandas as pd
df = pd.read_csv('DailyStock.csv')
df['Sector'].unique()
df['Sector'].nunique()
df['Industry'].unique()
df['Industry'].nunique()

ds = df[df['Industry'] != 'n/a']
# print(ds)
# remove all data with 'n/a' in Industry

stockSymbol = input('Enter a Stock Symbol: ')
# print(stockSymbol)


def recommend(stockSymbol, industry):
    if stockSymbol == industry:
        return True
    else:
        return False


if stockSymbol in ds['Symbol']:
    print('stockSymbol not in Data Set.')
else:
    print('You have entered', stockSymbol)
    target_Industry = ds.loc[ds.Symbol == stockSymbol, 'Industry'].values[0]
    print("Since you're interested in ", ds[ds['Symbol'] == stockSymbol]['Name'].item(),
          "industry, we recommend the following stocks:")
    ds_industry_match = ds[ds['Industry'] == target_Industry]

    print(ds_industry_match)
