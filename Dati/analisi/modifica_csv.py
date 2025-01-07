import csv
import matplotlib.pyplot as plt

# Leggere il file originale
with open('prova.csv', 'r') as infile:
    reader = csv.reader(infile)
    next(reader)  # Salta l'intestazione
    
    dati = [(int(tempo), float(temp)) for tempo, temp in reader]

# Calcolare la media degli ultimi 5 valori
medie = []
finestra = 5

for i in range(finestra - 1, len(dati)):
    sottoinsieme = dati[i - finestra + 1:i + 1]
    media_temp = sum([temp for _, temp in sottoinsieme]) / finestra
    tempo_finale = sottoinsieme[-1][0]
    medie.append((tempo_finale, round(media_temp, 2)))
    #i += finestra

# Scrivere il nuovo file CSV
with open('medie_prova.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['tempo(s)', 'mediatemp'])  # Intestazione
    
    for tempo, media in medie:
        writer.writerow([tempo, media])

print("File 'medie_temperatura.csv' creato con successo!")

# Creazione del grafico
tempi_originali = [tempo for tempo, _ in dati]
temperature_originali = [temp for _, temp in dati]

tempi_medie = [tempo for tempo, _ in medie]
temperature_medie = [media for _, media in medie]

plt.figure(figsize=(10, 6))
plt.plot(tempi_originali, temperature_originali, label="Temperatura originale (°C)", color='blue')
plt.plot(tempi_medie, temperature_medie, label="Media mobile (°C)", color='red', linestyle='--')
plt.xlabel('Tempo (secondi)')
plt.ylabel('Temperatura (°C)')
plt.title('Temperatura letta da Arduino e Media Mobile')
plt.legend()
plt.grid(True)

# Salva il grafico come immagine
plt.savefig("temperature_graph_m.png")
plt.show()
