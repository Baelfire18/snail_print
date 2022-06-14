import sys


# https://stackoverflow.com/questions/72575956/how-to-get-last-python-output
class StdoutHandler:
    def __init__(self):
        self.last_output = ""
        self.list_all_output = []

    def start(self):
        self._handled_stdout = sys.stdout
        sys.stdout = self

    def write(self, data: str):
        # write(data="") is called for the end kwarg in print(..., end="")
        if data:
            self.last_output = data
            self.list_all_output.append(data)
            self._handled_stdout.write(data)

    def end(self):
        sys.stdout = self._handled_stdout

    def flush(self):
        self._handled_stdout.flush()

    def get_last_output_line(self):
        s = "".join(self.list_all_output)
        last_line = s.rsplit("\n", 1)[-1]
        return last_line


if __name__ == "__main__":
    stdout_handler = StdoutHandler()
    stdout_handler.start()

    print("Hello World")
    last_output_line = stdout_handler.get_last_output_line()
    print(repr(last_output_line))

    print("Hello World", end="")
    last_output_line = stdout_handler.get_last_output_line()
    print(repr(last_output_line))

    print("Hello", "World", end="")
    last_output_line = stdout_handler.get_last_output_line()
    print(repr(last_output_line))
