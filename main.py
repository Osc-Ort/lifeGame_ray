import pyray as rl

from lifeGameSim import lifeSim


def main():
    ROWS = 100
    COLS = 100

    CELL_SIZE = 10

    def obtenerCelda(x, y):
        col = x // CELL_SIZE
        row = y // CELL_SIZE
        if 0 <= col <= COLS and 0 <= row <= ROWS:
            return col, row
        return None

    colorFondo = rl.WHITE
    colorCasil = rl.BLUE

    parada = False

    estado = lifeSim(ROWS, COLS)

    rl.init_window(ROWS * CELL_SIZE, COLS * CELL_SIZE, "lifeSim")
    rl.set_target_fps(10)
    while not rl.window_should_close():
        if rl.is_key_pressed(rl.KeyboardKey.KEY_SPACE):
            parada = not parada

        if not parada:
            estado.step()
        else:
            mx, my = rl.get_mouse_x(), rl.get_mouse_y()
            if rl.is_mouse_button_down(rl.MouseButton.MOUSE_BUTTON_LEFT):
                c = obtenerCelda(mx, my)
                if c:
                    estado.pintarCelda(*c)
            if rl.is_mouse_button_down(rl.MouseButton.MOUSE_BUTTON_RIGHT):
                c = obtenerCelda(mx, my)
                if c:
                    estado.borrarCelda(*c)
            if rl.is_key_pressed(rl.KeyboardKey.KEY_E):
                estado.tablero[:, :] = False
        if rl.is_key_pressed(rl.KeyboardKey.KEY_Q):
            estado = lifeSim(ROWS, COLS)

        rl.begin_drawing()
        rl.clear_background(colorFondo)
        for i in range(ROWS):
            for j in range(COLS):
                if estado.tablero[i, j]:
                    x = i * CELL_SIZE
                    y = j * CELL_SIZE
                    rl.draw_rectangle(x, y, CELL_SIZE, CELL_SIZE, colorCasil)
        rl.end_drawing()
    rl.close_window()


if __name__ == "__main__":
    main()
