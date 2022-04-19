# SPOJcounter

###### English
It is a program for counting how many exercises you've done on polish SPOJ.
The program works based on web-scraping - a method in which the program acts like a web browser, but instead of showing the web page, it's data is written to a variable, to later make use of it. You only need to provide a username, and the program will do the rest.

## Installing dependencies

In order for program to work, you need to install these packages:
```bash
pip install requests
pip install bs4
```

and have Python 3.7.1 installed.

## Usage

SPOJCounter is very easy to use, so if you run it, you only need to type desired username.

In order to run it, type:
```bash
python SPOJcounter.py
```

## Arguments

You can pass arguments to the program. For example you can use it with data streams to save your score to a text file.

```bash
python SPOJcounter.py --help
```

###### Polski
Jest to program do zliczania wykonanych zadań na polskim SPOJ'u. 
Działa on na zasadzie Web Scraping'u, czyli metodzie w której program zachowuje się jak użytkownik przeglądarki i pobiera interesujące go dane z witryny.
Wystarczy tylko podać nazwę użytkownika, a program sam zrobi resztę.

## Instalacja pakietów

Aby program uruchamiany przy pomocy Pythona działał, należy zainstalować następujące pakiety:
```bash
pip install requests
pip install bs4
```
oraz należy posiadać Python'a w wersji 3.7.1.

## Używanie

Program jest bardzo prosty w obsłudze, dlatego jeżeli się go uruchomi, to należy tylko podać nazwę użytkownika.

W celu uruchomienia piszemy:
```bash
python SPOJcounter.py
```

## Argumenty

Można programowi przekazać argumenty, aby użyć go np. w połączeniu ze strumieniem plików/danych. Na przykład:

```bash
python SPOJcounter.py --help
```
