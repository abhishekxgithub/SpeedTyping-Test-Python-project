from time import time
import random as r 


def mistake (paratest, usertest):
    error =0
    for i in range (len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                error=error+1
        except:
            error=error+1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s 
    time_r =round(time_delay,2)
    speed = len(userinput)/time_r
    return round(speed)
if __name__== '__main__':
    while True:
        check=input("Ready to take the test (Yes/No):")
        if check =="yes":
            test =["Hey there this is an  era of dancing ", "Any body is singing this song can also dance as well", " Hey there i am a programmer and can solve your every day programming related problems"]
            test1= r.choice(test)
            print("***** Typing speed *****")
            print(test1)
            print()
            print()
            time_1 = time()
            testinput =input( "Enter :")
            time_2 = time()
            print("Speed : " , speed_time(time_1,time_2,testinput)," words/sec")
            print("Error: ", mistake(test1, testinput))
        elif check== "no":
            print("thank you ")
            break
        else:
            print("wrong input")    

