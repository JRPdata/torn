import json
import numpy as np
# 249 tornados for june 2023, 4 days of no tornados (from csv gathered for last month)
june_tornado_count = 249
# data from torn_count_july.py
months_sums = [138, 123, 68, 50, 120, 134, 173, 100, 30, 63, 99, 133, 111, 93, 111, 114, 129, 178, 89]
months_zeros = [9, 6, 9, 9, 8, 5, 4, 9, 16, 10, 14, 6, 7, 8, 8, 8, 10, 9, 13]

firstmonth = 'torn-june.json'
secondmonth = 'torn-july.json'

def predict_linear(predict, x, y):
    # Perform linear regression
    slope, intercept = np.polyfit(x, y, 1)

    # Calculate the expected value using the linear fit equation
    predicted = slope * predict + intercept
    return predicted

def extract_tornado_counts(json_data):
    tornado_counts = []

    for year, count in sorted(json_data["tornadoes"].items()):
        tornado_counts.append(int(count))

    return tornado_counts

# Load the first JSON file
with open(firstmonth) as file:
    first_month_data = json.load(file)

# Extract tornado counts for the first month
first_month_tornado_counts = extract_tornado_counts(first_month_data)

# Load the second JSON file
with open(secondmonth) as file:
    second_month_data = json.load(file)

# Extract tornado counts for the second month
second_month_tornado_counts = extract_tornado_counts(second_month_data)

# Print the tornado counts for each month
print("First month tornado counts (US):", first_month_tornado_counts)
print("Second month tornado counts (US):", second_month_tornado_counts)

from scipy.stats import pearsonr

# Calculate the Pearson correlation coefficient and p-value
correlation_coefficient, p_value = pearsonr(first_month_tornado_counts, second_month_tornado_counts)

# Print the correlation coefficient and p-value
print("Correlation coefficient (between June and July):", correlation_coefficient)
print("P-value:", p_value)

#july_tornado_est = int(round(correlation_coefficient * june_tornado_count))
july_tornado_est = int(round(predict_linear(june_tornado_count, first_month_tornado_counts, second_month_tornado_counts)))
print(f"Estimated number of tornadoes in July (US), (from June count of {june_tornado_count}): {july_tornado_est}")

correlation_coefficient, p_value = pearsonr(months_sums, months_zeros)
print("Correlation coefficient (between July total tornados each month and July number of days with zero tornados):", correlation_coefficient)
print("P-value:", p_value)
july_zero_tornado_days_est = int(round(predict_linear(july_tornado_est, months_sums, months_zeros)))
print(f"Number of zero days of tornados estimated for July (US): {july_zero_tornado_days_est}")

# Bad science: US has 75% of tornados globally every year so multiply by 1/0.75 to get number of tornado days globablly
july_zero_tornado_days_est = int(round(predict_linear(july_tornado_est/0.75, months_sums, months_zeros)))
print(f"Number of zero days of tornados estimated for July (globally): {july_zero_tornado_days_est}")
