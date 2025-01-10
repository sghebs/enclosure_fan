import csv

# Leggi il file CSV originale
with open('prova.csv', 'r') as infile:
    reader = csv.reader(infile)
    next(reader)
    dati = [(int(tempo), float(temp)) for tempo, temp in reader]

    
    # Stampa le prime 5 righe
    i = 0
    sum = 0
    while i < len(dati):
        for j in range(5):
            if i < len(dati):
            #print(dati[i])
                sum += dati[i][1]
                i += 1
            else: 
                sum = sum / (j)
                break
        if i < len(dati): sum = sum / 5

        print(dati[i-1][0], sum)
        sum = 0
                
        

