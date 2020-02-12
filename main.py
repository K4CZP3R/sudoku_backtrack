from time import sleep, time
from os import system

grid = [
    [0, 0, 0, 0, 0, 7, 0, 1, 0],
    [0, 0, 4, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 0, 2, 0, 4],
    [9, 0, 0, 0, 7, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 9, 0, 2, 6],
    [4, 0, 0, 0, 0, 0, 8, 0, 0],
    [6, 5, 0, 0, 0, 2, 0, 0, 9],
    [0, 0, 0, 0, 9, 8, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 3, 0]
]


def print_number(_number):
    print(f" {_number} ", end="")


def print_changed_number(_number):
    print(f">{_number}<", end="")


def print_v_separator():
    print(" | ", end="")


def print_h_separator():
    print(f"{'-'*36}")


def point_out_changes(_grid, _x, _y, _new_val):
    system("cls")
    for y in range(0, 9):
        for x in range(0, 9):
            print_changed_number(grid[y][x]) if (
                _x == x and _y == y) else print_number(grid[y][x])

            if x % 3 == 2:
                print_v_separator()
            if(x == 8):
                print()
        if y % 3 == 2:
            print_h_separator()


def show_grid(_grid):
    system("cls")
    for y in range(0, 9):
        for x in range(0, 9):
            print_number(grid[y][x])

            if x % 3 == 2:
                print_v_separator()
            if(x == 8):
                print()
        if y % 3 == 2:
            print_h_separator()


def is_possible(_grid, _x, _y, _val):
    vals_in_vertical_line = list()
    vals_in_horizontal_line = list()
    vals_in_box = list()

    # vert
    for i in range(0, 9):
        v = _grid[i][_x]
        if v == 0:
            continue
        vals_in_vertical_line.append(v)
    # hor
    for i in range(0, 9):
        v = _grid[_y][i]
        if v == 0:
            continue
        vals_in_horizontal_line.append(v)
    # box
    # which box number (x)
    x_b_number = _x//3
    x_b_start = x_b_number * 3

    y_b_number = _y//3
    y_b_start = y_b_number * 3

    for x in range(0, 3):
        for y in range(0, 3):
            if _grid[y_b_start+y][x_b_start+x] == 0:
                continue
            vals_in_box.append(_grid[y_b_start+y][x_b_start+x])
    #print(f"In box: {vals_in_box}" )
    #print(f"Vert: {vals_in_vertical_line}")
    #print(f"Hor:  {vals_in_horizontal_line}")

    if _val in vals_in_vertical_line:
        return False
    if _val in vals_in_horizontal_line:
        return False
    if _val in vals_in_box:
        return False
    return True


show_grid(grid)
calls = 0


def execute():
    global calls
    calls += 1
    for y in range(0, 9):
        for x in range(0, 9):
            g_val = grid[y][x]
            if g_val == 0:
                for i in range(1, 10):
                    pos = is_possible(grid, x, y, i)
                    if pos:
                        grid[y][x] = i
                        #point_out_changes(grid, x, y, i)
                        # print(calls)
                        # sleep(0.001)
                        execute() #Continue with this setting, but if it returns, reset to 0 and add 1 up
                        grid[y][x] = 0
                return

    print("="*32)
    show_grid(grid)
    end = time()
    print(f"Rec calls: {calls}")
    print(f"Solving took: {end-start}s")


start = time()
execute()
