### 🔴 Projekt

# Napisz dla BBC program sprawdzający złożoność artykułów i wpisów, dzięki czemu pracę dziennikarzy będzie można sparametryzować i automatycznie ustalić, czy piszą teksty proste i łatwe w zrozumieniu. Policz jaka jest średnia długość słów i wyświetl rezultat.

# Podpowiedzi:
# text = "Ala ma kota, a Majka ma psa burka srającego na rogu podwórka"
text = input("Wprowadź tekst do analizy: ")

PUNCTUATION = "!#$%&()*+,-./:;<=>?@[\]^_`{|}~`\""

for punc in PUNCTUATION:
    text = text.replace(punc, " ")

print(text)

words = text.lower().split()

print(f'WORDS: {words}')

how_much_words = len(words)

print(f'ILOŚĆ SŁÓW: {how_much_words}')

total_lenght = 0
for word in words:
    lenght = len(word)
    total_lenght += lenght

print(f'ILOŚĆ ZNAKÓW: {total_lenght}')

division = total_lenght / how_much_words
print(f'Średnia długość słów wynosi -> {division}')

# Aby policzyć średnią długość słowa, możesz bazować na liczbie wszystkich znaków oraz liczbie słów.