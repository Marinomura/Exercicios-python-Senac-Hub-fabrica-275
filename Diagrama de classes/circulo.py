#atributo raio e 2 métodos: um para calcular a area do 
# circulo e outro para calcular o perimetro(criar no minimo 2 objetos)
class circulo():
    def __init__(self) :
    
       self.raio= (float (input ('Digite a medida do raio: ')))
       
    def area (self):
        area=(self.raio**2)*3.14
        return print (area)
    def perimetro (self):
        perimetro=2*3.14*self.raio
        return print (perimetro)
    
c1=circulo () 
c1.perimetro()
c1.area()
    
    
        
        
    