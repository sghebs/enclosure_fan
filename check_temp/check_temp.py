import serial
import time
import matplotlib.pyplot as plt

# Imposta la porta seriale e il baud rate (deve corrispondere con quelli di Arduino)
port = "/dev/ttyUSB0"  # Modifica con la porta corretta per il tuo sistema (es. COM3 su Windows)
baud_rate = 9600

# Apre la connessione seriale
ser = serial.Serial(port, baud_rate)
time.sleep(2)  # Attendi qualche secondo per l'inizializzazione della connessione seriale

# Variabili per salvare i dati
timestamps = []
temperatures = []

# Loop di acquisizione dati
start_time = time.time()
try:
    while(1):  # ciclo infinito
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()  # Leggi una riga e rimuovi spazi extra
            try:
                temperature = int(data)  # Converti il dato in int
                timestamps.append(int(time.time() - start_time))  # Aggiungi il timestamp
                temperatures.append(temperature)  # Aggiungi la temperatura
                print(f"Temperatura: {temperature}°C")
            except ValueError:
                print("Dati non validi ricevuti!")
        time.sleep(1)  # Aspetta 1 secondo prima della prossima lettura

except KeyboardInterrupt:
    print("Interrotto dall'utente.")

# Chiudi la connessione seriale
ser.close()

# Salva i dati in un file
with open("temperature_data.txt", "w") as f:
    for t, temp in zip(timestamps, temperatures):
        f.write(f"{t},{temp}\n")

# Crea il grafico
plt.plot(timestamps, temperatures, label="Temperatura (°C)")
plt.xlabel('Tempo (secondi)')
plt.ylabel('Temperatura (°C)')
plt.title('Temperatura letta da Arduino')
plt.legend()
plt.grid(True)

# Salva il grafico come immagine
plt.savefig("temperature_graph.png")
plt.show()
