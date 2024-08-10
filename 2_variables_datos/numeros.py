num = 10
type(num) # int
print(num + 10) # 20

num2 = "10" # string
type(num2) # str

print(num2 + "10") # 1010

num3 = 10.5 # float
type(num3) # float
print(num3 + 10) # 20.5

num4 = -10 # int negativo
type(num4) # int 
print(num4 + 10) # 0

num5 = 1_000_000 # int con guiones bajos para hacerlo más legible es igual a 1000000
type(num5) # int 
print(num5 + 10) # 1000010

num6 = 10 + 5j # complex
type(num6) # complex
print(num6 + 10) # (20+5j)

num7 = 1e6 # float en notación científica
num8 = 1e400 # float en notación científica
print(num8) # inf infinito