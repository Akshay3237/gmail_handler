
from input_handler import handle_input
from service_caller import service_call
if __name__ == '__main__':
    input_character = handle_input()
    print(input_character)
    service_call(input_character)
