import json
import pandas as pd

def data(filename='data.json'):
    with open(filename,'r') as f:
        return json.load(f)
    
def calculate(data):
    df = pd.DataFrame(data)
    df['price'] = df['price'].str.replace('$','').astype(float)

    avg_price = df['price'].mean()
    avg_rating = df['rating'].astype(float).mean()

    return {
        'total_prod':len(df),
        'avg_price' :avg_price,
        'avg_rating':avg_rating
    }

def display(data):
    df = pd.DataFrame(data)
    print(df.head())

if __name__ == "__main__":
    data = data()
    stats = calculate(data)
    print(stats)