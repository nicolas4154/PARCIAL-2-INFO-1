def diagnosticar_lh(sexo, edad, resultado):
    if sexo == 'mujer':
        if edad < 18:
            rango = (0, 5)
        elif edad >= 18 and edad < 50:
            rango = (5, 25)
        else:
            rango = (14.2, 52.3)
    elif sexo == 'hombre':
        if edad < 18:
            rango = (1, 1.8)
        else:
            rango = (1.8, 8.6)
    else:
        return "Sexo desconocido. Por favor, introduzca 'hombre' o 'mujer'."

    if rango[0] <= resultado <= rango[1]:
        return "El resultado de la prueba LH está dentro del rango normal."
    else:
        return "El resultado de la prueba LH está fuera del rango normal."


def validar(prompt):
    attempts = 3
    while attempts > 0:
        try:
            value = int(input(prompt))
            return value
        
        except ValueError:
            print("Error: Debes ingresar un número entero.")
            attempts -= 1
    print("Has alcanzado el límite de intentos. Volviendo al menú principal.")
    return None


def validate_float_input(prompt):
    attempts = 3
    while attempts > 0:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Debes ingresar un número decimal.")
            attempts -= 1
    print("Has alcanzado el límite de intentos. Volviendo al menú principal.")
    return None

def generate_patient_code(type_of_patient, counter):
    
    if type_of_patient == "SISBEN":
        code = f"EPS-SISBEN-{counter}"
    
    elif type_of_patient == "Sura":
        code = f"EPS-Sura-{counter}"

    elif type_of_patient == "Coomeva":
        code = f"EPS-Coomeva-{counter}"

    elif type_of_patient == "Medimas":
        code = f"EPS-Medimas-{counter}"

    elif type_of_patient == "IPS Universitaria":
        code = f"EPS-IPS Universitaria-{counter}"

    elif type_of_patient == "Salud Total":
        code = f"EPS-Salud Total-{counter}"

    else:
        print(f"La EPS {type_of_patient} no se enceuntra en nuestro sistema")

    return code

def search_patient(list_pac):

    documento = validar("Ingrese el documento de identidad del paciente: ")
    if documento in list_pac:
        patient_data = list_pac[documento]
        print("\nDatos del paciente:")
        print(f"Documento: {documento}")
        print(f"Nombre: {patient_data[0]}")
        print(f"Código del paciente: {patient_data[1]}")
        print(f"Fecha de nacimiento: {patient_data[2]}")
        print(f"Edad: {patient_data[3]}")
        print(f"Resultado de la prueba HbA1c: {patient_data[4][0]}")
        print(f"Diagnóstico: {patient_data[4][1]}")
    else:
        print(f"El paciente con el número de identificación {documento} no existe en la base de datos.")



