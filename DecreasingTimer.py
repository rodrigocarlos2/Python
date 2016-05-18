

import time
import os

print("Digite o tempo em horas: ");

horas = input();

horas = int(horas);

print("Digite o tempo em minutos: ");

minutos = input();

minutos = int(minutos);

print("Digite o tempo em segundos: ");

segundos = input();

segundos = int(segundos);

while horas>=0:

	while minutos >= 0:
	
		while segundos >=0:
		
			print(horas, ":", minutos, ":", segundos);
		
			time.sleep(1);
			
			os.system("cls");
			
			segundos = segundos - 1;
	
		minutos = minutos - 1;
		segundos = 60;
		
	horas = horas-1;
	minutos = 60;
