def main():
    vendors = {
        "a4:c3:f0": "Intel",
        "3c:d9:2b": "Hewlett-Packard",
        "00:1a:a1": "Cisco Systems",
    }
    
    addresses = [
        "a4:c3:f0:11:3a:b7",
        "3c:d9:2b:d2:11:88",
        "8c:85:90:44:12:0e",
    ]
    
    for address in addresses:
        prefix = address [0:8]
        
    
        if prefix in vendors:
            name = vendors [prefix]
        else:
            name = "Okänd tillverkare"
    
        print(f"{address} -> {name}")
        
if __name__ == "__main__":
    main()