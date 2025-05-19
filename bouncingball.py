import os
import sys
import time

def get_terminal_size():
    try:
        return os.get_terminal_size()
    except OSError:
        return (80, 24)

def move_cursor(x, y):
    sys.stdout.write(f"\033[{y+1};{x+1}H")
    sys.stdout.flush()

def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def main():
    width, height = get_terminal_size()
    ball = 'O'
    x, y = 1, 1
    dx, dy = 1, 1

    hide_cursor()
    print("\033[2J", end='')  # Clear screen once

    try:
        while True:
            move_cursor(x, y)
            print(' ', end='')  # Erase old ball

            x += dx
            y += dy

            if x <= 0 or x >= width - 1:
                dx = -dx
            if y <= 0 or y >= height - 1:
                dy = -dy

            move_cursor(x, y)
            print(ball, end='')
            sys.stdout.flush()
            time.sleep(0.03)
    except KeyboardInterrupt:
        show_cursor()
        print("\nBouncing ball animation stopped.")
    finally:
        show_cursor()

if __name__ == "__main__":
    main()
