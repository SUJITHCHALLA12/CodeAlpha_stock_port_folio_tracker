# Stock Portfolio Tracker

A command-line stock portfolio tracker built with Python — a CodeAlpha internship task.

Pick stocks from the built-in price list, enter how many shares you hold, and it prints a per-stock breakdown plus your total investment value.

## Run it

```bash
python "stock portfolio tracker.py"
```

Example session:

```
Available stocks: ['AAPL', 'TSLA', 'GOOGL', 'MSFT']
Enter stock symbol (or 'done' to finish): AAPL
Enter quantity of AAPL: 10
Enter stock symbol (or 'done' to finish): done

📊 Your Stock Portfolio:
AAPL: 10 shares × $180 = $1800

💰 Total Investment Value = $1800
```

## Notes

- Prices are hardcoded in the `stock_prices` dictionary at the top of the script — edit them to track different stocks or update values.
- No libraries needed — pure Python.
