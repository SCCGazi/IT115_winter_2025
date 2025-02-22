import math
import keyboard
while True:
    dia = float(input("Diameter(mm)="))
    rad = dia / 2
    len = float(input("Length(mm)="))
    # Distance(mm)=
    # dis = float(input("Distance(mm)="));
    for dis in range(100):
        s = len + dis
        B = 500 * ((s / math.sqrt(pow(rad, 2) + pow(s, 2))) - (dis / math.sqrt(pow(rad, 2) + pow(dis, 2))));
        B = B / 1000 #conversion from mili TESLA into Tesla
        A = math.pi * (rad / 1000) * (rad / 1000) #area
        u = 0.0000004 * math.pi #permeability *100 for steel coated
        F = B * B * A / (2 * u)
        kg = F / 9.81
        lb = kg * 2.2046226218
        inch = dis * 0.0394
        print(f"flux B(x)= {B} mT")
        print(f"F= {kg:.10f}kg, {lb:.10f}lb, {F:.10f}N, d={dis}mm, {inch:.10f}inch")
    print("recalculate? press esc for exit")
    if keyboard.is_pressed('esc'):
        print('Escape key pressed')
        break