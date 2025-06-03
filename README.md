# ☕ Coffee Machine Simulator

This is a simple command-line coffee machine built with Python. It simulates a real-world coffee vending machine where users can:
- Choose a drink (espresso, latte, or cappuccino)
- Insert virtual coins
- Receive a coffee if resources and funds are sufficient

## 🧠 Key Features

- Menu-driven interaction
- Tracks inventory of water, milk, and coffee
- Accepts virtual coins (pennies, nickles, dimes, quarters)
- Calculates change and profit
- Provides a status report of current resources
- Option to shut down the machine

## 🚀 How It Works

1. The user is prompted to choose a drink or request a report.
2. The machine checks if there are enough ingredients.
3. If sufficient, it requests coin input.
4. Calculates whether the payment is enough.
5. Dispenses coffee, updates resources and profit.

## 📋 Example Usage

```bash
What would you like? (espresso/latte/cappuccino): latte
Enter the money income: Pennies: 10
Enter the money income: Nickles: 10
Enter the money income: Dimes: 10
Enter the money income: Quarters: 10
Here is the change $0.25
Here is your coffee latte
