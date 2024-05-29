import curses

def clear_input_buffer(stdscr):
    """Clear the input buffer."""
    stdscr.nodelay(True)  # No bloquear las llamadas a getch
    try:
        while stdscr.getch() != -1:
            pass
    except curses.error:
        pass
    stdscr.nodelay(False)  # Restaurar el comportamiento de bloqueo

def main(stdscr):
    # Inicializa curses
    curses.cbreak()
    stdscr.keypad(True)
    curses.noecho()

    stdscr.addstr(0, 0, "Presiona cualquier tecla y luego borra el buffer...")
    stdscr.refresh()

    # Espera una tecla
    stdscr.getch()

    # Borra el buffer de entrada
    clear_input_buffer(stdscr)

    stdscr.addstr(1, 0, "Buffer de entrada borrado. Presiona otra tecla para salir.")
    stdscr.addstr(0,0,chr(30))
    stdscr.refresh()

    # Espera otra tecla antes de salir
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
