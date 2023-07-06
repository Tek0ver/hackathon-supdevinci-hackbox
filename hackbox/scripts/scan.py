import nmap
import json

def scanner_ports(request, mydb, adresse_ip, domain, id_client):

    for ip in adresse_ip:
        # Initialisez une liste vide pour contenir les résultats
        result_list = []
        print(ip)
        # Créez un objet scanner nmap
        scanner = nmap.PortScanner()

        # Effectuez l'analyse des ports sur l'IP spécifiée
        scanner.scan(ip, arguments='-p 1-1000')

        # Parcourez les résultats et imprimez les ports ouverts
        for host in scanner.all_hosts():
            print(f"Résultats de l'analyse pour l'IP : {host}")
            if 'tcp' in scanner[host]:
                for port in scanner[host]['tcp'].keys():
                    state = scanner[host]['tcp'][port]['state']
                    if state == 'open':
                        # On ajoute les données dans la liste de résultats
                        result_list.append({'port': port})
            else:
                print("Aucune information sur les ports trouvée.")

        # Créez un dictionnaire final avec une clé "result" associée à la liste de résultats
        final_dict = {'result': result_list}

        # Convertissez le dictionnaire final en format JSON
        json_file = json.dumps(final_dict)

        print(json_file)
        push_machine = request.check_machine(mydb, id_client, ip, domain)
        machine_id = push_machine
        request.push_test(mydb, "nmap", json_file, machine_id)