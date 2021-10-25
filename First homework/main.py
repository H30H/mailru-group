class TicTacToe:
    """
    Its a class for TicTacToe game with field size 3*3
    """
    def __init__(self):
        self.p1 = 'X'
        self.p2 = '0'
        self.size = 3
        self.count = 3  # count to win in 1 line
        self.whose_last_turn = False  # True = player1, False = player2
        self.map = [' ' for _ in range(self.size ** 2)]
        self.turns = 0

    def __check_coords(self, x_coord: int, y_coord: int) -> bool:
        return 0 <= x_coord < self.size and 0 <= y_coord < self.size

    def __get_coord(self, x_coord, y_coord):
        return x_coord + y_coord * self.size

    def turn(self, x_coord: int, y_coord: int) -> bool:
        """
        Its a method for player turn (player name switch automatically).
        :param x_coord: column of player turn (:raise ValueError: if there isn`t this column)
        :param y_coord: row of player turn (:raise ValueError: if there isn`t this row)
        :return: True if game has won by someone of False (:raise Warning: if game ended by tiy)
        """
        if x_coord < 0 or x_coord >= self.size:
            raise ValueError('Invalid x coordinate')
        if y_coord < 0 or y_coord >= self.size:
            raise ValueError('Invalid y coordinate')
        if self.map[self.__get_coord(x_coord, y_coord)] != ' ':
            raise ValueError('Invalid turn')

        self.whose_last_turn = not self.whose_last_turn

        if self.whose_last_turn:
            self.map[self.__get_coord(x_coord, y_coord)] = self.p1
        else:
            self.map[self.__get_coord(x_coord, y_coord)] = self.p2

        self.turns += 1
        if self.turns == self.size ** 2:
            if self.__check_win(x_coord, y_coord):
                return True
            raise Warning('The game ended in a draw')
        return self.__check_win(x_coord, y_coord)

    def __check_win_delta(self, x_coord: int, y_coord: int, delta_x: int, delta_y: int) -> bool:
        player = self.map[self.__get_coord(x_coord, y_coord)]
        count = 0

        while self.map[self.__get_coord(x_coord, y_coord)] == player:
            count += 1
            x_coord += delta_x
            y_coord += delta_y

            if count == self.count:
                return True

            if not self.__check_coords(x_coord, y_coord):
                break

        x_coord -= delta_x * (count + 1)
        y_coord -= delta_y * (count + 1)

        if not self.__check_coords(x_coord, y_coord):
            return False

        while self.map[self.__get_coord(x_coord, y_coord)] == player:
            count += 1
            x_coord -= delta_x
            y_coord -= delta_y

            if count == self.count:
                return True

            if not self.__check_coords(x_coord, y_coord):
                break

        return False

    def __check_win(self, x_coord: int, y_coord: int) -> bool:
        if x_coord < 0 or y_coord < 0 or x_coord >= self.size or y_coord >= self.size:
            raise ValueError

        return self.__check_win_delta(x_coord, y_coord, 1, 0) or \
               self.__check_win_delta(x_coord, y_coord, 1, 1) or \
               self.__check_win_delta(x_coord, y_coord, 0, 1) or \
               self.__check_win_delta(x_coord, y_coord, 1, -1)

    @property
    def getMap(self):
        """
        This method convert game field to string
        :return: string of converted game field
        """

        str1 = '─'
        for i in range(self.size):
            str1 += '┼─'
        str1 += '\n'

        res = ' '
        for i in range(self.size):
            res += '│' + str(i)
        res += '\n'

        for i in range(self.size):
            res += str1
            res += str(i)
            coord = i * self.size
            for j in range(self.size):
                res += '│' + self.map[coord + j]
            res += '\n'

        return res


def main():
    """
    Its a main function, that creates new game, reads coordinates of turn and makes a move
    :return: Nothing
    """

    field = TicTacToe()
    while True:
        print(field.getMap)
        print(f'Player{2 if field.whose_last_turn else 1} turn. '
              f'Enter x and y coordinates\n: ', end='')
        try:
            x_coord, y_coord = map(int, input().split())

            if field.turn(x_coord, y_coord):
                print(field.getMap, f'Player{1 if field.whose_last_turn else 2} has won!')
                break
        except ValueError as err:
            print(err)
        except Warning as err:
            print(field.getMap)
            print(err)
            break

    print('Do you want to try again? (yes | no)')

    while True:
        user_input = input()
        if user_input == 'yes':
            main()
            break
        elif user_input == 'no':
            break
        else:
            print('Incorrect word, try again')


if __name__ == '__main__':
    class CustomList(list):
        pass
    c = CustomList()
    print(isinstance(c, list))
    main()
