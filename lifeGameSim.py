import numpy as np


class lifeSim:
    def __init__(self, m: int, n: int):
        # Creación aleatoria
        self.tablero = np.random.rand(m, n) >= 0.5
        # Bordes a False
        self.tablero[[0, m - 1], :] = False
        self.tablero[:, [0, n - 1]] = False
        self.dims = (n, m)

    def step(self):
        m, n = self.dims
        nextTablero = np.ndarray((m, n), dtype=bool)
        nextTablero[:, :] = False
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                s = (
                    np.sum(self.tablero[i - 1 : i + 2, j - 1 : j + 2])
                    - self.tablero[i, j]
                )
                if self.tablero[i, j] and 2 <= s <= 3:
                    nextTablero[i, j] = True
                elif not self.tablero[i, j] and s == 3:
                    nextTablero[i, j] = True
        self.tablero = nextTablero

    def pintarCelda(self, x, y):
        self.tablero[x, y] = True

    def borrarCelda(self, x, y):
        self.tablero[x, y] = False
