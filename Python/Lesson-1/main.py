def main():
    name = input ("Enter your name: ")
    
    if name == "Axel":
        bool =True
    else:
        bool = False
        
    if bool:
        print(f"Hello {name}, welcome back!")
        
    else: 
        print(f"Hello {name}, you're not the owner of this computer >:(")
        
if __name__ == "__main__":
    main()