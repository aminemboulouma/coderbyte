def Letter_Changes(s): 

    # code goes here 

    q = list(s)
    p = []
    ALPHABET = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z] 
    VOWELS = [a, e, i, o, u]
    for i in range(len(q)):
        if q[i] == 'z':
            p.append('a')
        else:
            p.append(ALPHABET[ALPHABET.index(q[i])+1])
    for i in range(len(p)):
        if p[i] in VOWELS:
            p[i] = p[i].upper()
    return l.join(p)
# keep this function call here  
print Letter_Changes(raw_input())