from getpass import getpass

from netmiko import ConnectHandler

def main():
    losenord = getpass("Losenord: ")

    enheter = [
        {"namn": "R-Nordvik-1", "host": "192.168.1.193"},
        {"namn:": "SW--Nordvik-1", "host": "192.168.1.194"},
    ]

    rader = ["# Inventarierapport", ""]
              
    for enhet in enheter:
        anslutning = ConnectHandler (
            device_type = "cisco_ios",
            host = enhet["host"],
            username = "drift",
            password = "losenord",
        )
    version = anslutning.send_command ("show version | include uptime")
    anslutning.disconnect()

    rader.append(f"## {enhet['namn']} ({enhet['host'
    ]})")
    rader.append(version)
    rader.append("")
    with open("inventarie.md", "w") as f:
        f.write("\n".join(rader))

    print(f"Skrev rapport for (len(enheter)) enheter till inventarie.md")

if __name__ == "__main__":
    main()