#Convertir de Farenheit a Kelvin
def F_to_K(F):
    kelvin = ((5/9) * (F - 32) + 273.15)
    return kelvin

#Convertir de Celsius a Rankine
def C_to_R(C):
    Rankine = ((1.8 * C) + 491.67)
    return Rankine

#Convertir de Celsius a Farenheit
def C_to_F(C):
    Farenheit = ((C * 1.8) + 32)
    return Farenheit
