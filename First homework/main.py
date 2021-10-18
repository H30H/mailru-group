class TicTacToe:
    """
    Its a class for TicTacToe game with field size 3*3
    """
    def __init__(self):
        self.__p1 = 'X'
        self.__p2 = 'Y'
        self.__size = 3
        self.__count = 3  # count to win in 1 line
        self.__whose_last_turn = False  # True = player1, False = player2
        self.__map = [' ' for _ in range(self.__size ** 2)]
        self.__turns = 0

    def __check_coords(self, x_coord: int, y_coord: int) -> bool:
        return 0 <= x_coord < self.__size and 0 <= y_coord < self.__size

    def __get_coord(self, x_coord, y_coord):
        return x_coord + y_coord * self.__size

    def turn(self, x_coord: int, y_coord: int) -> bool:
        """
        Its a method for player turn (player name switch automatically).
        :param x_coord: column of player turn (:raise ValueError: if there isn`t this column)
        :param y_coord: row of player turn (:raise ValueError: if there isn`t this row)
        :return: True if game has won by someone of False (:raise Warning: if game ended by tiy)
        """
        if x_coord < 0 or x_coord >= self.__size:
            raise ValueError('Invalid x coordinate')
        if y_coord < 0 or y_coord >= self.__size:
            raise ValueError('Invalid y coordinate')

        if self.__map[self.__get_coord(x_coord, y_coord)] != ' ':
            raise ValueError('Invalid turn')
        self.__whose_last_turn = not self.__whose_last_turn

        if self.__whose_last_turn:
            self.__map[self.__get_coord(x_coord, y_coord)] = self.__p1
        else:
            self.__map[self.__get_coord(x_coord, y_coord)] = self.__p2

        self.__turns += 1
        if self.__turns == self.__size ** 2:
            if self.__check_win(x_coord, y_coord):
                return True
            raise Warning('The game ended in a draw')
        return self.__check_win(x_coord, y_coord)

    def __check_win_delta(self, x_coord: int, y_coord: int, delta_x: int, delta_y: int) -> bool:
        player = self.__map[self.__get_coord(x_coord, y_coord)]
        count = 0

        while self.__map[self.__get_coord(x_coord, y_coord)] == player:
            count += 1
            x_coord += delta_x
            y_coord += delta_y

            if count == self.__count:
                return True

            if not self.__check_coords(x_coord, y_coord):
                break

        x_coord -= delta_x * (count + 1)
        y_coord -= delta_y * (count + 1)

        if not self.__check_coords(x_coord, y_coord):
            return False

        while self.__map[self.__get_coord(x_coord, y_coord)] == player:
            count += 1
            x_coord -= delta_x
            y_coord -= delta_y

            if count == self.__count:
                return True

            if not self.__check_coords(x_coord, y_coord):
                break

        return False

    def __check_win(self, x_coord: int, y_coord: int) -> bool:
        if x_coord < 0 or y_coord < 0 or x_coord >= self.__size or y_coord >= self.__size:
            raise ValueError

        return self.__check_win_delta(x_coord, y_coord, 1, 0) or \
               self.__check_win_delta(x_coord, y_coord, 1, 1) or \
               self.__check_win_delta(x_coord, y_coord, 0, 1) or \
               self.__check_win_delta(x_coord, y_coord, 1, -1)

    @property
    def whose_turn(self) -> bool:
        """
        This method return boolean, that shows whose turn
        :return: True if player1 turn else False
        """
        return self.__whose_last_turn

    @property
    def map(self):
        """
        This method convert game field to string
        :return: string of converted game field
        """
        res = str()

        str1 = '─'
        for i in range(self.__size):
            str1 += '┼─'
        str1 += '\n'

        res += ' '
        for i in range(self.__size):
            res += '│' + str(i)
        res += '\n'

        for i in range(self.__size):
            res += str1
            res += str(i)
            coord = i * self.__size
            for j in range(self.__size):
                res += '│' + self.__map[coord + j]
            res += '\n'

        return res


def main():
    """
    Its a main function, that creates new game, reads coordinates of turn and makes a move
    :return: Nothing
    """
    field = TicTacToe()
    while True:
        print(field.map)
        print(f'Player{1 if field.whose_turn else 2} turn. '
              f'Enter x and y coordinates\n :')
        try:
            x_coord, y_coord = map(int, input().split())
            k = field.turn(x_coord, y_coord)

            if k:
                print(field.map, f'Player{1 if field.whose_turn else 2} has won!')
                break
        except ValueError as err:
            print(err)
        except Warning as err:
            print(field.map)
            print(err)
            break

    print('Do you want to try again? (yes | no)')

    if input() == 'yes':
        main()


if __name__ == '__main__':
    main()
