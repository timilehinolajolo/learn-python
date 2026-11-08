
# EXERCISE
# Start - to start the car
# Stop - to stop the car
# Quiz - to exit

#result
# I don't understand that.. (for a wrong input)
# car started. ready to go! (start)
# car stopped (stop)
# code stop (quit)

#Answer
i = 1
while i > 0:
    user_input = input('Enter Command: ')
    i += 1
    if user_input == 'start':
        print ('Car started... Ready to go!')
    elif user_input == 'stop':
        print ("Car Stopped.")
    elif user_input == "quiz":
        break
    else:
       print ("I don't understand that")



#Improved Solution
command = ""
started = False
while True:
    command = input ("> ").lower()
    if command == "start":
        if started:
            print('Car is already started!')
        else:
            started = True
        print ('Car started... Ready to go!')

    elif command == "stop":
        if not started:
            print('Car was already stopped!')
        else:
            started = False
        print ("Car Stopped.")

    elif command == "help":
         print ("""
         start - to start the car
         stop - to stop the car
         quit - to quit
         """)

    elif command == "quit":
        break

    else:
       print ("I don't understand that")
