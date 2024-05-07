liste = []
entre = int(input())

def convesion(x) :
        rep = 8
        while rep > 0 :
            rep = rep-1
            if x%2 == 0 :
                liste.append(0)
            else :
                liste.append(1)  
                x = x-1
            x = x/2    

        return liste

convesion(entre) 
print(liste[::-1]) 
    