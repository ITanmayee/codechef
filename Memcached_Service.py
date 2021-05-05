"""

Chef is a programmer. In his computer, he is running a caching service, Memcached. He can give the commands "start", "restart" or "stop" to the service, the functionalities of which are specified below.

"start": Start the service.
"restart": If the service is started, do nothing. Otherwise, start the service.
"stop": If the service is not running, give an error. Otherwise, stop the service.

The service is initially not running. You are given n commands that he then gives to the program in sequence. Your task is to identify whether some error/s were encountered while running these commands.

"""


def error(commands):
    start = 0
    for i in commands:
        if i == "start" or i == "restart":
            start = 1
        if i == "stop":
            if start == 1:
                start = 0
            else:
                return "404"
    return  "200"

for _ in range(int(input())):
    no_of_commands = int(input())
    commands = input().split()
    print(error(commands))
