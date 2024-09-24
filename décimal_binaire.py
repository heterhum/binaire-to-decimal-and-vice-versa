liste = []
def conversion(x):
    for _ in range(0,8):
        if x%2 == 0:
            liste.append(0)
        else:
            liste.append(1)  
            x = x-1
        x = x/2    
    return liste
conversion("number here") 
print(liste[::-1]) 
