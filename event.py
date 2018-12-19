def game_starting(game_name):
    print("Starting game " + game_name)

def select_number(server):
    number = input("Please select your number...")
    server.send(str(number).encode())

def game_ended():
    return "finished"

def unpack(response):
    split_response = response.split(",")
    if(len(split_response) > 1):
        return split_response[0], split_response[1]
    else:
        return split_response[0], ""