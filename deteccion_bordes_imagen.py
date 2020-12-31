from PIL import Image
import math
ancho, alto = 0,0
def resalteborde(img,H,V):
     # el valor de la matriz de la mascara
    Ha,Hb,Hc = H[0][0],H[0][1],H[0][2]
    Hd,He,Hf = H[1][0],H[1][1],H[1][2]
    Hg,Hh,Hi = H[2][0],H[2][1],H[2][2]
    
    Va,Vb,Vc = V[0][0],V[0][1],V[0][2]
    Vd,Ve,Vf = V[1][0],V[1][1],V[1][2]
    Vg,Vh,Vi = V[2][0],V[2][1],V[2][2]
    salida = Image.new("L",(ancho,alto))
    for i in range(2,img.size[0]-1):
        for j in range(2,img.size[1]-1):
              # valor de la porcion de la imagen
            Ia,Ib,Ic = float(img.getpixel((i-1,j-1))), float(img.getpixel((i-1,j))), float(img.getpixel((i-1,j+1)))
            Id,Ie,If = float(img.getpixel((i,j-1))), float(img.getpixel((i,j))), float(img.getpixel((i,j+1)))
            Ig,Ih,Ii = float(img.getpixel((i+1,j-1))), float(img.getpixel((i+1,j))), float(img.getpixel((i+1,j+1)))
            Gx = Ia*Ha+Ib*Hb+Ic*Hc+Id*Hd+Ie*He+If*Hf+Ig*Hg+Ih*Hh+Ii*Hi
            Gy = Ia*Va+Ib*Vb+Ic*Vc+Id*Vd+Ie*Ve+If*Vf+Ig*Vg+Ih*Vh+Ii*Vi
            q = int (math.sqrt(Gx*Gx+Gy*Gy))
            salida.putpixel((i,j),q)
    return salida
    
imgGray = Image.open("snoopygris.jpg").convert("L") # imagen original 
imgGray.show()

ancho,alto = imgGray.size
# borde 1
PrewittX = [[-1.0,0.0,1.0],
            [-1.0,0.0,1.0],
            [-1.0,0.0,1.0]]
PrewittY = [ [1.0,1.0,1.0],
            [0.0,0.0,0.0],
            [-1.0,-1.0,-1.0]]
# borde 2
SobelX = [[1.0,0.0,-1.0],
            [2.0,0.0,-2.0],
            [1.0,0.0,-1.0]]
SobelY = [ [-1.0,-2.0,-1.0],
            [0.0,0.0,0.0],
            [1.0,0.0,1.0]]
# borde 3
RobertX = [[0.0,0.0,0.0],
            [0.0,1.0,0.0],
            [0.0,0.0,-1.0]]
RobertY = [ [0.0,0.0,0.0],
            [0.0,0.0,1.0],
            [0.0,-1.0,0.0]]

resultado = resalteborde(imgGray,RobertX,RobertY) # eligiendo el tipo de resalte de borde
                                                  # como ejemplo utilize el borde 3
resultado.save("Prewitt.tiff") 
resultado.show() # mostrando la imagen con el borde 
