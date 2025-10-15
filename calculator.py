class Calculator:
    def __init__(self):
        self.version = "1.0.0"
    
    def add(self, a, b):
        """Sestevanje"""
        return a + b
    
    def subtract(self, a, b):
        """Odstevanje"""
        return a - b
    
    def multiply(self, a, b):
        """Mnozenje"""
        return a * b
    
    def divide(self, a, b):
        """Deljenje"""
        if b == 0:
            raise ValueError("Deljenje z nic ni mogoce!")
        return a / b
    
    def power(self, a, b):
        """Potenciranje"""
        return a ** b

def main():
    calc = Calculator()
    print(f"Kalkulator verzija {calc.version}")
    print("="*40)
    
    while True:
        print("\n1. Sestevanje")
        print("2. Odstevanje")
        print("3. Mnozenje")
        print("4. Deljenje")
        print("5. Potenciranje")
        print("0. Izhod")
        
        choice = input("\nIzberi operacijo: ")
        
        if choice == "0":
            print("Nasvidenje!")
            break
        
        if choice in ["1", "2", "3", "4", "5"]:
            try:
                a = float(input("Vnesi prvo stevilo: "))
                b = float(input("Vnesi drugo stevilo: "))
                
                if choice == "1":
                    print(f"Rezultat: {calc.add(a, b)}")
                elif choice == "2":
                    print(f"Rezultat: {calc.subtract(a, b)}")
                elif choice == "3":
                    print(f"Rezultat: {calc.multiply(a, b)}")
                elif choice == "4":
                    print(f"Rezultat: {calc.divide(a, b)}")
                elif choice == "5":
                    print(f"Rezultat: {calc.power(a, b)}")
            except ValueError as e:
                print(f"Napaka: {e}")
            except Exception as e:
                print(f"Prislo je do napake: {e}")
        else:
            print("Neveljavna izbira!")

if __name__ == "__main__":
    main()