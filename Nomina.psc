Proceso Nomina
	
    Definir n, i Como Entero
    Definir nombre, puesto, num_empleado, periodo_pago, fecha_emision, departamento, tipo_contrato, tipo_jornada Como Cadena
    Definir dias_trabajados, faltas, domingos_trabajados, horas_extras, retardos Como Entero
    Definir sueldo_base, bono, prima_dominical, deducciones, isr, imss, desc_faltas, infonavit, pension_alimenticia Como Real
    Definir sueldo_bruto, sueldo_neto, pago_horas_extras, desc_retardos, valor_por_minuto Como Real
	
    Escribir "¿Cuántos empleados desea registrar?"
    Leer n
	
    Para i <- 1 Hasta n Con Paso 1
		
        Escribir "----- DATOS DEL EMPLEADO ", i, " -----"
        
        
        Escribir "Nombre:" ; Leer nombre
        Escribir "Puesto:" ; Leer puesto
        Escribir "Número de empleado:" ; Leer num_empleado
        Escribir "Departamento:" ; Leer departamento
        Escribir "Tipo de contrato:" ; Leer tipo_contrato
        Escribir "Tipo de jornada:" ; Leer tipo_jornada
        Escribir "Periodo de pago:" ; Leer periodo_pago
        Escribir "Fecha de emisión:" ; Leer fecha_emision
		
        
        Escribir "Días trabajados:" ; Leer dias_trabajados
        Escribir "Sueldo base:" ; Leer sueldo_base
        Escribir "Bono:" ; Leer bono
        Escribir "Faltas:" ; Leer faltas
        Escribir "Retardos (minutos):" ; Leer retardos
        Escribir "Horas extras:" ; Leer horas_extras
        Escribir "Domingos trabajados:" ; Leer domingos_trabajados
        Escribir "Deducciones extra:" ; Leer deducciones
        Escribir "Infonavit:" ; Leer infonavit
        Escribir "Pensión alimenticia:" ; Leer pension_alimenticia
		
        
        desc_faltas <- (sueldo_base / 30) * faltas
        prima_dominical <- (sueldo_base / 30) * 0.25 * domingos_trabajados
        pago_horas_extras <- ((sueldo_base / 30) / 8) * 2 * horas_extras
        valor_por_minuto <- (sueldo_base / 30) / 480
        desc_retardos <- valor_por_minuto * retardos
		
        sueldo_bruto <- sueldo_base + bono + prima_dominical + pago_horas_extras
        isr <- sueldo_bruto * 0.10
        imss <- sueldo_bruto * 0.07
		
        sueldo_neto <- sueldo_bruto - isr - imss - deducciones - infonavit - pension_alimenticia - desc_faltas - desc_retardos
		
        
        Escribir "-------- RECIBO DE NÓMINA --------"
        Escribir "Nombre: ", nombre, " | Puesto: ", puesto, " | No. Empleado: ", num_empleado
        Escribir "Depto: ", departamento, " | Contrato: ", tipo_contrato, " | Jornada: ", tipo_jornada
        Escribir "Periodo: ", periodo_pago, " | Fecha emisión: ", fecha_emision
        Escribir "----------------------------------"
        Escribir "Días trabajados: ", dias_trabajados, " | Faltas: ", faltas, " | Retardos: ", retardos, " min | Hrs. extras: ", horas_extras
        Escribir "----------------------------------"
        Escribir "Sueldo base: $", sueldo_base, " | Bono: $", bono
        Escribir "Prima dominical: $", prima_dominical, " | Hrs. extras: $", pago_horas_extras
        Escribir "Sueldo bruto: $", sueldo_bruto
        Escribir "----------------------------------"
        Escribir "ISR: $", isr, " | IMSS: $", imss
        Escribir "Desc. Faltas: $", desc_faltas, " | Retardos: $", desc_retardos
        Escribir "Infonavit: $", infonavit, " | Pensión: $", pension_alimenticia, " | Otras deducciones: $", deducciones
        Escribir "----------------------------------"
        Escribir "Sueldo Neto: $", sueldo_neto
        Escribir "----------------------------------"
        Escribir ""
		
    FinPara
	
FinProceso