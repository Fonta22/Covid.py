# Covid.py
Command line tool made with **Python** and the [corona-stats](https://corona-stats.online/) public API that shows the **COVID-19** status of any country.

## Usage
Firstable, you'll need to have installed [Python](https://www.python.org/downloads/), which is free.

Then, inside the project's folder you'll have to run the **main Python file**, `main.py`. The program will ask you for the **country code** of the country that you want to get the stats of.

> In case you don't know which is the code of the country you want, here you have a list of the avaiable countries and it's country codes: [CCodes.md](https://github.com/Fonta22/Covid.py/blob/main/docs/CCodes.md)

## Example
Example of the usage of the program.

> Searched for [Poland](https://en.wikipedia.org/wiki/Poland) the day `18/03/2022`.

```powershell
$ python main.py

Enter country code: PL

POLAND SARS-CoV-2 CASES [18/03/2022]

Country         : Poland 🇵🇱
Total Cases     : 5875072
New Cases ▲     : 11660
Total Deaths    : 114087
New Deaths ▲    : 107
Recovered       : 5223340
Active          : 537645
Critical        : 434
Cases / 1M pop  : 155524
```