
# Nulltrace HTTP Security Headers Analyzer

Lekkie narzędzie cybersecurity napisane w Pythonie, służące do analizy nagłówków bezpieczeństwa HTTP oraz identyfikowania brakujących zabezpieczeń.

## O projekcie

Nulltrace HTTP Security Headers Analyzer analizuje nagłówki odpowiedzi HTTP, sprawdza wybrane mechanizmy bezpieczeństwa oraz przedstawia informacje o wykrytych brakach, poziomie ryzyka i zalecanych działaniach. Narzędzie wykorzystuje również ważony system punktacji do oceny konfiguracji analizowanych nagłówków.

## Funkcje

- Analiza nagłówków odpowiedzi HTTP
- Wykrywanie brakujących nagłówków bezpieczeństwa
- Ważony system punktacji bezpieczeństwa
- Klasyfikacja poziomu ryzyka
- Rekomendacje dla wykrytych braków
- Obsługa błędów połączenia i przekroczenia czasu oczekiwania

## Analizowane nagłówki bezpieczeństwa

Narzędzie sprawdza obecność następujących nagłówków HTTP:

- `Content-Security-Policy` — pomaga ograniczać ryzyko ataków XSS i wstrzykiwania niepożądanego kodu
- `Strict-Transport-Security` — wymusza korzystanie z bezpiecznego połączenia HTTPS
- `X-Frame-Options` — pomaga chronić przed atakami typu clickjacking
- `X-Content-Type-Options` — zapobiega interpretowaniu typu zawartości przez przeglądarkę w sposób inny niż zadeklarowany
- `Referrer-Policy` — kontroluje zakres informacji przekazywanych w nagłówku `Referer`
- `Permissions-Policy` — pozwala ograniczać dostęp strony do wybranych funkcji przeglądarki

## Wymagania

Do uruchomienia projektu wymagane są:

- Python 3
- biblioteka `requests`
- połączenie z Internetem

## Instalacja

1. Sklonuj repozytorium:

```bash
git clone https://github.com/TWOJ-USERNAME/nulltrace-http-analyzer.git
cd nulltrace-http-analyzer
python -m pip install -r requirements.txt
## Uruchomienie

Uruchom program za pomocą:

```bash
python main.py
Po uruchomieniu podaj domenę, którą chcesz przeanalizować:

Enter target URL: example.com
Program automatycznie utworzy adres HTTPS, pobierze nagłówki odpowiedzi i przeprowadzi ich analizę bezpieczeństwa.
## Przykładowy wynik

```text
--- SECURITY ANALYSIS ---

[-] Content-Security-Policy: MISSING
    Risk: HIGH
    Issue: Helps mitigate XSS and code injection attacks.
    Recommendation: Implement a restrictive Content-Security-Policy.

[+] Strict-Transport-Security: PRESENT
[+] X-Content-Type-Options: PRESENT

==============================
     NULLTRACE SECURITY SCORE
==============================
Score: 7/12
Security: 58%
Risk level: MEDIUM
==============================
## Interpretacja wyniku

Wynik generowany przez narzędzie dotyczy wyłącznie konfiguracji analizowanych nagłówków bezpieczeństwa HTTP. Nie stanowi pełnej oceny bezpieczeństwa witryny ani potwierdzenia braku innych podatności.

Każdy nagłówek posiada przypisaną wagę zależną od jego znaczenia w przyjętym modelu oceny. Maksymalny wynik wynosi 12 punktów.

## Odpowiedzialne użytkowanie

Narzędzie zostało stworzone w celach edukacyjnych oraz do analizy konfiguracji bezpieczeństwa własnych lub autoryzowanych zasobów.

Nulltrace HTTP Security Headers Analyzer nie wykonuje prób wykorzystania podatności ani ingerencji w analizowany system. Narzędzie analizuje nagłówki zawarte w odpowiedzi HTTP otrzymanej od serwera.