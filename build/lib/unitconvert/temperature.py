"""
Converts between celsius and fahrenheit

"""

def celsius_to_fahrenheit(tempc):
 """
 Convert the input temperature from Celsius to Fahrenheit
 PARAMETERS
 ----------
 tempc : float
 a temperature in degrees Celsius
 RETURNS
 -------
 tempf : float
 """
    return (tempc*(5/9))+32

def fahrenheit_to_celsius(tempf):
 """
 Convert the input temperature from Fahrenheit to Celsius
  PARAMETERS
 ----------
 tempf : float
 a temperature in degrees fahrenheit
 RETURNS
 -------
 tempc : float
 """
    return (tempf*9/5)-32