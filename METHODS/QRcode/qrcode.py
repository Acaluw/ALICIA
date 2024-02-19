# Importar librerias
import cv2
import webbrowser

# Function to open a web page in the browser
def openUrl(url):
    webbrowser.open(url)

def qrSearch():
    # Detect and decode if there is a possible QR code in the frame
    frame = cv2.imread('TEMPFILES/images/productImg.png')
    qrDetector = cv2.QRCodeDetector()
    data, bbox, rectifiedImage = qrDetector.detectAndDecode(frame)
    # If a QR code is detected
    if len(data) > 0:
        print(f'Dato: {data}')
        # Open the corresponding web page for the QR code data
        openUrl(data)

if __name__ == '__main__':
    qrSearch()