import numpy as np
import cv2


 #Classidicador
cascadeC = cv2.CascadeClassifier('cascade_c.xml')
cascadeR = cv2.CascadeClassifier('cascade_r.xml')

#imagem
imagem = cv2.imread('imagem/c1.jpg')
imagem2 = cv2.imread('imagem/r1.jpg')

#cinza
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cinza2 = cv2.cvtColor(imagem2, cv2.COLOR_BGR2GRAY)

#aplica o classificador
face1 = cascadeC.detectMultiScale(cinza, scaleFactor=1.09, minNeighbors=10)
face2 = cascadeR.detectMultiScale(cinza2, scaleFactor=1.09, minNeighbors=10)


#loop
for(x, y, w, h) in face1:
    dectada = cv2.rectangle(imagem, (x, x), (x + w, y + h), (255,0,0),2)

for(ex, ey, ew, eh) in face2:
    dectada2 = cv2.rectangle(imagem2, (ex, ex), (ex + ew, ey + eh), (255,0,0),2)

#final
while True:
    dectada == True
    print('Cubista')
    cv2.imshow('Window', imagem)

    dectada2 == True
    print('Renacentista')
    cv2.imshow('window', imagem2)
    cv2.waitKey()
    cv2.destroyAllWindows()
    break


