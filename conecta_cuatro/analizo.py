def fila(p,i,b,s):
    cs=0 # Contador de fichas seguidas.
    CF=0
    CH=0
    aux_cs=0
    for j in range(1,8):
        m=j,i
        if m in s.moves:
            CH+=1
            aux_cs=cs
            cs=0
        elif b[m]==p:
            CF+=1
            cs+=1
        else:
            CF=0
            CH=0
            cs=0
            aux_cs=0
        if cs==3 and CH>0:
            return 950,CH
        if CF==3 and CH>0 and (cs==2 or aux_cs==2):
            return 950,CH    
        if CH+CF>3:
            if cs>=aux_cs:
                return cs,CH
            else:
                return aux_cs,CH
    return 0,CH        

def columna(p,i,b,s):
    CF=0
    j=0
    for j in range(1,7):
        m=i,j
        if m in s.moves:
            break
        elif b[m]==p:
            CF+=1
        else:
            CF=0
        if CF==3 and 6-j>0:
            return 950
    if CF+7-j>3:
        return CF
    return 0 