# coding=UTF-8
import requests
from bs4 import BeautifulSoup
import sys

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'} 
if len(sys.argv) - 1 == 1 and sys.argv[1] == "--help":
    print("Składnia: SPOJcounter.py <użytkownik> -t\n\nOpcja    Działanie\n-t       Wyświetli listę nazw wykonanych zadań bez komunikatu z pytaniem (opcjonalnie)")
else:
    def zapytanie(fail):
        if len(sys.argv) - 1 == 1 and sys.argv[1] == "-t" or fail == True:
            user = input("Podaj nazwę użytkownika\n")
        elif len(sys.argv) - 1 == 0:
            user = input("Podaj nazwę użytkownika\n")
        elif len(sys.argv) - 1 == 2 and sys.argv[2] != "-t":
            user = sys.argv[2]
        else:
            user = sys.argv[1]
        try:
            page = requests.get("https://pl.spoj.com/users/"+user+"/")
        except:
            print("Sprawdź połączenie internetowe!")
            exit()
        global soup
        soup = BeautifulSoup(page.content, 'html.parser')
        global test
        test = soup.find('h3', {'class':['top-4','text-center']})

    zapytanie(False)

    while test == None:
        print("Ten użytkownik nie istnieje! Spróbuj ponownie.")
        zapytanie(True)
    table = soup.find_all('table')[1]
    rows = table.find_all('tr')
    zadania = []
    ilosc = 0
    for tr in rows:
        td = tr.find_all('td')
        for i in td:
            ilosc = ilosc + 1
            zadania.append(i.text)
            
    print("Zrobiłeś", ilosc, "zadań na SPOJ'u")

    if len(sys.argv) - 1 == 1 and sys.argv[1] != "-t":
        pytanie = input("Czy chcesz wyświetlić ich nazwy? (t/n)\n")
    elif len(sys.argv) - 1 == 2 and sys.argv[2] == "-t":
       pytanie = "t"
    elif len(sys.argv) - 1 == 0:
        pytanie = input("Czy chcesz wyświetlić ich nazwy? (t/n)\n")
    else:
        pytanie = "t"
    if pytanie == "t":
        print("Oto ich nazwy:")
        for x in zadania:
            print(x, end=", ")

