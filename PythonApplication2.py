import random

print("ül 1 jänes:")
num = int(input("kirjuta number (0-9): "))

if 0 < num < 10:
    rida1 = "  (\\_/)  "
    rida2 = "  (o o)  "
    rida3 = "  / | \\* "

    print(rida1 * num)
    print(rida2 * num)
    print(rida3 * num)
else:
    print("Ei saa sisestada arvu, mis on väiksem kui 1 ja suurem kui 9.")

print("\n==============================")

print("\nül 2 summa:")
L = int(input("kirjuta arv L: "))  

summa = 0  
a = 0  

while a <= L:  
    summa = summa + a  
    a = a + 1  

print("summa on", summa)  

print("\n==============================")

print("\nül 3 arva ära arv (0-100):")
n = random.randint(0, 100)  
k = 0  
ok = False 

while k < 10:
    a = int(input("pakkumine: "))  
    if a == n:
        print("õige number oli", n) 
        ok = True
        break
    elif a < n:
        print("number on suurem")  
    else:
        print("number on väiksem")  
    k = k + 1

if ok == False:
    print("vale, õige number oli", n)  

print("")