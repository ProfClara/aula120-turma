# Aula 120 - continuação da detecção de trajetória

# Começamos importando cv2
import cv2
# A variável video está carregando o vídeo da bola de basket
video = cv2.VideoCapture("bb3.mp4")
# Usamos o loop while para reproduzir cada frame
while True:
    check,img = video.read()   

    cv2.imshow("resultado",img)
    # Caso queira parar o vídeo antes de terminar         
    key = cv2.waitKey(25)

    if key == 32:
        print("Interrompido!")
        break

# Quando acabarem os frames do vídeo encerramos o loop
video.release()
cv2.destroyALLwindows()



