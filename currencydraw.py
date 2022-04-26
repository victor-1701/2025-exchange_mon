import os
from datetime import datetime

if os.name == 'nt':

    from ctypes import windll, Structure, c_short, c_char_p

    STD_OUTPUT_HANDLE = -11

    class COORD(Structure):
        pass

    COORD._fields_ = [("X", c_short), ("Y", c_short)]


def currencydraw(input_buffer):
    def print_at_win(r, c, s):
        h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))

        c = s.encode("windows-1252")
        windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)

    def print_at_sh(r, c, s):
        print(s)

    def make_label():
        now = datetime.now()
        current_time = now.strftime("%y-%m-%d %H:%M:%S")

        return "Cotizacion de las: {hora}".format(hora=current_time)

    def make_output_buffer(input_buffer):
        def make_line(position=0, size=80):
            linechars = [
                ['+', '+'],
                ['+', '+'],
                ['+', '+']
            ]

            linechar = linechars[position]

            return ' ' + linechar[0] + '-' * (size + 2) + linechar[1]

        def make_linetext(line, size=80):

            return ' | ' + line.ljust(size) + ' | '

        output_buffer = []

        longest_line = max(input_buffer, key=len)
        line_len = len(longest_line)

        output_buffer.append(make_line(0, line_len))
        first = True
        for line in input_buffer:
            output_buffer.append(make_linetext(line, line_len))
            if first:
                first = False
                output_buffer.append(make_line(1, line_len))

        output_buffer.append(make_line(2, line_len))

        return output_buffer

    def print_on_screen(buffer):
        currentLine = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        for line in buffer:
            currentLine += 1
            if os.name == 'nt':
                print_at_win(currentLine, 3, line)
            else:
                print_at_sh(currentLine, 3, line)

    output_buffer = make_output_buffer(
        [make_label()]
        + input_buffer
    )

    output_buffer.append("\n  Presione cualquier tecla para salir")

    print_on_screen(output_buffer)
