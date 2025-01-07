import csv

# Leggi il file CSV originale
with open('medie_prova.csv', 'r') as infile:
    reader = csv.reader(infile)
    
    # Stampa le prime 5 righe
    for i, row in enumerate(reader):
        if i < 5:
            print(row)
        else:
            break
