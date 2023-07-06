import nmap
import ipaddress
import platform
import socket
import subprocess
import json
from netaddr import IPAddress
from scripts.scan_intense import active_scan

def recon(request, mydb, domain, id_client):

    system = platform.system()
    print(system)
    if system == "Linux" or system == "Darwin":
        # Exécute la commande "ip route" pour récupérer l'adresse IP et le masque de sous-réseau
        output = subprocess.run(["ip", "route"], capture_output=True).stdout.decode(errors='replace')
        lines = output.split("\n")
        for line in lines:
            if "link" in line:
                # Sépare l'adresse IP et le masque de sous-réseau
                parts = line.split()
                network = parts[0]
                subnet = network.strip().split('/')
                ip_address = subnet[0]
                mask = subnet[1]
                print(f"\nAdresse réseau : {network}")
                break

    elif system == "Windows":
        # Exécute la commande "ipconfig" pour récupérer l'adresse IP et le masque de sous-réseau
        # Voir pour utiliser la commande route print pour être sur de l'IP
        ip_address = socket.gethostbyname(socket.gethostname())
        output = subprocess.run(["route", "print"], capture_output=True).stdout.decode(errors='replace')
        lines = output.split("\n")
        for line in lines:
            if ip_address in line:
                if "0.0.0.0" not in line:
                    # Sépare le masque de sous-réseau
                    parts = line.split()
                    subnet_mask = parts[1]
                    break

        # Déterminer le réseau à partir de l'adresse IP et du masque de sous-réseau
        mask = IPAddress(subnet_mask).netmask_bits()
        ip_network = ipaddress.IPv4Network(f'{ip_address}/{mask}', strict=False)
        ip_network = str(ip_network.network_address)
        network = str(ip_network) + "/" + str(mask)

        # Affiche le réseau concerné
        print(f"\nAdresse réseau : {network}")

    else:
        print("Système d'exploitation non supporté.")
        return

    # Utiliser nmap pour effectuer un scan du réseau
    nm = nmap.PortScanner()
    nm.scan(hosts=network, arguments='-O -T5 -F')

    # Initialisez une liste vide pour contenir les résultats
    result_list = []
    ip_recon = []

    # Pour chaque hôte détecté
    for host in nm.all_hosts():
        osmatch_list = sorted(nm[host]['osmatch'], key=lambda x: x['accuracy'], reverse=True)

        # On récupère le système d'exploitation le plus probable (le premier de la liste triée)
        if osmatch_list:
            osmatch = osmatch_list[0]
            os = osmatch['name'] + " (" + str(osmatch['accuracy']) + "%)"
        else:
            os = "Unknown"

        # On ajoute les données dans la liste de résultats
        ip_recon.append(host)
        result_list.append({'host': host, 'os': os})

    # Créez un dictionnaire final avec une clé "result" associée à la liste de résultats
    final_dict = {'result': result_list}

    # Convertissez le dictionnaire final en format JSON
    json_file = json.dumps(final_dict)

    print(json_file)
    
    push_machine = request.check_machine(mydb, id_client, network, domain)
    machine_id = push_machine
    request.push_test(mydb, "recon", json_file, machine_id)
    
    active_scan(request, mydb, ip_recon, domain, id_client)