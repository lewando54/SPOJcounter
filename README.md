# SPOJcounter

Jest to program do zliczania wykonanych zadań na polskim SPOJ'u. 
Działa on na zasadzie Web Scraping'u, czyli metodzie w której program zachowuje się jak użytkownik przeglądarki i pobiera interesujące go dane z witryny.
Wystarczy tylko podać nazwę użytkownika, a program sam zrobi resztę.

## Instalacja pakietów

Aby program działał, należy zainstalować następujące pakiety:
```bash
pip install requests
pip install bs4
```

## Używanie

Program jest bardzo prosty w obsłudze, dlatego jeżeli się go uruchomi, to należy tylko podać nazwę użytkownika. W celu jego uruchomienia należy posiadać Python'a w wersji 3.7.1.

```bash
python SPOJcounter.py
```

## Argumenty

Można programowi przekazać argumenty, aby użyć go np. w połączeniu ze strumieniem plików/danych. Na przykład:

```bash
python SPOJcounter.py --help
```
