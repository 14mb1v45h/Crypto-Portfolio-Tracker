import requests
import pandas as pd

def track_portfolio(holdings):
    coins = list(holdings.keys())
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(coins)}&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rows = []
        total_value = 0
        for coin in coins:
            if coin in data:
                price = data[coin]['usd']
                amount = holdings[coin]
                value = price * amount
                total_value += value
                rows.append({'Coin': coin.upper(), 'Amount': amount, 'Price (USD)': price, 'Value (USD)': value})
        df = pd.DataFrame(rows)
        print(df.to_string(index=False))
        print(f"\nTotal Portfolio Value: ${total_value:.2f}")
    else:
        print("API request failed.")

if __name__ == "__main__":
    holdings = {'bitcoin': 0.5, 'ethereum': 2, 'solana': 10}  # Edit here
    track_portfolio(holdings)