### 馃敶 Projekt

# Napisz dla BBC program sprawdzaj膮cy z艂o偶ono艣膰 artyku艂贸w i wpis贸w, dzi臋ki czemu prac臋 dziennikarzy b臋dzie mo偶na sparametryzowa膰 i automatycznie ustali膰, czy pisz膮 teksty proste i 艂atwe w zrozumieniu. Policz jaka jest 艣rednia d艂ugo艣膰 s艂贸w i wy艣wietl rezultat.

# Podpowiedzi:
# text = "Ala ma kota, a Majka ma psa burka sraj膮cego na rogu podw贸rka"
text = input("Wprowad藕 tekst do analizy: ")

PUNCTUATION = "!#$%&()*+,-./:;<=>?@[\]^_`{|}~`\""

for punc in PUNCTUATION:
    text = text.replace(punc, " ")

print(text)

words = text.lower().split()

print(f'WORDS: {words}')

how_much_words = len(words)

print(f'ILO艢膯 S艁脫W: {how_much_words}')

total_lenght = 0
for word in words:
    lenght = len(word)
    total_lenght += lenght

print(f'ILO艢膯 ZNAK脫W: {total_lenght}')

division = total_lenght / how_much_words
print(f'艢rednia d艂ugo艣膰 s艂贸w wynosi -> {division}')

# Aby policzy膰 艣redni膮 d艂ugo艣膰 s艂owa, mo偶esz bazowa膰 na liczbie wszystkich znak贸w oraz liczbie s艂贸w.