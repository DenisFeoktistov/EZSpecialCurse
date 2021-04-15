from typing import List, Any


def enumerate_choice(options: List[Any], select_text: str,
                     error_text: str = "\nIncorrect input! Try again!",
                     input_text: str = "Your choice: ") -> Any:
    print(select_text)
    for i, option in enumerate(options):
        if isinstance(option, dict):
            pairs = list(zip(option.keys(), option.values()))
            print(f"\tOption {i + 1}: {pairs[0][0]}: {pairs[0][1]}")
            for pair in pairs[1:]:
                indent = ' ' * len(f'Option {i + 1}:')
                print(f"\t{indent} {pair[0]}: {pair[1]}")
        else:
            print(f"\tOption {i + 1}: {option}")
    print()
    inp = input(input_text)
    while not (inp.isdigit() and int(inp) in range(1, len(options) + 1)):
        print(error_text)
        inp = input(input_text)
    return options[int(inp) - 1]
