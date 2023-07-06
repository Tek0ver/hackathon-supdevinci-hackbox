import nmap
import json
import requests

def active_scan(request, mydb, ips, domain, id_client):

    for ip in ips:
        # Initialisez une liste vide pour contenir les résultats
        result_list = []
        active_ports = []
        print(ip)
        # Créez un objet scanner nmap
        scanner = nmap.PortScanner()

        # Effectuez l'analyse des ports sur l'IP spécifiée
        try:
            scanner.scan(ip, arguments='-sS', timeout=300)
        except:
            pass

        # Parcourez les résultats et imprimez les ports ouverts
        for host in scanner.all_hosts():
            print(f"Résultats de l'analyse pour l'IP : {host}")
            if 'tcp' in scanner[host]:
                for port in scanner[host]['tcp'].keys():
                    state = scanner[host]['tcp'][port]['state']
                    if state == 'open' or state == 'filtered' or state == 'unfiltered':
                        print(f"\nPort {port} : Ouvert")
                        # On ajoute les données dans la liste de résultats
                        active_ports.append(port)
            else:
                print("Aucune information sur les ports trouvée.")

            # Crée un objet nmap.PortScanner pour scanner l'adresse IP
            nm = nmap.PortScanner()

            for active_port in active_ports:

                print(f"\nSan intense pour {ip}, port {active_port}")

                nmap_arguments = f"-A -T4 -p {active_port}"

                # Execute le scan
                try:
                    nm.scan(ip, arguments=nmap_arguments, timeout=120)
                except:
                    pass

                # Récupère les ports ouverts et leurs informations
                open_ports = nm[ip]["tcp"].keys()
                port_info = {}
                for port in open_ports:
                    port_info[port] = {
                        "service": nm[ip]["tcp"][port]["product"],
                        "version": nm[ip]["tcp"][port]["version"],
                        "name": nm[ip]["tcp"][port]["name"],
                        "cpe": nm[ip]["tcp"][port]["cpe"]
                    }

                # Ajoute les ports ouverts, leurs informations et les CVE associées dans le tableau
                for port, info in port_info.items():
                    error_api = False
                    cvss = ""
                    name_cve = ""
                    # Vérifie si une donnée CPE est disponible (vulnérabilité) afin d'effectuer une recherche CVE
                    if info["cpe"] != "":
                        cpe_split = info["cpe"].split(":")
                        # Exclu les recherche sur "linux" et sur "windows" afin d'éviter les CVEs inutiles sur le kernel
                        if "linux" not in cpe_split:
                            if "windows" not in cpe_split:
                                # Envoyez une requête à l'API de NVD avec le CPE
                                response = requests.get(
                                    f'https://services.nvd.nist.gov/rest/json/cves/1.0?cpeMatchString={info["cpe"]}')
                                if response.status_code == 200:
                                    # Récupérez la liste des vulnérabilités dans le résultat de la recherche
                                    cves = response.json()['result']['CVE_Items']
                                    # Pour chaque vulnérabilité, récupère son identifiant et sa description
                                    for cve in cves:
                                        # Récupère le score CVSS
                                        if 'baseMetricV3' in cve['impact']:
                                            cvss_score = cve['impact']['baseMetricV3']['cvssV3']['baseScore']
                                        elif 'baseMetricV2' in cve['impact']:
                                            cvss_score = cve['impact']['baseMetricV2']['cvssV2']['baseScore']
                                        else:
                                            cvss_score = 0
                                        if cvss_score > 6:
                                            cvss = cvss_score
                                            cve = cve["cve"]["CVE_data_meta"]["ID"]
                                            # Decommenter la ligne ci dessous si on souhaite avoir les liens des CVEs à la place du numéro de CVE
                                            # cve = "https://nvd.nist.gov/vuln/detail/" + cve
                                            name_cve = cve
                                            # name_cve.append(cve["cve"]["CVE_data_meta"]["ID"])
                                            # Incrémente le tableau avec les informations des ports avec CVE
                                        result_list.append({'port': active_port, 'protocole': info["name"], 'service': info["service"], 'version': info["version"], 'cve': name_cve, 'cvss': cvss})
                                        print(f'Port : {active_port}, protocole : {info["name"]}, service : {info["service"]}, version: {info["version"]}, cve : {name_cve}, cvss : {cvss}')
                                else:
                                    error_api = True
                            else:
                                result_list.append({'port': active_port, 'protocole': info["name"], 'service': info["service"], 'version': info["version"], 'cve': name_cve, 'cvss': cvss})
                                print(f'Port: {active_port}, protocole : {info["name"]}, service : {info["service"]}, version: {info["version"]}, cve : {name_cve}, cvss : {cvss}')
                        else:
                            result_list.append({'port': active_port, 'protocole': info["name"], 'service': info["service"], 'version': info["version"], 'cve': name_cve, 'cvss': cvss})
                            print(f'Port: {active_port}, protocole : {info["name"]}, service : {info["service"]}, version: {info["version"]}, cve : {name_cve}, cvss : {cvss}')
                    else:
                        # Incrémente le tableau avec les informations des ports sans CVE
                        result_list.append({'port': active_port, 'protocole': info["name"], 'service': info["service"], 'version': info["version"], 'cve': name_cve, 'cvss': cvss})
                        print(f'Port: {active_port}, protocole : {info["name"]}, service : {info["service"]}, version: {info["version"]}, cve : {name_cve}, cvss : {cvss}')

                # Créez un dictionnaire final avec une clé "result" associée à la liste de résultats
                final_dict = {'result': result_list}

                # Convertissez le dictionnaire final en format JSON
                json_file = json.dumps(final_dict)

                #print(json_file)

                push_machine = request.check_machine(mydb, id_client, ip, domain)
                machine_id = push_machine
                request.push_test(mydb, "nmap", json_file, machine_id)

                # Affiche un message en cas d'erreur pour l'API de NVD (check CVEs)
                if error_api == True:
                    print(f"Error {response.status_code} pour l'API de NVD. Impossible de vérifier les CVEs.\n")