# --------------------------------------------------------------------------------
# 30/07/2022
# Juego mascota virtual con GUI.
# Librería empleada en GUI: tkinter
# 
# --------------------------------------------------------------------------------

from tkinter import *
import os


TITULO = "Tamagotchi"

# De pendiendo del SO el icono tiene que ser de un formato determinado
ICONO_LINUX = "assets/iconos/icono.png"
ICONO_WINDOWS = "assets/iconos/icono.ico"
SERVIDOR = "http://127.0.0.1:5000"


def cargarIcono():
   if os.name == 'nt':
      return ICONO_WINDOWS
   if os.name == 'posix':
      return ICONO_LINUX


# FUNCIÓN MAIN

if __name__ == "__main__":
   print("Tamagotchi arranca")

   # Agregar documentación a funciones
   cargarIcono.__doc__ = "Carga el icono de la app dependiendo del SO"
   # ----

   raiz = Tk()
   raiz.title(TITULO)

   # 1 es true, 0 false. Se pueden usar booleans también
   raiz.resizable(TRUE,TRUE)

   icono = cargarIcono()

   # raiz.iconbitmap(ICONO) # no me funciona (con Windows en teoría tiene que ir)
   # Solución encontrada: https://stackoverflow.com/questions/11176638/tkinter-tclerror-error-reading-bitmap-file
   img = PhotoImage(file = icono)
   raiz.tk.call('wm', 'iconphoto', raiz._w, img)

   # mainloop para que la ventana esté siempre escuchando
   raiz.mainloop()



# if __name__ == "__main__":
#    print("File two executed when ran directly")
# else:
#    print("File two executed when imported")
