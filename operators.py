import os
try:
    from numba import njit
except ImportError:
    os.system('pip install numba')
    from numba import njit
cls = lambda: os.system('cls' if os.name == 'nt' else 'clear')
class lo:
    '''
    Looping mathematical operations
    '''
    def find_multiplier(start: float, toi: float, outputstr: bool) -> float:
        '''
        Starts from inputted value `start` and returns multiplier to arrive to `toi` from `start`
        '''
        mult = 0
        out = 0
        while not out >= toi:
            mult += 0.01
            out = start * mult
        offset = start * mult - toi
        ostr = f'Multiplier to reach {toi} from {start} is about {mult}.\nOffset is {offset}.\nExact multiplier is impossible to find due to INSANE wait time'
        if outputstr:
            return ostr
        else:
            return mult

class o():
    '''
    Mathematical operations
    '''
    def tan(x: float) -> float:
        import math
        return math.tan(x)

    def pi(digits: int) -> float:
        import os
        try:
            from mpmath import mp
        except ImportError:
            os.system('pip install mpmath')

        mp.dps = digits
        return mp.pi
    
    def pow(y1: float, y2: float) -> float:
        import math
        return math.pow(y1, y2)
