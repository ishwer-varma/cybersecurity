import socket
import argparse # Permet d'analyser les arguments de ligne de commande.
from concurrent.futures import ThreadPoolExecutor # Permet d'exécuter des tâches en parallèle pour améliorer les performances.

def get_service_name(port):
    try:
        return socket.getservbyport(port)  # Renvoie le nom du service associé à un port
    except:
        return "Service non identifié" # Si une erreur se produit (pas de service connu), on retourne "Service non identifié"

def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # Crée un socket pour communiquer via IPv4 et TCP
            s.settimeout(1)
            result = s.connect_ex((target, port)) # Tente de se connecter au port du serveur cible
            if result == 0: # Si la connexion est réussie (port ouvert)
                service = get_service_name(port)  # Récupère le nom du service correspondant au port
                print(f"[+] Port {port} est ouvert ({service})") # Affiche que le port est ouvert et son service associé
    except Exception as e: # Si une erreur se produit, on l'affiche
        print(f"[-] Erreur lors du scan des ports {port}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")  # Crée un parser pour les arguments de la ligne de commande
    parser.add_argument("target", help="Cible IP ou domaine") # Argument obligatoire : cible à scanner (IP ou domaine)
    parser.add_argument("--ports", help="Port range", default="1-1024") # Plage de ports à scanner, par défaut 1-1024
    
    args = parser.parse_args() # Récupère les arguments passés en ligne de commande
    target = args.target # L'IP ou le domaine cible
    start_port, end_port = map(int, args.ports.split("-")) # Sépare la plage de ports et la convertit en entiers
    
    print(f"Scan {target} du port {start_port} au port {end_port}...") # Affiche un message de début de scan
    
    with ThreadPoolExecutor(max_workers=50) as executor: # Utilise un pool de threads pour effectuer des scans en parallèle
        for port in range(start_port, end_port + 1): # Pour chaque port dans la plage spécifiée (+1 pour inclure le dernier port)
            executor.submit(scan_port, target, port) # Soumet une tâche de scan pour chaque port
    
    print("[+] Scan terminé!") # Affiche que le scan est terminé

if __name__ == "__main__":
    main() # Exécute la fonction `main` si le script est lancé directement.


'''
Manuel d'utilisation rapide
Ce programme est un scanner de ports simple en Python.

Exécution de base (scanner tous les ports de 1 à 1024) :

Bash
python port_scanner.py <target>
Remplace <target> par l'adresse IP ou le nom de domaine à scanner (ex: 192.168.1.1 ou example.com).
Scanner une plage personnalisée de ports :

Bash
python port_scanner.py <target> --ports <start_port>-<end_port>
Remplace <start_port> et <end_port> par les numéros de ports (ex: 80-1000).
Exemples :
Scanner tous les ports de 1 à 1024 sur 192.168.1.1 :

Bash
python port_scanner.py 192.168.1.1
Scanner les ports de 80 à 443 sur example.com :

Bash
python port_scanner.py example.com --ports 80-443
Le programme affiche les ports ouverts et les services associés.

'''