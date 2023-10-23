import pyautogui
import keyboard




altura = 600
largura = 500
captura = (400, 275, altura, largura)
ecra = pyautogui.screenshot(region=captura)


def indentify_v(imagem):
    altura_imagem, largura_imagem = imagem.size
    for x in range(0, altura):
        for y in range(0, largura):
            if imagem.getpixel((x, y)) == (255, 0, 0):
                return x, y


while not keyboard.is_pressed('m'):
    pixel_vermelho = indentify_v(ecra)
    if pixel_vermelho:
        pyautogui.moveTo(pixel_vermelho[0]+captura[0], pixel_vermelho[1]+captura[1])
        pyautogui.mouseDown()


    #pyautogui.sleep(0.016)
    ecra = pyautogui.screenshot(region=captura)


