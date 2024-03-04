import csv
import requests
import csv

print("!!!!!!!!!!!!!!!!!!!!!Renommer les AP Aruba gérer par Central!!!!!!!!!!!!")
print("De Kamal.ait-hammou@cpu.ca")
# Demander à l'utilisateur d'entrer l'URL de base et le jeton d'authentification
base_url = input("Veuillez entrer l'URL de base exemple pour Canada https://apigw-ca.central.arubanetworks.com : ")
token = input("Veuillez entrer votre jeton d'authentification : ")

# Les headers restent les mêmes
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": f"Bearer {token}"
}
time.sleep(5)
# Lecture à partir du fichier CSV
with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        serial, ip_address, hostname = row
        
        # Construction de l'URL avec le numéro de série
        url = f"{base_url}/configuration/v1/ap_settings/{serial}"
        
        # Construction du payload
        payload = {
            "hostname": hostname,
            "ip_address": ip_address
        }
        
        # Envoi de la requête POST
        response = requests.post(url, json=payload, headers=headers)
        print(f"Data for {hostname} sent. Response: {response.text}")