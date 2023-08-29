import numpy as np
from typing import List, Tuple
from functools import reduce

class Board:
    def __init__(self):
        self.state = np.array([[0 for i in range(3)] for j in range(3)])
        self.spare = self._select_spare()

    def change(self, x, y, side):
        self.state[x][y] = side
        self.spare = self._select_spare()
        return self.state

    def _select_spare(self) -> List[Tuple]:
        self.spare = []
        for x, row in enumerate(self.state):
            for y, el in enumerate(row):
                if el == 0:
                    if any([el == 0 for el in row]):
                        self.spare.append((x, y))
        return self.spare

    def check_win(self):
        diag_sums = [sum([self.state[i][i] for i in range(2)]), sum([self.state[i][i] for i in range(2, 0, -1)])]
        vertical_sums = self.state.sum(axis=0)
        horiz_sums = self.state.sum(axis=1)
        sums = np.array([vertical_sums, horiz_sums] + diag_sums).flatten()

        if any([s in [-3, 3] for s in sums]):
            return True


class Agent:
    def __init__(self, side, board):
        self.side = side
        self.board = board

    def make_move(self, ai=False):
        spares = self.board.spare
        proba = 1 / len(spares)
        run = True
        while run:
            if not ai:
                for cell in spares:
                    if np.random.rand() >= proba:
                        continue
                    else:
                        print(cell[0], cell[1])
                        self.board.state = self.board.change(cell[0], cell[1], self.side)
                        run = False
                        break
            else:
                pass

    def ai(self):
        pass

    def minimax(self):
        pass


class User(Agent):
    def __init__(self, side, board):
        super().__init__(side, board)

    def make_move(self):
        x, y = self.input_xy()
        self.board.state = self.board.change(x, y, self.side)

    def input_xy(self):
        inp = input()
        x, y = map(int, inp.split(" "))
        return x, y


if __name__ == "__main__":

    def run_game(is_user=False):
        board = Board()
        agent: Agent = Agent(-1, board)
        if is_user:
            user: User = User(1, board)
        else:
            user: User = Agent(1, board)

        spares = len(board.spare)
        print(board.spare)
        while len(agent.board.spare) > 0 and len(user.board.spare) > 0:
            agent.make_move()
            print(agent.board.state)
            user.make_move()
            print(user.board.state)
            agent.board = user.board
            spares -= 2


    # run_game(True)

