Algoritmo geometric_areas
	Definir lado, baseRect, alturaRect, baseTri, alturaTri, radio como Real 
	Definir areaCuadrado, areaRect, areaTri, areaCir, totalAreas Como Real
	pivalor <-3.1416
	
	Escribir "Ingrese el lado del cuadrado: "
	Leer lado
	Escribir "Ingrese la base del rectangulo: "
	Leer baseRect
	
	Escribir "Ingrese la altura del rectangulo: "
	Leer alturaRect
	Escribir "Ingrese la base del triangulo: "
	Leer baseTri
	
	Escribir "Ingrese la altura del triangulo: "
	Leer alturaTri
	Escribir "Ingrese el radio del circulo: "
	Leer radio
	
	areaCuadrado <- lado * lado
	areaRect <- baseRect * alturaRect
	areaTri <- (baseTri * alturaTri) / 2
	areaCir <- pivalor * (radio* radio)
	totalAreas <- areaCuadrado + areaRect + areaTri + areaCir
	
	Escribir "Area del cuadrado es: " , areaCuadrado
	Escribir "Area del rectangulo es: " , areaRect
	Escribir "Area del triangulo es: " , areaTri
	Escribir "Area del circulo es: " , areaCir
	Escribir "Total de todas las areas es: " , totalAreas
	
FinAlgoritmo
