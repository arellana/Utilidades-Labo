1###Autorun.m debe correrse desde la terminal utilizando
# octave -f Autorun.m 
# estando en el directorio donde se encuentra Autorun.m

opcion = input("Elejir potencial (1,2 o 3): ");


switch (opcion)
case 1
	cd programas;
  Potencial1();
  disp('Presion Enter para cerrar')
  pause()  
case 2
  cd programas;
	Potencial2();
  disp('Presion Enter para cerrar')
  pause()    
case 3
  cd programas
	Potencial3();
  disp('Presion Enter para cerrar')
  pause()  
otherwise
	disp("Cerrando");
endswitch

