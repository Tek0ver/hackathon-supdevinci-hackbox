from scripts.foo_ip_collect import foo_ip_collect
from scripts.foo_scan_open_ports import foo_scan_open_ports
from scripts.foo_count import foo_count

test_mode = True

if not test_mode:

    import main as scripts

    tests = [
        {
            "id": 1,
            "title": "Récupération des ips",
            "description": "",
            "command": scripts.scan,
            "parameter": []
        },
        {
            "id": 2,
            "title": "Scan des ports",
            "description": "",
            "command": scripts.recon,
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
