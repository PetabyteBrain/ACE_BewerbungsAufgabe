# AUFGABEN

Ein API entwickeln das die Voraussetzungen erfüllt.

URL zur Lösung: [https://ace.catechis.ch](https://ace.catechis.ch)

## 1 /temp

### Anfrage:
```bash
curl https://ace.catechis.ch/api/temp?celsius=25
```

### Aufgabe der route:

Es soll Temperaturen von Kelvin zu Celsius umberechnen und von Celsius zu Kelvin.

### weg zur lösung:

- kelvin = celsius + 273.15

- celsius = kelvin - 273.15

## 2 /prime

### Anfrage:
```bash
curl https://ace.catechis.ch/api/prime?limit=10
```

### Aufgabe der route:

Die API route soll alle Primzahlen angeben bis zur gegebene Limit, max ist 10'000.

### weg zur lösung:

Sieb des Eratosthenes

## 3 /numbers

### Anfrage:
```bash
curl https://ace.catechis.ch/api/number?n=45
```

### Aufgabe der route:

Herausfinden wie die Zahlen berechnet werden und diese als API nachproduzieren.

### weg zur lösung:

Es handelt sich um die Fibonacci Sequenz, es werden immer die letzen zwei zahlen der Sequenz zusammen summiert um die nächste zahl zu erstellen.


## Hosting

Das Hosting ist durch meinen eigenen kleinen Ubuntu Server verbracht und läuft mit einen einfachen Dockerfile, Docker-compose skript und Caddy als Reverse-Proxy.