# winbot/windows.py
# librerias importantes
import win32api
import win32con


class MouseBot:

    def __init__(self):
        print('MouseBot se iniciado con exitos')

    def getPosition(self):
        # tomara posicion actual el raton
        pos = win32api.GetCursorPos()
        return pos

    def move(self, x, y):
        NewPos = [x, y]
        win32api.SetCursorPos(NewPos)

    def click(self, button):
        # button es un valor y depende de que boton del mouse queres que semueva 1 izq 2 der
        clickAction = 2 ** (2 * button) - 1
        x = self.getPosition()[0]
        y = self.getPosition()[1]
        win32api.mouse_event(clickAction, x, y)

    def scroll(self, vertical=None, horizontal=None):
        if horizontal is not None:
            horizontal = int(horizontal)
            if horizontal == 0:  # scroll es igual a 0 no pasa nada
                pass
            elif horizontal > 0:  # scroll hacia la derecha si es positivo
                for _ in range(horizontal):
                    win32api.mouse_event(0x0100, 0, 0, 120, 0)
            else:  # scroll hacia la izquierda
                for _ in range(abs(horizontal)):
                    win32api.mouse_event(0x0100, 0, 0, -120, 0)
        if vertical is not None:
            vertical = int(vertical)
            if vertical == 0:
                pass
            elif vertical > 0:
                for _ in range(vertical):
                    win32api.mouse_event(0x0800,0,0,120,0)
            else:
                for _ in range(abs(vertical)):
                    win32api.mouse_event(0x0800,0,0,-120,0)

