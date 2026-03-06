Proceso Calificacion_Estudiante
	
    Definir nota Como Entero
	
    Escribir "Ingrese la nota del estudiante (0 a 10): "
    Leer nota
	
    Si nota >= 6 Entonces
        Escribir "Aprobado"
    Sino
        Si nota = 5 Entonces
            Escribir "Recuperacion"
        Sino
            Si nota <= 4 Entonces
                Escribir "Reprobado"
            FinSi
        FinSi
    FinSi
	
FinProceso