# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 14:57:15 2024

@author: ASAF
"""
from abc import ABC , abstractmethod

class Shape(ABC):
    """
    Shape sınıfı, soyut bir sınıftır ve geometrik şekilleri temsil eder.
    Bu sınıf, türetilen alt sınıflar için bir şablon sağlar.
    """
    @abstractmethod
    def area(self): 
        """
        Alanı hesaplayan soyut metoddur. Türetilen sınıflar tarafından uygulanmalıdır.
        """
        pass

    @abstractmethod
    def perimeter(self): 
        """
        Çevreyi hesaplayan soyut metoddur. Türetilen sınıflar tarafından uygulanmalıdır.
        """
        pass

    def tostring(self): 
        """
        Şeklin bilgilerini yazdıran metoddur. Alt sınıflar tarafından gerektiğinde geçersiz kılınabilir.
        """
        pass 
        
class Square(Shape):
    """
    Square sınıfı, Shape sınıfından türetilmiş alt bir sınıftır ve kare şekillerini temsil eder.
    """
    def __init__(self, edge):
        self.__edge = edge 
    
    def area(self):
        """
        Kare alanını hesaplayan metoddur.
        """
        result = self.__edge**2
        print("Square area:", result)
        
    def perimeter(self):
        """
        Kare çevresini hesaplayan metoddur.
        """
        result = 4 * self.__edge
        print("Square perimeter:", result)
    
    def tostring(self):
        """
        Kare kenar uzunluğunu yazdıran metoddur.
        """
        print("Square edge:", self.__edge)
    
class Circle(Shape):
    """
    Circle sınıfı, Shape sınıfından türetilmiş alt bir sınıftır ve daireleri temsil eder.
    """
    PI = 3.14
    
    def __init__(self, radius):
        self.__radius = radius
        
    def area(self):
        """
        Daire alanını hesaplayan metoddur.
        """
        result = self.PI * self.__radius**2
        print("Circle area:", result)
        
    def perimeter(self):
        """
        Daire çevresini hesaplayan metoddur.
        """
        result = 2 * self.PI * self.__radius
        print("Circle perimeter:", result)
        
    def tostring(self):
        """
        Daire yarıçapını yazdıran metoddur.
        """
        print("Circle radius:", self.__radius)
        
# Daire örneği oluşturma ve metotları çağırma
c = Circle(10)
c.area()
c.perimeter()
c.tostring()
        
# Kare örneği oluşturma ve metotları çağırma
s = Square(10)   
s.area()
s.perimeter()
s.tostring()  
    
    
    
    
    
    
    
    
    
    
    
    
    