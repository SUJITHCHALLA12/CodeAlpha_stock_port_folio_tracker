stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "MSFT": 300
}

portfolio = {}
total_investment = 0

print("Available stocks:", list(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("❌ Stock not found. Try again.")
        continue
    
    qty = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + qty

print("\n📊 Your Stock Portfolio:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_investment += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print(f"\n💰 Total Investment Value = ${total_investment}")