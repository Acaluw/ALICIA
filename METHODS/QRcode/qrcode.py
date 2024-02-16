# Importar librerias
import cv2
import webbrowser

# Función para abrir una página web en el navegador
def openUrl(url):
    webbrowser.open(url)

def qrSearch():
    # Detectamos y decodificamos si hay un posible código QR en el fotograma
    frame = cv2.imread('TEMPFILES/images/productImg.png')
    qrDetector = cv2.QRCodeDetector()
    data, bbox, rectifiedImage = qrDetector.detectAndDecode(frame)
    # Si se detecta un código QR
    if len(data) > 0:
        print(f'Dato: {data}')
        # Abrir la página web correspondiente al dato del código QR
        openUrl(data)

if __name__ == '__main__':
    qrSearch()