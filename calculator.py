# ETH MEXC Futures Position Size Calculator

def calculate_position(account_balance, risk_percent, entry_price, stop_loss_price, leverage=20):
    risk_amount = account_balance * (risk_percent / 100)
    price_diff = abs(entry_price - stop_loss_price)
    
    if price_diff == 0:
        return "Error: Stop Loss cannot be same as Entry"
    
    stop_distance_percent = (price_diff / entry_price) * 100
    position_usdt = risk_amount / (price_diff / entry_price)
    quantity_eth = position_usdt / entry_price
    margin_usdt = position_usdt / leverage
    max_quantity = (account_balance * leverage) / entry_price
    
    print("=== ETH MEXC Futures Position Calculator ===")
    print(f"Account Balance     : ${account_balance:,.2f}")
    print(f"Risk %              : {risk_percent}% (${risk_amount:,.2f})")
    print(f"Entry Price         : ${entry_price:,.2f}")
    print(f"Stop Loss           : ${stop_loss_price:,.2f}")
    print(f"Stop Distance       : {stop_distance_percent:.2f}%")
    print(f"Leverage            : {leverage}x")
    print("---------------------------------------------")
    print(f"Position Size (USDT): ${position_usdt:,.2f}")
    print(f"Quantity (ETH)      : {quantity_eth:.4f} ETH")
    print(f"Required Margin     : ${margin_usdt:,.2f} USDT")
    print(f"Max Possible        : {max_quantity:.4f} ETH")
    print("---------------------------------------------")
    print("✅ Max 1% risk | Always use SL | Check Funding Rate")

# টেস্ট করার জন্য
if __name__ == "__main__":
    calculate_position(1000, 1, 2500, 2450, 20)
