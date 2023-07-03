# torn
Attempts to predict the number of days for a month (July) with zero tornados.
Uses tornado counts from historical data to analyze correlations between successive months (June and July)
This is checked against ```torn_count_july.py```.
Predicts the US tornado count for July 2023 and number of zero days of July given June 2023 tornado count and number of days with zero hurricanes.
From the US prediction of tornados for July, estimates (very poorly) the global numbers for tornados and zero days using US statistics (this is as best as I can do).

The necessary data is already gathered in repos for predicting July 2023. There is also a script for gathering the daily data for a month for a year range from NOAA.

# Run for July 2023

```
> torn_count_july.py
Proportion of zero tornado days (July) for all gathered years (scale is 0 to 1):
0.065,0.049,0.132,0.18,0.067,0.037,0.023,0.09,0.533,0.159,0.141,0.045,0.063,0.086,0.072,0.07,0.078,0.051,0.146
Statistics of number of zero days for July for all gathered years (normalized to 31 days):
Median: 9.0
Mean: 8.842
Maximum: 16
Minimum: 4
70% Confidence Interval: [ 6.  10.9]
Total tornadoes for each Month:
months_sums = [138, 123, 68, 50, 120, 134, 173, 100, 30, 63, 99, 133, 111, 93, 111, 114, 129, 178, 89]
Total number of zero days for each Month:
months_zeros = [9, 6, 9, 9, 8, 5, 4, 9, 16, 10, 14, 6, 7, 8, 8, 8, 10, 9, 13]
```

This predicts about 9 days of no tornados in the contintental US for July 2023 just using historical data from July (2004-2022).

```
> python3 tornado-corr-june-july.py 
First month tornado counts (US): [28, 76, 34, 111, 107, 153, 65, 147, 128, 73, 125, 107, 170, 90, 137, 147, 126, 210, 136, 137, 134, 198, 113, 224, 194, 196, 169, 132, 148, 150, 217, 223, 196, 178, 243, 82, 134, 132, 63, 252, 334, 216, 400, 313, 236, 216, 128, 193, 379, 289, 136, 248, 97, 292, 266, 316, 119, 128, 292, 270, 324, 160, 111, 124, 286, 184, 86, 146, 155, 177, 91, 105, 123]
Second month tornado counts (US): [23, 23, 27, 32, 45, 49, 92, 55, 121, 62, 42, 77, 78, 62, 63, 85, 100, 90, 56, 98, 81, 100, 115, 80, 59, 79, 84, 100, 143, 132, 95, 98, 95, 99, 72, 51, 89, 163, 103, 59, 106, 64, 213, 242, 155, 163, 201, 188, 82, 99, 148, 120, 68, 167, 124, 137, 71, 69, 95, 118, 146, 103, 37, 72, 85, 115, 108, 81, 92, 101, 99, 126, 64]
Correlation coefficient (between June and July): 0.48256837062085617
P-value: 1.5353866232364318e-05
Estimated number of tornadoes in July (US), (from June count of 249): 116
Correlation coefficient (between July total tornados each month and July number of days with zero tornados): -0.6164601184338939
P-value: 0.004939946299257071
Number of zero days of tornados estimated for July (US): 8
Number of zero days of tornados estimated for July (globally): 7
```

This estimates 8 days of no tornados in the contintental US for July 2023 by using a linear prediction on the previous month's (June 2023) tornado data.
This estimate falls within the historical data prediction for July.
Using the same linear model for global tornados and using the number of 75% for the number of tornados of globally that happen in the US, we calculate the number of tornados and zero days from the previous prediction's tornado count for July 2023 (US).

This estimates there will be 7 days (globally) in July 2023 without tornados.

Calculating the probability there will be at least one tornado: ```100*(1 - (7 / 31)) ~= 77.41 %```

For reference, the question at https://manifold.markets/DerekHarris/will-there-be-a-tornado-reported-an-d47157388841?r=cGFyaGl6ag has a % presently at ~80% at July 3, 2023 (2023-07-03T17:52:22Z); this corresponds to ```(1-0.8)*31 ~= 6.2 days``` of no tornados.
