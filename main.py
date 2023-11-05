oryg = open("73523925.txt", 'r')
manu = open("73523925-manual.txt", 'r')

orygStr = oryg.read()
manuStr = manu.read()

oryg.close()
manu.close()

oryginalPociety = orygStr.split(' ')
manualniePociety = manuStr.split(' ')

print("Pierwsza kolejka, sprawdzam ilość przekleństw i porównuje z manualnie poprawionym testem")
print()

i = 0
for word in oryginalPociety:
    if "#!$%@?" in word:
        print("Przekleństwo w słowie " + str(i) + "\t- " + ' '.join(oryginalPociety[i-1:i+2]) + "\t\t- " + ' '.join(manualniePociety[i-1:i+2]))

        # logika
        ## wkurwia
        if oryginalPociety[i][-2:] == "ło":
            oryginalPociety[i] = word.replace("#!$%@?", "wkurwia")
        ## chuja
        elif oryginalPociety[i-1] == "w" and oryginalPociety[i+1] == "wali":
            oryginalPociety[i] = word.replace("#!$%@?", "chuja")
        ## napierdala
        elif ' '.join(oryginalPociety[i-2:i+2]) == "wyciąga i #!$%@? jakby":
            oryginalPociety[i] = word.replace("#!$%@?", "napierdala")
        elif ' '.join(oryginalPociety[i-1:i+2]) == "stary #!$%@? puka":
            oryginalPociety[i] = word.replace("#!$%@?", "napierdala")
        ## obsrane
        elif ' '.join(oryginalPociety[i-2:i+1]) == "dupsko całe #!$%@?":
            oryginalPociety[i] = word.replace("#!$%@?", "obsrane")
        ## pojebany
        elif ' '.join(oryginalPociety[i-1:i+2]) == "był #!$%@? jak":
            oryginalPociety[i] = word.replace("#!$%@?", "pojebany")
        ## kurwa - wartość standardowa
        else:
            oryginalPociety[i] = word.replace("#!$%@?", "kurwa")
    i += 1

# Przetestuj
print()
print("Testuje logikę zamiany znaczków na słowa")
print()

i = 0
nbledow = 0
for word in oryginalPociety:
    if word != manualniePociety[i]:
        print("Słowo się nie zgadza!: " + ' '.join(oryginalPociety[i-2:i+2]) + " - " + ' '.join(manualniePociety[i-2:i+2]))
        nbledow += 1
    i += 1

if nbledow == 0:
    print("Nie znaleziono różnic między poprawkami wprowadzonymi przez skrypt, a manualnie poprawionym tekstem!")
else:
    print("Znaleziono " + str(nbledow) + " różnic")

expo = open("73523925-export.txt", "w")
expo.write(' '.join(oryginalPociety))
expo.close()
