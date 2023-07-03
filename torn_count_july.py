# Tornado statistics for contintental U.S.=
# data gathered with gettorndata.py

import os
import numpy as np
def calculate_statistics(data):
    median = np.median(data)
    mean = np.mean(data)
    maximum = np.max(data)
    minimum = np.min(data)

    return median, mean, maximum, minimum

def process_files(directory):
    count = {}

    # Loop through files in the directory
    sortedfiles = sorted(os.listdir(directory))
    for filename in sortedfiles:
        if filename.endswith(".csv") and filename.startswith("report_"):
            # Extract YY and DD from the filename
            YY = filename[7:9]
            DD = filename[11:13]

            # Initialize the count dictionary if necessary
            if YY not in count:
                count[YY] = {}

            # Count the number of lines in the file
            with open(os.path.join(directory, filename), 'r') as file:
                lines = file.readlines()
                line_count = len(lines) - 1  # Subtract 1 to exclude the header line

            # Store the result in the count dictionary
            count[YY][DD] = line_count

    # Calculate the sums
    all_zero_days_ratio_str = []
    all_zero_days_ratio_float = []
    months_sums = []
    months_zeros = []

    for YY, DD_dict in count.items():
        total_sum = 0
        zero_count_sum = 0
        month_sum = 0
        for DD, value in DD_dict.items():
            month_sum += value
            total_sum += value
            if value == 0:
                zero_count_sum += 1
        months_sums.append(month_sum)
        months_zeros.append(zero_count_sum)
        # Print the sums
        zero_days_ratio = zero_count_sum / total_sum
        print(f"July{YY}:")
        print("Total sum:", total_sum)
        print("Zero count sum:", zero_count_sum)
        print("Proportion of zero tornado day:", zero_days_ratio)
        print("----------------------------------")
        all_zero_days_ratio_str.append(str(round(zero_days_ratio,3)))
        all_zero_days_ratio_float.append(zero_days_ratio)

    print("Proportion of zero tornado days (July) for all gathered years (scale is 0 to 1):")
    print(",".join(all_zero_days_ratio_str))
    median, mean, maximum, minimum = calculate_statistics(all_zero_days_ratio_float)
    print("Statistics of number of zero days for July for all gathered years (normalized to 31 days):")
    print("Median:", round(median*31,3))
    print("Mean:", round(mean*31,3))
    print("Maximum:", round(maximum*31,3))
    print("Minimum:", round(minimum*31,3))

    print("Total tornadoes for each Month:")
    print(f"months_sums = {months_sums}")
    print("Total number of zero days for each Month:")
    print(f"months_zeros = {months_zeros}")


# Usage
directory = "july2004-2022"
process_files(directory)
