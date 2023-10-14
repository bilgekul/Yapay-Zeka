print("3 adet değer giriniz")
input1 = int(input("Birinci değeri giriniz: "))
input2 = int(input("İkinci değeri giriniz: "))
input3 = int(input("Üçüncü değeri giriniz: "))

class Triangle:
    _first_degree : int
    _second_degree : int
    _third_degree : int
    def __init__(self,first_degree=int,second_degree=int,third_degree=int)->int:
        self._first_degree = first_degree
        self._second_degree = second_degree
        self._third_degree = third_degree
    
    @property
    def triangle(self):
        result = (self._first_degree+self._second_degree+self._third_degree)
        if result < 180:
            return "This is a narrow triangle"
        elif result == 180:
            return "This is a wide triangle"
        elif result > 180 and self._first_degree == 90:
            return "This is a right triangle"
           

triangle = Triangle(input1,input2,input3)
print(triangle.triangle)

      







