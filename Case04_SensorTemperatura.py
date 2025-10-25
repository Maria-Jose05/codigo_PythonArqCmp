Vs = 20  # voltios
Rs = 75  # ohmios
Ro = 100 # ohmios
k  = 0.5 # adimensionel
done = 1 # centinela
while done:
	Vm = float(input("Ingrese el voltaje mostrado en el multimetro: "))

	if Vm >=12.0 and Vm <= 18.0: #Si vm está entre los parametros entonces:
		T = (Rs/k)*(Vm/(Vs-Vm))-(Ro/k) #Formula de la temperatura de la camara.
		print("La temperatura de la camara de gas es: ",T)
		done = 0 #Desactiva centinela
	else:
		print("Voltaje Incorrecto. Por favor ingrese nuevamente el valor.")
