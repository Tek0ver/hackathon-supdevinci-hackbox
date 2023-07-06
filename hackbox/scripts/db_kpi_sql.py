import datetime
import mysql.connector
import os

class db_initiator:

    def __init__(self):
        pass

    def db_connect(self, ip, usr, pwd, db):
        try:
            mydb = mysql.connector.connect(
            host = ip,
            user = usr,
            password = pwd,
            database = db
            )

            print(f"Connexion OK")

            return mydb
        
        except:
            print(f"Erreur de connexion à la base de données.")
            os.exit()

class db_request:
    
    def __init__(self):
        pass

    def get_client(self, mydb):
        
        sql_client = "SELECT id, entreprise FROM client"
        
        try:
            cursor = mydb.cursor()
            cursor.execute(sql_client)
            all_client = cursor.fetchall()
            print("OK")
            print(all_client)

        except:
            # Rolling back in case of error
            mydb.rollback()
            print("NOK")

    def check_machine(self, mydb, id_client, adresse_ip, domain):

        sql_check_machine = f"SELECT id FROM machine WHERE client_id = {id_client} AND ip = '{adresse_ip}' AND domaine = '{domain}'"

        try:
            cursor = mydb.cursor()
            cursor.execute(sql_check_machine)
            #result_set = cursor.fetchall()
            exist_machine = cursor.fetchone()
            print("OK")

        except:
            # Rolling back in case of error
            mydb.rollback()
            print("NOK")

        if exist_machine == None:

            self.push_machine(mydb, id_client, adresse_ip, domain)
            id_machine = self.check_machine(mydb, id_client, adresse_ip, domain)
            return id_machine

        else:
            id_machine = exist_machine[0]
            return id_machine

    def push_machine(self, mydb, id_client, adresse_ip, domain):

        sql_create_machine = f"INSERT INTO machine (client_id, ip, domaine) VALUES ('{id_client}', '{adresse_ip}', '{domain}');"

        try:
            cursor = mydb.cursor()
            cursor.execute(sql_create_machine)
            mydb.commit()
            print("OK")

        except:
            # Rolling back in case of error
            mydb.rollback()
            print("NOK")

    def push_test(self, mydb, type, result, machine_id):
        
        date = datetime.datetime.now()

        sql_result_test = f"INSERT INTO test (type, result, date, machine_id) VALUES ('{type}', '{result}', '{date}', '{machine_id}');"
        
        try:
            cursor = mydb.cursor()
            cursor.execute(sql_result_test)
            mydb.commit()
            print("OK")

        except:
            # Rolling back in case of error
            mydb.rollback()
            print("NOK")