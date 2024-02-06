import matplotlib.pyplot as plt

# Define the variables
initial_investment = 10000  # Initial amount (e.g., $10,000)
annual_interest_rate = 0.05  # Annual interest rate (e.g., 5%)
years = 30  # Number of years

# Calculate compound interest
amounts = [initial_investment]
for year in range(1, years + 1):
  last_year = amounts[-1]
  new_amount = last_year + last_year * annual_interest_rate
  amounts.append(new_amount)

# Visualization

plt.figure(figsize=(10, 6))
# plt.plot(range(years + 1), amounts)
plt.plot(range(years + 1), amounts, marker='o')
# plt.bar(range(years + 1), amounts)

plt.title('Compound Interest Over Time')
plt.xlabel('Years')
plt.xticks(rotation=90)
plt.ylabel('Amount ($)')
plt.grid(True)
plt.show()

