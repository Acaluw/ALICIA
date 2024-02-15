# Importar librerias
import cv2
import webbrowser

# Función para abrir una página web en el navegador
def abrir_pagina_web(url):
    webbrowser.open(url)

# Inicializarmos la captura de la cámara
capture = cv2.VideoCapture(0)

# Bucle principal para capturar imágenes de la cámara
while capture.isOpened():
    # Leemos un nuevo fotograma de la cámara
    ret, frame = capture.read()
    
    # Detectamos y decodificamos si hay un posible código QR en el fotograma
    qrDetector = cv2.QRCodeDetector()
    data, bbox, rectifiedImage = qrDetector.detectAndDecode(frame)
    
    # Si se detecta un código QR
    if len(data) > 0:
        print(f'Dato: {data}')
        # Abrir la página web correspondiente al dato del código QR
        abrir_pagina_web(data)
        cv2.imshow('webCam', rectifiedImage)
    else: 
        # Si no se detecta un código QR, mostrar el fotograma original
        cv2.imshow('webCam', frame) 
    
    # Esperar hasta que se presione la tecla 'Esc' para salir del bucle
    if cv2.waitKey(1) == 27:  # 27 corresponde al código ASCII de la tecla 'Esc'
        break

# Liberamos la captura de la cámara y cerrar todas las ventanas
capture.release()
cv2.destroyAllWindows()
