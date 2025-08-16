#def soma(a:float, b:float, c:float)->float:
#    return a + b + c
#
#def media(a:float, b:float, c=0)->float: # função que usa outra função dentro dela / Quando o ultimo argumento é igual a zero, ele se torna opcional no codigo
#    return soma(a,b,c) / 3
#
#
#a = float(input("entre com o valor de a: "))
#b = float(input("entre com o valor de b: "))
#c = float(input("entre com o valor de c: "))
#
#print("Media:", media(a,b))

#%%

def soma(a:float, b:float, *args)->float: # '*' -> representa uma lista de argumentos opcionais, varias tuplas
    valores = [a,b] + list(args)
    return sum(valores)

def media(a:float, b:float, *args)->float:
    return soma(a,b, *args) / (len(args)+2)


a = float(input("entre com o valor de a: "))
b = float(input("entre com o valor de b: "))
c = float(input("entre com o valor de c: "))
d = float(input("entre com o valor de d: "))
e = float(input("entre com o valor de e: "))


print("Media:", media(a,b,c,d,e))