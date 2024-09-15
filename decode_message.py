#ID успешной посылки: 117905981

def get_decoded_message(coded_message: str) -> str:
    '''Функция, принимающая на вход закодированное сообщение,
    и возвращающая его раскодированным. В теле сохраняет в стэк последние
    найденные числа и команды внутри скобок с помощью буферов,
    а после нахождения закрывающей скобки записывает результат
    в конец переменной-раскодированного сообщения
    '''
    nums_of_message: int = 0
    message: str = ''
    symbols_stack: list = []
    for index in range(len(coded_message)):
        if coded_message[index] == '[':
            symbols_stack.append(nums_of_message)
            nums_of_message -= nums_of_message
            symbols_stack.append(message)
            message = ''
        elif coded_message[index] == ']':
            message = symbols_stack.pop() + \
                      (message * symbols_stack.pop())
        else:
            try:
                int(coded_message[index])
            except ValueError:
                message += coded_message[index]
            else:
                nums_of_message = int(coded_message[index]) + \
                                  (nums_of_message * 10)

    return message


if __name__ == '__main__':
    coded_message = input()
    print(get_decoded_message(coded_message))
