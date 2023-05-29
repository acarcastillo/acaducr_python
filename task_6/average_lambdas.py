# Definimos el diccionario con los datos del estudiante
sampleDict = {
    "nombre": "Mike",
    "notas": {
        "fisica": 70,
        "historia": 80,
        "matematicas": 90
    }
}
# Accedemos a los datos del estudiante
nombre = sampleDict["nombre"]
notas = sampleDict["notas"]
# Calculamos el promedio de notas
promedio_notas = sum(notas.values()) / len(notas)
# Creamos un diccionario con el resultado
resultado = {"nombre": nombre, "nota": promedio_notas}
# Imprimimos el resultado
print(resultado)

#MISMO EJEMPLO ANTERIOR PERO USANDO LAMBDAS:
obtener_promedio = lambda d: {"nombre": d["nombre"], "nota": sum(d["notas"].values()) / len(d["notas"])}
print(obtener_promedio(sampleDict))