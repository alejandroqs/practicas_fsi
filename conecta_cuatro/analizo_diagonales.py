def diagonal(p,b,s):
        aux_m=0
        e=0
        
        # Recorrido con columnas como referencia #
        for i in range(4,7):
            x = i
            y = 1
            CH=0
            CF=0
            CS=0
            AUX_CS=0
            
            # Recorre cada diagonal: #
            while x>0:
                m=x,i
                
                if m in s.moves:
                    CH+=1
                    AUX_CS=CS
                    CS=0
                elif b[m]==p:
                    CF+=1
                    CS+=1
                else:
                    CF=0
                    CS=0
                    AUX_CS=0
                    CH=0
                if CS==3 and CH>0:
                    return 950
                if CF+CH>3:
                    e+=1
                x = x - 1
                y = y + 1
            if AUX_CS>CS and AUX_CS>aux_m:
                aux_m=AUX_CS
            elif AUX_CS<CS and AUX_CS>aux_m:
                aux_m=CS
        
        # Recorrido con filas como referencia #
        for j in range(1,4):
            x = 7
            y = j
            CH=0
            CF=0
            CS=0
            AUX_CS=0
            
            # Recorre cada diagonal: #
            while y < 7:
                m=x,y
                
                if m in s.moves:
                    CH+=1
                    AUX_CS=CS
                    CS=0
                elif b[m]==p:
                    CF+=1
                    CS+=1
                else:
                    CF=0
                    CS=0
                    AUX_CS=0
                    CH=0
                if CS==3 and CH>0:
                    return 950
                if CF+CH>3:
                    e+=1
                x = x - 1
                y = y + 1
                if AUX_CS>CS and AUX_CS>aux_m:
                    aux_m=AUX_CS
                elif AUX_CS<CS and AUX_CS>aux_m:
                    aux_m=CS
        if e>0:
            return aux_m
        return 0    
            
def diagonal_inversa(p,b,s):
        aux_m=0
        e=0
        
        # Recorrido con filas como referencia #
        for j in range(3,0,-1):
            x = 1
            y = j
            CH=0
            CF=0
            CS=0
            AUX_CS=0
            
            # Recorre cada diagonal: #
            while y < 7:
                m=x,y
                
                if m in s.moves:
                    CH+=1
                    AUX_CS=CS
                    CS=0
                elif b[m]==p:
                    CF+=1
                    CS+=1
                else:
                    CF=0
                    CS=0
                    AUX_CS=0
                    CH=0
                if CS==3 and CH>0:
                    return 950
                if CF+CH>3:
                    e+=1
                x = x + 1
                y = y + 1
                if AUX_CS>CS and AUX_CS>aux_m:
                    aux_m=AUX_CS
                elif AUX_CS<CS and AUX_CS>aux_m:
                    aux_m=CS
        
        # Recorrido con columnas como referencia #
        for i in range(2,5):
            x = i
            y = 1
            CH=0
            CF=0
            CS=0
            AUX_CS=0
            
            # Recorre cada diagonal: #
            while x < 8:
                m=x,y
                if m in s.moves:
                    CH+=1
                    AUX_CS=CS
                    CS=0
                elif b[m]==p:
                    CF+=1
                    CS+=1
                else:
                    CF=0
                    CS=0
                    AUX_CS=0
                    CH=0
                if CS==3 and CH>0:
                    return 950
                if CF+CH>3:
                    e+=1
                x = x + 1
                y = y + 1
            if AUX_CS>CS and AUX_CS>aux_m:
                aux_m=AUX_CS
            elif AUX_CS<CS and AUX_CS>aux_m:
                aux_m=CS
        
        if e>0:
            return aux_m
        return 0