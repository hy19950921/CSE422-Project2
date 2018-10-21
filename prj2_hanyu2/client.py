from socket import *
from sys import argv

def main():
  # Parse command line args
  if len(argv) != 3 or not argv[2].isdigit():
    print("usage: python3 client.py <server name> <server port>")
    return 1

  hostname, serverTCPPort = argv[1], int(argv[2])
  print("Client is running...")
  print("Remote host: {}, remote TCP port: {}".format(hostname, serverTCPPort))

  # Prompt user for their name
  usrname = input("Input your user name: ")
  # Create TCP socket
  s = socket(AF_INET, SOCK_STREAM)
  # Get IP address of server via DNS and print it
  serverIP = gethostbyname(hostname)
  print("Server IP is " + serverIP)
  # Connect to the server program
  s.connect((serverIP,serverTCPPort,))

  # Send hello message to the server over TCP connection
  hello_msg = "hello %s"%usrname
  s.send(hello_msg.encode('utf-8'))

  # TCP Loop
  while True:
    # Read in from TCP port
    msg = s.recv(1000)
    msg = msg.decode('utf-8')
    # Keep listening if it doesn't receive a portUDP message
    print(msg)
    if 'portUDP' not in msg:
      continue

    # Read the control message from the TCP socket and print its contents
    print("recv from the server: %s"%msg)
    udpPort = int(msg.split()[1])
    serverAddress = (serverIP, udpPort)
    # Break from loop once needed info is received

    break

  # Create a UDP socket
  sudp = socket(AF_INET, SOCK_DGRAM)
  serverAddress = (serverIP,udpPort)
  end = False # default end flag
  game_active = False
  # Game loop
  while True:
    # Prompt

    valid_commands = ['start', 'end', 'guess', 'exit']
    icommand = input('>').lower()
    commands = icommand.split()

    if commands[0] not in valid_commands:
      print('invalid message')
      continue
    if commands[0] == 'start':
      sudp.sendto('ready'.encode('utf-8'), serverAddress)
    elif commands[0] == 'end' and game_active:
      sudp.sendto('end'.encode('utf-8'), serverAddress)
    elif commands[0] == 'exit':
      sudp.sendto('bye'.encode('utf-8'), serverAddress)
    elif commands[0] == 'guess' and game_active:
      if len(commands) != 2:
        print('invalid guess')
        continue
      sudp.sendto(('guess %s'% commands[1]).encode('utf-8'),serverAddress)
    else:
      print('Game is not active yet. Start a game using command \'start\'')
      continue
    # UDP loop
    while True:
      # Continuously Read in from UDP port
      rmsg = sudp.recv(1000)
      rmsg = rmsg.decode('utf-8')
      rmsgs = rmsg.split()
      valid_msg_types = ["instr", "stat", "end", "na", "bye"]
      if rmsgs[0] not in valid_msg_types:
        print('invalid message')
        break
      # print message
      #print(rmsg)

      # Instruction message should be followed by stat message
      if rmsgs[0] == "instr":
        print(rmsg[7:])
        game_active = True
        continue


      # Break once receiving info and reprompt user
      if rmsgs[0] == 'stat':
        print('Word: %s, Attemps Left: %d'%(rmsgs[1], int(rmsgs[2])))
        break
      if rmsgs[0] == 'na':
        break
      if rmsgs[0] == 'end':
        print(rmsg[4:])
        game_active = False
        break
      if rmsgs[0] == 'bye':
        game_active = False
        end = True
        break

    if end:
      break

  # Close sockets
  print("Closing TCP and UDP sockets...")
  s.close()
  sudp.close()
 ###########################################

if __name__ == "__main__":
  main()
