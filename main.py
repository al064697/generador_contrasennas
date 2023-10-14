#creando una contraseña segura

#funcion para crear contraseñas seguras
def create_random_password(num):
    chars = "abcdefghijklmnopqrstuvwxyz"
    integer_number = input_data#str(num)
    #num = int[num_entero[0]]
    num * 2
    char = num
    char1 = num - 1
    char2 = num - 2
    char3 = num - 3
    char4 = num - 4
    if(num <= 24):
        password = f'{chars[char]}{num}{chars[char1]}{chars[char2]}{chars[char3]}{integer_number * 2}{num}{chars[char4]}{integer_number * 4}'
        return password
    elif(num > 24):
        print(f'Proceso terminado. El proceso solo llega hasta 24 y usted ha usado {num}, por lo que no puede continuar')
        return None

#funcion que verifica los datos de salida
def output_data_verification():
    if (password == None):
        print("--------------------")
        print('No se pudo generar una contraseña de forma adecuada')
        print("--------------------")

    else:
        print(f'Generalmente las contraseñas que se consideran seguras es una mezcla de igual o mayor cantidad de digitos compuestos por letras y numeros y por eso te sugerimos: {password} como tu nueva contraseña')
        print("--------------------")

#funcion que arroja un menu de bienvenida con algunas especificaciones de la aplicacion
def menu():
    print("--------------------")
    print("Bienvenido")
    print("Antes de continuar, cabe mencionar que el programa solo alcanza a leer hasta el número 24, de revasar dicha cantidad se cerrara el programa")
    print("")

#ejecutando la funcion menu()
menu()

#ingresando un input de datos para que el usuario pueda escribir un número >24 y con base en eso crear la contraseña
input_data= input("Ingresa un digito para crear una contraseña segura: ")

#convirtiendo la variable input_data de tipo str a int
input_data = int(input_data)

print("--------------------")

#ejecutando las demás funciones
password = create_random_password(input_data)
output = output_data_verification()