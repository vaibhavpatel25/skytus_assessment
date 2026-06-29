#check type of triangle(Equilateral,Isosceles,Scalene)

Side1=float(input("Enter a side 1 of Triangle :"))
Side2=float(input("Enter a side 2 of Triangle :"))
Side3=float(input("Enter a side 3 of Triangle :"))

if Side1==Side2==Side3:
    print("The Triangle type is Equilateral ")
elif Side1==Side2 or Side1==Side3 or Side2==Side3:
    print("The Triangle type is Isosceles ")
else:
    print("The Triangle type is Scalene")