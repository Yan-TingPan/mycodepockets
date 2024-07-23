"""
File: webcrawler.py
Name: Cara Pan
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""


import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        # ----- Write your code below this line ----- #
        tbody = soup.find('tbody')
        if tbody:
            male_number = 0
            female_number = 0
            rows = tbody.find_all('tr')
            for row in rows[:200]:  # every sentence
                line = row.find_all('td')
                if len(line) >= 5:  # every word in sentence
                    male_number += int(line[2].text.replace(',', ''))
                    female_number += int(line[4].text.replace(',', ''))
            print(f"Male Number: {male_number}")
            print(f"Female Number: {female_number}")


if __name__ == '__main__':
    main()
