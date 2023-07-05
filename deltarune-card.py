#!/bin/python3
import sys

#There is a line of boxes, each with a symbol inside:
#[ a b x x y ]
#There is another empty line:
#[ _ _ _ _ _ ]
#And there are three buttons that manipulate it:
#a    x    swap
#Pressing "a" or "x" places an a or x on the leftmost unused space
#Pressing "swap" swaps each symbol on the line for its counterpart
#Counterparts are:
#a : b
#x : y
#Can you fill the empty line such that it matches the other's pattern?

initial_symbols =  ['a','x']
swapped_symbols =  ['b','y']
symbol_pairs = { k:v for k, v in zip(initial_symbols, swapped_symbols)}
symbol_pairs.update({v:k for k, v in symbol_pairs.items()})

def main():
    if len(sys.argv) > 1:
        target_pattern = sys.argv[1]
    else:
        eprint("Missing pattern argument")
        return

    solution = solve_for_target(target_pattern)
    # print(target_pattern)
    # print( simulate_solution(solution) )
    print(solution)


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def solve_for_target(target):
    #valid moves are any of the initial letters and "swap"
    solution = []
    num_swaps_even = True
    for i in reversed(range(0, len(target))):
        c = target[i]
        button = c
        if c in swapped_symbols:
            button = symbol_pairs[c]
        is_initial = c in initial_symbols

        if is_initial == num_swaps_even:
            solution.append(button)
        else:
            solution.append("swap")
            solution.append(button)
            num_swaps_even = not num_swaps_even
    return list(reversed(solution))

def simulate_solution(sol):
    target = []
    for button_press in sol:
        if button_press == "swap":
            for i in range(0, len(target)):
                target[i] = symbol_pairs[target[i]]
        else:
            target.append(button_press)
    return "".join(target)

if __name__ == '__main__':
    main()
