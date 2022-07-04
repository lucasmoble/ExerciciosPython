item_list=list(map(int, input().split()))

commands = {
    "exibir":   lambda : print(' '.join(map(str, sorted(item_list)))),
    "is_in_list":   lambda value: item_list.count(value),
    "adicionar":    lambda item : item_list.append(item),
    "remover":  lambda  item : item_list.pop(item_list.index(item)) if commands["is_in_list"](item) else print("código {} não encontrado".format(item))
}

while True:
    command = input().split()
    if command[0] == "encerrar":
        commands["exibir"]()
        break
    elif len(command) ==1:
        commands[command[0]]()
    else:
        commands[command[0]](int(command[1]))

