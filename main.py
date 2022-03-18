import requests
import datetime

code = input('\nEnter country code: ').lower()
url = f'https://corona-stats.online/{code}?format=json'
country_url = 'https://corona-stats.online?format=json'
emoji_url = 'https://cdn.jsdelivr.net/npm/country-flag-emoji-json@2.0.0/dist/by-code.json'

r = requests.get(url)
e = requests.get(emoji_url)

def codesList():
    res = requests.get(country_url)
    json = res.json()
    data = json['data']
    countryCodes = []
    for i in range(len(data)):
        cc = data[i]['countryCode']
        name = data[i]['country']

        if cc == '' or cc == None:
            full = name
        else:
            full = f"{cc} {name}"
        
        countryCodes.append(f"- {full}")

    sortedCodes = sorted(countryCodes)

    for i in range(len(sortedCodes)):
        print(sortedCodes[i])

    print()

if r.status_code != 200 or code == '':
    code = ''
    print('\033[91mInvalid country code.\n\n\033[00mCOUNTRY CODES:\n')
    codesList()
    exit()
else:
    response = r.json()['data'][0]
    cres = r.json()
    eres = e.json()

flag = eres[code.upper()]['emoji']
date = datetime.date.strftime(datetime.date.today(), "%d/%m/%Y")

country = response['country']
cases = response['cases']
todayCases = response['todayCases']
deaths = response['deaths']
todayDeaths = response['todayDeaths']
recovered = response['recovered']
active = response['active']
critical = response['critical']
casesPerOneMillion = response['casesPerOneMillion']

print(f"""
\033[93m{country.upper()}\033[00m SARS-CoV-2 CASES [\033[96m{date}\033[00m]

Country         : {country} {flag}
Total Cases     : {cases}
New Cases ▲     : {todayCases}
Total Deaths    : {deaths}
New Deaths ▲    : {todayDeaths}
Recovered       : {recovered}
Active          : {active}
Critical        : {critical}
Cases / 1M pop  : {casesPerOneMillion}
""")