from socket import *
from sys import argv
from random import *
from game import *

def main():
  # Parse command line args
  if len(argv) != 2:
    print("usage: python3 server.py <word to guess or '-r' for random word>")
    return 1
  guessword = argv[1]
  if guessword == '-r':
    guessword = ""
  print("Server is running...")

  # Create the TCP Socket
  print("Creating TCP socket...")
  s = socket(AF_INET, SOCK_STREAM)

  # Bind a name to the TCP socket, letting the OS choose the port number
  s.bind(('0.0.0.0', 0,))
  # Get the port number of the socket from the OS and print it
  address = s.getsockname()
  print("TCP socket has port number: %d"%address[1])
  # The port number will be a command-line parameter to the client program


  # Configure the TCP socket (using listen) to accept a connection request
  s.listen(1)
  try: # try/except to catch ctrl-c
    while True:
      # Accept the TCP Connection
      print("Waiting for a client...")
      conn, address = s.accept()
      print('new connection from '+str(address[1]))
      # TCP loop
      while True:
        # Continuously Read in from TCP port
        msg =  conn.recv(1024)
        msg = msg.decode('utf-8')
        msgs = msg.split()
        # Keep listening if it doesn't receive a hello message
        if 'hello' != msg[0:5]:
          continue

        # Extract username handling empty case
        try:
          usrname = msg.split()[1]
          print('User\' name: %s'%usrname)
        except IndexError:
          print('No username is contained')
          return

        # Create and bind a UDP socket, letting the OS choose the port number
        print("Creating UDP socket...")
        sudp = socket(AF_INET, SOCK_DGRAM)
        sudp.bind(('0.0.0.0',0,))
        # Add a timeout to the UDP socket so that it stops listening
        sudp.settimeout(120)
        # after 2 minutes of inactivity

        # Get the port number assigned by the OS and print to console
        conn2, address2 = sudp.getsockname()

        # Put the UDP port number in a message and send it to the client using TCP
        print("Sending UDP port number to client using TCP connection...")
        smsg = "portUDP %d"%(address2)
        conn.send(smsg.encode('utf-8'))

        # Break from loop once needed info is received
        break
      active = False # game not active by default

      # Game (UDP) loop
      while True:
        try:
          # receive on UDP port here
          msg2,cudpadd = sudp.recvfrom(1024)
          msg2 = msg2.decode('utf-8')
          msg2s = msg2.split()
          print(msg2)
        except timeout: # catch UDP timeout
          print("Ending game due to timeout...")
          break # break and wait to accept another client

        if 'ready' == msg2[0:5]:
          # Game setup
          active = True
          word, word_blanks, attempts, win = gameSetup(argv)
          print("Hidden Word: {}".format(word))
          print("Starting game...")

          # Send inst then stat messages
          smsg2 = "instr %s"%INSTRUCTIONS
          sudp.sendto(smsg2.encode('utf-8'),cudpadd)
          smsg3 = "stat %s %d"%(word_blanks, attempts)
          print('Sending message: stat Word: %s Attempts left: %d'%(word_blanks, attempts))
          sudp.sendto(smsg3.encode('utf-8'),cudpadd)


        elif 'guess' == msg2[0:5]  :
          guess = msg2.split()[1]
          word_blanks, attempts, win = checkGuess(word, word_blanks, attempts, guess, win)

          # Losing conditions - break if end
          if len(guess) > 1 and not win or attempts == 0 or win:
            # Handle win/lose conditions
            active = False
            smsg3 = "end "
            endmsg = " "
            if len(guess) > 1 and not win:
              endmsg = "You lose since you guess wrong."
            elif attempts == 0:
              endmsg = "You lose since you run out of attempts."
            else:
              endmsg = "You win."
            smsg3 = smsg3 + endmsg + " The word is \'%s\'"%word
            sudp.sendto(smsg3.encode('utf-8'), cudpadd)
          else:
            smsg3 = "stat %s %d" % (word_blanks, attempts)
            print('Sending message: stat Word: %s Attempts left: %d' % (word_blanks, attempts))
            ##print('Sending message: stat Word: %s Attempts left: %d' % (word_blanks, attempts))
            sudp.sendto(smsg3.encode('utf-8'), cudpadd)

        elif msg2s[0] == 'end':
          if active:
            smsg3 = 'end You lose! the word is \'%s\''%word
            sudp.sendto(smsg3.encode('utf-8'), cudpadd)
            active = False

        elif msg2s[0] == 'bye':
          active = False
          print('disconnect this user')
          conn.close()
          sudp.sendto('bye'.encode('utf-8'), cudpadd)
          break
        else:
          sudp.sendto('na'.encode('utf-8'), cudpadd)



        # always send a response message to the client


      # end of UDP Game loop
      # close the TCP socket the client was using as well as the udp socket.


    # end of TCP loop

  except KeyboardInterrupt:

    # Close sockets
    s.close()
    sudp.close()
    print("Closing TCP and UDP sockets...")


  ###########################################

if __name__ == "__main__":
  main()
