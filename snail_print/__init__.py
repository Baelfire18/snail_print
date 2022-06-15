from time import sleep
from os import get_terminal_size
from .utils import StdoutHandler

stdout_handler = StdoutHandler()
stdout_handler.start()


RLL = "\x1b[1A\x1b[2K"  # Remove Last Line


def __validate_arguments(delay: float, sep: str, end: str) -> None:
    delay_type = type(delay)
    if not (delay_type is float or delay_type is int):
        raise TypeError("Argument 'delay' must be a float")
    if type(sep) is not str:
        raise TypeError("Argument 'sep' must be a string")
    if type(end) is not str:
        raise TypeError("Argument 'end' must be a string")


def snail_print(*objects, delay: float = 0.1, sep: str = " ", end: str = "\n") -> None:
    __validate_arguments(delay, sep, end)
    try:
        height, _ = get_terminal_size()
    except OSError:
        height = 80

    prev_output = stdout_handler.get_last_output_line().strip(RLL)
    string = sep.join([str(i) for i in objects])
    string_len = len(string)

    for i in range(string_len):
        back_slash_n_count = string[0:i].count("\n")
        times_RLL = 1 + ((i - 1) // height) + back_slash_n_count
        string_frag = string[0 : i + 1]

        if i == 0 and prev_output:
            print(f"{RLL * times_RLL}{string_frag}")
        elif (i == string_len - 1) and end != "\n":
            print(f"{RLL * times_RLL}{prev_output + string_frag}", end=end)
        else:
            print(f"{RLL * times_RLL}{prev_output + string_frag}")
        sleep(delay)
