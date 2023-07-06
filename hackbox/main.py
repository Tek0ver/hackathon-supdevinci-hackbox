from scripts.scan import scanner_ports
from scripts.recon import recon
from scripts.scan_intense import active_scan
from scripts.db_kpi_sql import db_initiator
from scripts.db_kpi_sql import db_request
from settings import *

db = db_initiator()
request = db_request()

mydb = db.db_connect("20.199.117.214","cyberman","90886fghfjhgGHDFGHFNBJ","cyberbox")

def scan(adresse_ip : str=None):

    if adresse_ip is None:
        adresse_ip = input("Entrez une adresse IP : ")
    adresse_ip = [adresse_ip]

    if DOMAIN is None:
        domain = input("Entrez un domaine : ")
    else:
        domain = DOMAIN

    if ID_CLIENT is None:
        request.get_client(mydb)
        id_client = input("Entrez l'ID de l'entreprise' : ")
    else:
        id_client = ID_CLIENT

    scanner_ports(request, mydb, adresse_ip, domain, id_client)

def better_scan():

    adresse_ip = input("Entrez une adresse IP : ")
    adresse_ip = [adresse_ip]
    domain = input("Entrez un domaine : ")
    request.get_client(mydb)
    id_client = input("Entrez l'ID de l'entreprise' : ")
    active_scan(request, mydb, adresse_ip, domain, id_client)

def recon_subnet():

    if DOMAIN is None:
        domain = input("Entrez un domaine : ")
    else:
        domain = DOMAIN

    if ID_CLIENT is None:    
        request.get_client(mydb)
        id_client = input("Entrez l'ID de l'entreprise' : ")
    else:
        id_client = ID_CLIENT
        
    recon(request, mydb, domain, id_client)
