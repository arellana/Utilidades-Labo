eleccionCampo = input('Elejir distribucion (1,2, o 3): ')

eleccionCampo = int(eleccionCampo)

if eleccionCampo == 1:
    import programas.Campo1
elif eleccionCampo == 2:
    import programas.Campo2
elif eleccionCampo == 3:
    import programas.Campo3
else:
    print('Cerrando')




