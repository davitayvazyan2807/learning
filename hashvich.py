import math

print("Hashvich")
print("1-gumari")
print("2-hani")
print("3-bajani")
print("4-bazmapatki")
print("5-armat hani")
print("6-qarakusi hani")

yntrutyun = input("Yntrir gorcoxutyuny (1-6): ")

if yntrutyun == "1":
    a = float(input("Arajin tivy: "))
    b = float(input("Erkrord tivy: "))
    result = a + b
elif yntrutyun == "2":
    a = float(input("Arajin tivy: "))
    b = float(input("Erkrord tivy: "))
    result = a - b
elif yntrutyun == "3":
    a = float(input("Arajin tivy: "))
    b = float(input("Erkrord tivy: "))
    result = a / b
elif yntrutyun == "4":
    a = float(input("Arajin tivy: "))
    b = float(input("Erkrord tivy: "))
    result = a * b
elif yntrutyun == "5":
    a = float(input("Tivy: "))
    result = math.sqrt(a)
elif yntrutyun == "6":
    a = float(input("Tivy: "))
    result = a ** 2
else:
    result = "sxal yntrutyun"

print( "aha dzer xndiri lucumy:   " +  str(result) )
