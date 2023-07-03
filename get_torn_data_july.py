import requests

for year in range(4, 23):
    YY = f"{year:02d}"
    for day in range(1, 32):
        DD = f"{day:02d}"
        url = f"https://www.spc.noaa.gov/climo/reports/{YY}07{DD}_rpts_torn.csv"
        response = requests.get(url)

        if response.status_code == 200:
            filename = f"report_{YY}07{DD}.csv"
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download: {url}")
