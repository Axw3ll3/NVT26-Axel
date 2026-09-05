def vlan_config(number, name):
    rader = []
    rader.append(f"vlan: {number}")
    rader.append(f"name: {name}")
    return rader

vlans = {
    10: "KONTOR",
    20: "EKONOMI",
    30: "GAST",
    40: "DRIFT",
    }

for number in vlans:
    for rad in vlan_config(number, vlans[number]):
        print (rad)
