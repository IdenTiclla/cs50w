class Humano:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def print_info(self):
        print(f"Yor name: {self.nombre}")
        print(f"your lastname: {self.apellido}")
        print(f"your age: {self.edad}")
    def delay_age(self,aumento):
        self.edad += aumento

def main():
    # create a new human
    h1 = Humano(nombre="Iden", apellido="Ticlla", edad=20)
    h1.print_info()
    print()
    h2 = Humano(nombre="Alex", apellido="Ticlla", edad=15)
    h2.delay_age(5)
    h2.print_info()
if __name__ == "__main__":
    main()