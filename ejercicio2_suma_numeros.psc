Proceso Suma_Numeros_Positivos
	
    Definir numero Como Entero
    Definir suma Como Entero
	
    suma <- 0
	
    Repetir
        Escribir "Ingrese un numero (negativo para terminar): "
        Leer numero
		
        Si numero >= 0 Entonces
            suma <- suma + numero
        FinSi
		
    Hasta Que numero < 0
	
    Escribir "La suma de los numeros positivos es: ", suma
	
FinProceso
