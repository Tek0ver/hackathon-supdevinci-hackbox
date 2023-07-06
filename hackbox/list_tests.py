from scripts.foo_ip_collect import foo_ip_collect
from scripts.foo_scan_open_ports import foo_scan_open_ports
from scripts.foo_count import foo_count

test_mode = False

if not test_mode:

    import main as scripts

    tests = [
        {
            "id": 1,
            "title": "Scan léger d'une IP",
            "description": "",
            "command": scripts.scan,
            "parameter": [('IP à scanner (exemple: 15.111.5.48)', 'str', "0.0.0.0")]
        },
        {
            "id": 2,
            "title": "Scan du réseau pour scanner toutes les IPs",
            "description": "",
            "command": scripts.recon_subnet,
            "parameter": []
        },
        {
            "id": 3,
            "title": "Recherche des CVE",
            "description": "",
            "command": scripts.better_scan,
            "parameter": []
        }
    ]

else:

    def test3():
        print("Voilà les CVE !")

    tests = [
        {
            "id": 1,
            "title": "Récupération des ips",
            "description": "",
            "command": foo_ip_collect,
            "parameter": []
        },
        {
            "id": 2,
            "title": "Scan des ports",
            "description": "",
            "command": foo_scan_open_ports,
            "parameter": []
        },
        {
            "id": 3,
            "title": "Recherche des CVE",
            "description": "",
            "command": test3,
            "parameter": []
        },
        {
            "id": 4,
            "title": "Counter(for testing)",
            "description": "Lance un compteur pour tester.",
            "command": foo_count,
            "parameter": [('tick', 'int', 2), ('max', 'int', 30)]
        }
    ]
