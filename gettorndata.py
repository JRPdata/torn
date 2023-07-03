# Gathers continental US data daily data for July
import requests

# only available from 2004 to 2022 presently
minyear = 4
maxyear = 22
month = 7
monthdays = 31

# Reports found via https://www.spc.noaa.gov/products/archive/

MM = f{"month:02d"}
for year in range(minyear, maxyear+1):
    YY = f"{year:02d}"
    for day in range(1, monthdays+1):
        DD = f"{day:02d}"
        url = f"https://www.spc.noaa.gov/climo/reports/{YY}{MM}{DD}_rpts_torn.csv"
        response = requests.get(url)

        if response.status_code == 200:
            filename = f"report_{YY}07{DD}.csv"
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download: {url}")
