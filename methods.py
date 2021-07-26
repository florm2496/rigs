import sys
import subprocess
import os

def apagar():
    if sys.platform == 'win32':

        import ctypes
        user32 = ctypes.WinDLL('user32')
        user32.ExitWindowsEx(0x00000008, 0x00000000)

    else:

        
        os.system('Sudo shutdown now')
    


def reiniciar():
    if sys.platform == 'win32':
        subprocess.run("shutdown -r")
        estado='Reiniciado en windows'
    else:
        subprocess.run("shutdown -r")
        estado='Reiniciado en linux'
    return estado