# 1. Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3500,
    "MSFT": 330
}

# 2. Get user input
portfolio = {}
while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("❌ Stock not found in price list. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("❌ Please enter a valid number.")

# 3. Calculate total investment
total_value = 0
result_lines = []
print("\n📊 Investment Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = qty * price
    total_value += investment
    line = f"{stock}: {qty} shares × ₹{price} = ₹{investment}"
    print(line)
    result_lines.append(line)

print(f"\n💰 Total Investment Value: ₹{total_value}")

# 4. Save to file (optional)
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()
if save == 'yes':
    with open("stock_portfolio.txt", "w") as file:
        file.write("📊 Investment Summary:\n")
        for line in result_lines:
            file.write(line + "\n")
        file.write(f"\n💰 Total Investment Value: ₹{total_value}\n")
    print("✅ Saved to 'stock_portfolio.txt'")