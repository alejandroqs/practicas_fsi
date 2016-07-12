import analizo
import games
import random
import analizo_diagonales
#from utils import *

def memoize(e):
    memo={}
    def auxiliar(state):
        strBoard = str(state.board)
        if strBoard not in memo:
            memo[strBoard] = e(state)
        return memo[strBoard]   
    return auxiliar

@memoize
def e(state):
    hjp=h('X',state.board,state)
    if hjp==950:
       return 200
    hjc=h('O',state.board,state)    
    if hjc==950:
        return -200
    return hjp-hjc    
def h(p,b,s):
    vf=0
    vp=1
    for i in range(1,7):
        aux_vf,h=analizo.fila(p,i,b,s)
        if aux_vf==950:
            return 200
        vf+=vp*aux_vf
        vp-=1/6
        if h==7:
            break
    vc=0
    vp=1
    for i in range(1,8):
        aux_vc=analizo.columna(p,i,b,s)
        if aux_vc==950:
            return 200
        vc+=vp*aux_vc
        vp=-1/6
    vd1=analizo_diagonales.diagonal(p,b,s)
    if vd1==950:
        return 200
    vd2=analizo_diagonales.diagonal_inversa(p,b,s)
    if vd1==950:
        return 200
    return 3*vf+vc+4*(vd1+vd2)
    
def m(state):
    if state.utility !=0:
        return 1000*state.utility
    vmemo=memoize(e)
    return vmemo(state)