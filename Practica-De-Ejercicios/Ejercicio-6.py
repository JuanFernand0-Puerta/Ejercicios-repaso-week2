hora=int(input("Que hora es (0h,23h)"))

if hora < 12 or hora > 18:
    print("No es hora de trabajar")
else:
    print("Es hora de trabajar")