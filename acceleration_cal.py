#This code is going to be a simple yet efficient acceleration calculator

v = float(input('Your given final velocity [in m/s]: '))
u = float(input('Your given initial velocity [in m/s]: '))
t = float(input('Your given time period [in seconds]: '))

a = v - u
afinal = a / t
print('Your acceleration [in m/s^2]: ' + str(afinal))
