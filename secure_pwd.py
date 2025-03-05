import secrets
import string
import argparse

def strengthen_password(password):
    """
    Renforce un mot de passe en gardant sa structure originale tout en ajoutant des caractères spéciaux, des chiffres
    et en remplaçant certaines lettres par des caractères plus sécurisés.
    """
    # Dictionnaire de remplacement des caractères spéciaux
    replacements = {
        'a': '@', 'A': '@',
        's': '$', 'S': '$',
        'o': '0', 'O': '0',
        'i': '1', 'I': '1',
        'e': '3', 'E': '3',
        't': '7', 'T': '7',
        '!': '1', '"': "'", '#': 'H', '$': 'S', '%': '5', '&': '7',
        "'": "'", '(': 'C', ')': 'C', '*': 'x', '+': 'p', ',': ',', 
        '-': '-', '.': ',', '/': '/', ':': ':', ';': ';', '<': '<', 
        '=': '=', '>': '>', '?': '7', '@': 'a', '[': '{', '\\': '\\', 
        ']': '}', '^': 'v', '_': '-', '`': '~', '{': '(', '|': 'I', 
        '}': ')', '~': '*'
    }

    # Renforcement du mot de passe : remplacement des lettres par des caractères spéciaux ou chiffres
    strengthened_password = ''.join(replacements.get(c, c) for c in password)
    
    # Vérification de la longueur et ajout de caractères spéciaux ou chiffres si nécessaire
    if len(strengthened_password) < 12:
        # Ajouter des caractères aléatoires pour atteindre une longueur minimale de 12 caractères
        while len(strengthened_password) < 12:
            strengthened_password += secrets.choice(string.punctuation + string.digits)
    
    # Vérification de la présence de majuscules, minuscules, chiffres et caractères spéciaux
    if not any(c.isupper() for c in strengthened_password):
        # Si aucune majuscule, on convertit la première lettre en majuscule
        strengthened_password = strengthened_password[0].upper() + strengthened_password[1:]
    
    if not any(c.islower() for c in strengthened_password):
        # Si aucune minuscule, on convertit la première lettre en minuscule
        strengthened_password = strengthened_password[0].lower() + strengthened_password[1:]
    
    if not any(c.isdigit() for c in strengthened_password):
        # Si aucun chiffre, on ajoute un chiffre aléatoire à la fin
        strengthened_password += secrets.choice(string.digits)
    
    if not any(c in string.punctuation for c in strengthened_password):
        # Si aucun caractère spécial, on ajoute un caractère spécial à la fin
        strengthened_password += secrets.choice(string.punctuation)

    return strengthened_password

def main():
    parser = argparse.ArgumentParser(description="Renforceur de mots de passe")
    parser.add_argument("password", type=str, help="Le mot de passe à renforcer")
    
    args = parser.parse_args()
    
    strengthened_password = strengthen_password(args.password)
    # Affichage du mot de passe renforcé
    print(f"[+] Mot de passe renforcé : {strengthened_password}")

if __name__ == "__main__":
    main()

"""
Manuel d'utilisation
Exécution du script
Ouvre ton terminal.
Va dans le dossier où se trouve le script.

Exécute la commande suivante pour renforcer un mot de passe :
Bash
python3 secure_pwd.py "TonMotDePasse"

Exemple
python strengthen_password.py "Password123"

Sortie attendue
Le script renverra un mot de passe renforcé :
[+] Mot de passe renforcé : P@ssw0rd123$





"""
