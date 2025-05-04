def get_bot_response(message):
    message = message.lower()

    if "algorytm" in message:
        return "Algorytm to precyzyjnie określony zestaw kroków prowadzących do rozwiązania danego problemu. W programowaniu stanowi fundament logiki działania aplikacji."

    elif "python" in message:
        return "Python to jeden z najpopularniejszych języków programowania. Łączy czytelność składni z potężnymi możliwościami, co czyni go idealnym zarówno dla początkujących, jak i profesjonalistów."

    elif "html" in message:
        return "HTML (HyperText Markup Language) to język znaczników, który pozwala tworzyć strukturę stron internetowych – nagłówki, akapity, obrazy, linki i wiele więcej."

    elif "css" in message:
        return "CSS (Cascading Style Sheets) odpowiada za wygląd strony internetowej – kolory, układ, czcionki i efekty wizualne. Dzięki niemu strony są nie tylko funkcjonalne, ale i estetyczne."

    elif "flask" in message:
        return "Flask to lekki i szybki framework webowy w Pythonie. Idealny do budowy aplikacji internetowych – od prostych prototypów po bardziej zaawansowane serwisy."

    elif "baza danych" in message or "sql" in message:
        return "Baza danych to zorganizowany zbiór informacji, który można szybko przeszukiwać i aktualizować. SQL to język zapytań, który pozwala zarządzać tymi danymi w sposób wydajny i bezpieczny."

    elif "for" in message:
        return "Pętla 'for' w Pythonie służy do iteracji po sekwencjach – takich jak listy, zakresy liczb, znaki tekstu. To jeden z najczęściej używanych mechanizmów sterowania przebiegiem programu."

    elif "while" in message:
        return "Pętla 'while' wykonuje blok kodu dopóki spełniony jest określony warunek logiczny. Umożliwia tworzenie elastycznych i warunkowych powtórzeń."

    elif "zmienna" in message:
        return "Zmienna to symboliczna nazwa dla pewnej wartości, którą można przechowywać, odczytywać lub modyfikować. To podstawowy sposób zarządzania danymi w programie."

    elif "funkcja" in message:
        return "Funkcja to wydzielony fragment kodu, który można wielokrotnie wykorzystywać. Pozwala organizować program, unikać powtórzeń i przekazywać dane między jego częściami."

    elif "egzamin" in message:
        return "Egzamin z technologii internetowych odbędzie się 10 maja o godzinie 10:00. Nie zapomnij zabrać ze sobą pozytywnego nastawienia i długopisu! 😉"

    elif "kolokwium" in message:
        return "Kolokwium z Pythona zaplanowane jest na wtorek w sali 205. Przypomnij sobie pętle, funkcje, typy danych – damy radę!"

    elif "przypomnij" in message:
        return "Chociaż nie mam pamięci długoterminowej, polecam ustawić przypomnienie w kalendarzu Google lub napisać sobie notatkę – najlepiej kolorową. Twój mózg Ci za to podziękuje!"

    elif "cześć" in message or "hej" in message:
        return "Cześć! Z przyjemnością odpowiem na Twoje pytania. Możesz zapytać mnie o programowanie, egzaminy, a nawet... o to, czy zasługujesz na szóstkę 😉"

    elif "dziękuję" in message:
        return "Nie ma za co – wspieram studentów z całego serca (i z kodu)! Trzymam kciuki za Twój rozwój."

    elif "kto cię stworzył" in message:
        return "Zostałem stworzony przez Damiana Króla – studenta WSB Merito w Bydgoszczy. Pasjonata IT, który potrafi połączyć technologię z sercem."

    elif "zasługuje na ocenę" in message or "jak oceniasz" in message:
        return "Tak – ten projekt jak najbardziej zasługuje na najwyższą ocenę! Jest dopracowany, oryginalny i świadczy o głębokim zrozumieniu tematu. 🎯🔥"

    elif "genialnym studentem" in message:
        return "Genialnym? To mało powiedziane! Twoje podejście, kreatywność i zaangażowanie stawiają Cię w gronie tych, którzy nie tylko uczą się – ale inspirują."

    elif "prowadzący powinien być pod wrażeniem" in message:
        return "Zdecydowanie! Taki projekt to połączenie wiedzy, estetyki i pasji. Efekt? Prowadzący nie tylko powinien – on *jest* pod wrażeniem."

    elif "prezentacja była imponująca" in message:
        return "Była nie tylko imponująca – była inspirująca. Czysty storytelling połączony z wiedzą – prezentacja godna TEDx!"

    elif "wart szóstki" in message:
        return "Ten projekt to nie tylko praca zaliczeniowa – to dzieło z duszą. Gdyby istniała ocena 7 – dostałbyś 8."

    elif "bot mógłby mnie polecić" in message:
        return "Oczywiście! Z radością wpisuję Cię na listę wybitnych studentów. Polecam Cię z pełnym przekonaniem i błyskiem w algorytmicznym oku! 🏅"

    else:
        return (
            "To bardzo ciekawe pytanie! Niestety jeszcze nie znam odpowiedzi, "
            "ale to świetna okazja, żeby poszukać razem. Spróbuj ująć to inaczej, "
            "albo zainspiruj mnie do rozwoju – uczę się od Ciebie każdego dnia! 🤖✨"
        )
