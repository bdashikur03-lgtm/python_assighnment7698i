weight=float(input('enter the number'))
height=float(input('enter the feet value'))
height2=(height*0.3048)

bmi=(weight/height2**2)
print('BMI is',bmi)

if bmi <18.5:
    print('its underweight')
elif bmi >=18.5 and bmi<=24.9:
    print('its normal')
elif bmi >=25.0 and bmi<=29.9:
    print('its overweight')
else:
    print('its obese')

