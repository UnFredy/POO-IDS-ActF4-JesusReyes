from abc import ABC, abstractmethod
# CLASE PRINCIPAL: Producto

class Producto(ABC):
    
    __limite_descuento = 0.5
    
    def __init__(self, nombre, descripcion, precio, stock):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
    

    @abstractmethod
    def mostrar_info(self):
        pass
    
    def actualizar_stock(self, cantidad):
        self.stock += cantidad
        print(f"{self.nombre}. Stock actualizado a: {self.stock} unidades.")
        
    def mostrar_precio(self):
        print(f"${self.precio}") 
    
    def venta(self, cantidad):
        
        if self.stock > 0:
            if self.stock - cantidad >= 0:
                self.stock -= cantidad
                print(f"Venta realizada! \n{self.nombre}. Nuevo stock: {self.stock}")
            else:
                print(f"{self.nombre}. Stock insuficiente para la venta. Stock actual: {self.stock}. Productos requeridos: {cantidad}")
        else:
            print("No hay stock")
    
    def aplicar_descuento(self, descuento):
        
        if descuento > self.__limite_descuento:
            raise ValueError("Descuento mayor al limite")
        self.precio = round(self.precio * (1 - descuento), 2)
    

class Electronico(Producto):
    def mostrar_info(self):
        print(f"--- ELECTRÓNICO --- \n{self.nombre}. \n{self.descripcion}. \nPrecio: ${self.precio} \nStock: {self.stock}")



class Ropa(Producto):
    
    def __init__(self, nombre, descripcion, precio, stock, talla):
        super().__init__(nombre, descripcion, precio, stock)
        self.talla = talla
        
    def mostrar_info(self):
        print(f"--- ROPA --- \n{self.nombre} \n{self.descripcion} \nPrecio: ${self.precio} \nStock: {self.stock} en talla {self.talla}")



class Videojuegos(Electronico):
    def __init__(self, nombre, descripcion, precio, stock, plataforma, genero):
        super().__init__(nombre, descripcion, precio, stock)
        self.plataforma = plataforma  
        self.genero = genero
        
        
    def mostrar_info(self):
        print(f"--- VIDEOJUEGO --- \n{self.nombre} - {self.genero} \n{self.descripcion}. \nPrecio: ${self.precio} \nCopias disponibles: {self.stock} {self.plataforma}")

    
tele = Electronico("Televisor", "Televisor 42 pulgadas", 5500, 10)
camisa = Ropa("Camisa", "Camisa de algodón color azul tipo polo", 350, 25, "M")
juego = Videojuegos("Zelda", "Aventura en mundo abierto", 1400, 5, "Xbox", "Aventura")

Productos = [tele, camisa, juego]


for p in Productos:
    p.mostrar_info()
    p.aplicar_descuento(0.2)

tele.actualizar_stock(20)
camisa.venta(10)
juego.venta(10)