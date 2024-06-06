import curses

def main(stdscr):
    # Clear screen
    stdscr.clear()
    
    # Enable mouse events
    curses.mousemask(curses.ALL_MOUSE_EVENTS)
    
    # Instructions for quitting
    stdscr.addstr(0, 0, "Click anywhere or press 'q' to quit.")
    stdscr.refresh()

    while True:
        # Wait for an event
        key = stdscr.getch()
        
        # Handle mouse events
        if key == curses.KEY_MOUSE:
            _, mx, my, _, _ = curses.getmouse()
            # Display the mouse click position
            stdscr.addstr(1, 0, f"Mouse clicked at ({mx}, {my})")
            stdscr.refresh()
        
        # Exit if 'q' is pressed
        if key == ord('q'):
            break

# Run the curses program
curses.wrapper(main)

    
