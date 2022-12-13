from time import localtime, strftime

format_time = lambda t : strftime("%H:%M:%S", t)

def build_logger(name):
    def logger(*messages):
        """
      to help with testing - returns logger (string) with time (that program was run) and message
      """
        current_time_string = format_time(localtime())
        single_message = " ".join(map(str, messages))
        print(f"{current_time_string} [{name}] {single_message}")
    return logger