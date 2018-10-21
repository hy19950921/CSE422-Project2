/***** SAMPLE README *****/
Name: Yu Han
PID: A49129859
Machines Tested On: arctic

/**** Comments *****/
Code all appears to work as described in the handout. Had no issues in completing all assigned tasks.


/***** Sample Server Output *****/
<129 arctic:~ >cd project2
<130 arctic:~/project2 >python3 server.py -r
Server is running...
Creating TCP socket...
TCP socket has port number: 52611
Waiting for a client...
new connection from 52654
User' name: hanyu2
Creating UDP socket...
Sending UDP port number to client using TCP connection...
ready
Hidden Word: their
Starting game...
Sending message: stat Word: ----- Attempts left: 5
guess t
Correctly guessed char
Attempts left: 5
Win status: False
Sending message: stat Word: t---- Attempts left: 5
guess h
Correctly guessed char
Attempts left: 5
Win status: False
Sending message: stat Word: th--- Attempts left: 5
guess e
Correctly guessed char
Attempts left: 5
Win status: False
Sending message: stat Word: the-- Attempts left: 5
guess i
Correctly guessed char
Attempts left: 5
Win status: False
Sending message: stat Word: thei- Attempts left: 5
guess r
Correctly guessed char
Attempts left: 5
Correctly guessed word
Win status: True
ready
Hidden Word: pound
Starting game...
Sending message: stat Word: ----- Attempts left: 5
guess p
Correctly guessed char
Attempts left: 5
Win status: False
Sending message: stat Word: p---- Attempts left: 5
guess a
Incorrectly or already guessed char
Attempts left: 4
Win status: False
Sending message: stat Word: p---- Attempts left: 4
guess b
Incorrectly or already guessed char
Attempts left: 3
Win status: False
Sending message: stat Word: p---- Attempts left: 3
guess c
Incorrectly or already guessed char
Attempts left: 2
Win status: False
Sending message: stat Word: p---- Attempts left: 2
guess s
Incorrectly or already guessed char
Attempts left: 1
Win status: False
Sending message: stat Word: p---- Attempts left: 1
guess a
Incorrectly or already guessed char
Attempts left: 0
Win status: False
ready
Hidden Word: shop
Starting game...
Sending message: stat Word: ---- Attempts left: 5
end
bye
disconnect this user


/***** Sample Client Output *****/
<129 arctic:~ >cd project2
<130 arctic:~/project2 >python3 client.py arctic.cse.msu.edu 52611
Client is running...
Remote host: arctic.cse.msu.edu, remote TCP port: 52611
Input your user name: hanyu2
Server IP is 127.0.1.1
portUDP 41738
recv from the server: portUDP 41738
>start
This is hangman. You will guess one letter at a time. If the letter is in
the hidden word, the "-" will be replaced by the correct letter. Guessing multiple letters at
a time will be considered as guessing the entire word (which will result in either a win
or loss automatically - win if correct, loss if incorrect). You win if you either guess all of
the correct letters or guess the word correctly. You lose if you run out of attempts. Attempts
will be decremented in the case of an incorrect or repeated letter guess.


Word: -----, Attemps Left: 5
>guess t
Word: t----, Attemps Left: 5
>GuESS h
Word: th---, Attemps Left: 5
>guess e
Word: the--, Attemps Left: 5
>guess i
Word: thei-, Attemps Left: 5
>guess r
You win. The word is 'their'
>start
This is hangman. You will guess one letter at a time. If the letter is in
the hidden word, the "-" will be replaced by the correct letter. Guessing multiple letters at
a time will be considered as guessing the entire word (which will result in either a win
or loss automatically - win if correct, loss if incorrect). You win if you either guess all of
the correct letters or guess the word correctly. You lose if you run out of attempts. Attempts
will be decremented in the case of an incorrect or repeated letter guess.


Word: -----, Attemps Left: 5
>guess p
Word: p----, Attemps Left: 5
>guess a
Word: p----, Attemps Left: 4
>guess b
Word: p----, Attemps Left: 3
>guess c
Word: p----, Attemps Left: 2
>guess s
Word: p----, Attemps Left: 1
>guess a
You lose since you run out of attempts. The word is 'pound'
>end
Game is not active yet. Start a game using command 'start'
>start
This is hangman. You will guess one letter at a time. If the letter is in
the hidden word, the "-" will be replaced by the correct letter. Guessing multiple letters at
a time will be considered as guessing the entire word (which will result in either a win
or loss automatically - win if correct, loss if incorrect). You win if you either guess all of
the correct letters or guess the word correctly. You lose if you run out of attempts. Attempts
will be decremented in the case of an incorrect or repeated letter guess.


Word: ----, Attemps Left: 5
>end
You lose! the word is 'shop'
>exit
Closing TCP and UDP sockets...
