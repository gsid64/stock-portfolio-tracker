import csv

# define hardcoded stock prices

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "AMZN": 3300,
    "GOOGL": 2800,
    "MSFT": 300
}

def stock_portfolio_tracker():
   
    #initialize portfolio dictionary and total value
    
    portfolio_data = []
    total_value = 0

    # gather user input
   
    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock == 'DONE':
            break
        if stock not in stock_prices:
            print("Stock not found. Available stocks:", ', '.join(stock_prices.keys()))
            continue
        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
            if quantity <= 0:
                raise ValueError("Quantity must be positive.")
        except ValueError as e:
            print(f"Invalid input: {e}")
            continue

        price = stock_prices[stock]
        value = quantity * price
        total_value += value
        portfolio_data.append({'Stock': stock, 'Quantity': quantity, 'Price': price, 'Value': value})

   
    # display portfolio summary
    
    print("\nPortfolio Summary:")
    print("{:<10} {:<10} {:<10} {:<10}".format("Stock", "Quantity", "Price", "Value"))
    for item in portfolio_data:
        print("{:<10} {:<10} ₹{:<9} ₹{:<10}".format(
            item['Stock'], item['Quantity'], item['Price'], item['Value']
        ))

    print(f"\nTotal Investment Value:₹{total_value:.2f}")

    #optional file saving
    
    save = input("Do you want to save the result to a file? (yes/no): ").lower()
    if save == 'yes':
        filename = input("Enter filename (with .txt or .csv extension): ").strip()
        if filename.endswith(".txt"):
            with open(filename, "w") as f:
                f.write("Stock\tQuantity\tPrice\tValue\n")
                for item in portfolio_data:
                    f.write(f"{item['Stock']}\t{item['Quantity']}\t₹{item['Price']}\t₹{item['Value']}\n")
                f.write(f"\nTotal Investment Value: ₹{total_value:.2f}")
        elif filename.endswith(".csv"):
            with open(filename, "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Stock", "Quantity", "Price", "Value"])
                for item in portfolio_data:
                    writer.writerow([item['Stock'], item['Quantity'], item['Price'], item['Value']])
                writer.writerow([])
                writer.writerow(["Total", "", "", total_value])
        else:
            print("Invalid file type. Please use .txt or .csv")

#run the Portfolio Tracker
stock_portfolio_tracker()