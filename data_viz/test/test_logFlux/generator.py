import time
import datetime

def simulate_logs(filename="log.txt"):
    print(f"Début de la génération de logs dans {filename}...")
    print("Appuyez sur Ctrl+C pour arrêter.")
    
    count = 1
    while True:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"LOG #{count} - État du système : OK - CPU: {count % 100}%"
        
        # 'a' pour append (ajouter à la fin)
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {message}\n")
            # flush est crucial pour que les données soient écrites 
            # immédiatement sans attendre que le cache soit plein
            f.flush() 
        
        print(f"Ligne ajoutée : {message}")
        count += 1
        
        # Pause de 5 secondes
        time.sleep(5)

if __name__ == "__main__":
    simulate_logs()