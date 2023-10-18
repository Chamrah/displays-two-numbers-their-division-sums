#Program that displays two numbers their division sums
n=int(input("Veuillez entrer un entier : "))
d=0
for i in range(1,n+1):
    if(n % i ==0):
        d=d+1
print(f"Le nombre de division est {d}")