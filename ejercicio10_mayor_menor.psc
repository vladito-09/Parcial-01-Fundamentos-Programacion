Proceso Mayor_y_Menor
	
    Definir num1 Como Real
    Definir num2 Como Real
	
    Escribir "Ingrese el primer numero:"
    Leer num1
	
    Escribir "Ingrese el segundo numero:"
    Leer num2
	
    Si num1 > num2 Entonces
        Escribir "El numero mayor es: ", num1
        Escribir "El numero menor es: ", num2
    SiNo
        Si num2 > num1 Entonces
            Escribir "El numero mayor es: ", num2
            Escribir "El numero menor es: ", num1
        SiNo
            Escribir "Los numeros son iguales"
        FinSi
    FinSi
	
FinProceso
