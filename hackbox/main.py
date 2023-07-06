from scripts.scan import scanner_ports
from scripts.recon import recon
from scripts.scan_intense import active_scan
from scripts.db_kpi_sql import db_initiator
from scripts.db_kpi_sql import db_request


db = db_initiator()
request = db_request()

mydb = db.db_connect("20.199.117.214","cyberman","90886fghfjhgGHDFGHFNBJ","cyberbox")

def scan():

    adresse_ip = input("Entrez une adresse IP : ")
    adresse_ip = [adresse_ip]
    domain = input("Entrez un domaine : ")
    request.get_client(mydb)
    id_client = input("Entrez l'ID de l'entreprise' : ")
    scanner_ports(request, mydb, adresse_ip, domain, id_client)

def better_scan():

    adresse_ip = input("Entrez une adresse IP : ")
    adresse_ip = [adresse_ip]
    domain = input("Entrez un domaine : ")
    request.get_client(mydb)
    id_client = input("Entrez l'ID de l'entreprise' : ")
    active_scan(request, mydb, adresse_ip, domain, id_client)

def recon_subnet():

    domain = input("Entrez un domaine : ")
    request.get_client(mydb)
    id_client = input("Entrez l'ID de l'entreprise' : ")
    recon(request, mydb, domain, id_client)
