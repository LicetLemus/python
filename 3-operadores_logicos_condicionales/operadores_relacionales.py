4 == 5 #  False

4 != 5 #  True

4 == 4 #  True

a = 4
b = 5

a < b #  True
a > b #  False
a <= b #  True
a >= b #  False
a == b #  False
a != b #  True


a = 10 
b = 10
c = 5

# primero resuelve el parentesis, luego los operadores aritmeticos y por ultimo los operadores relacionales
(a + b) * c > a ** 2 # return False
