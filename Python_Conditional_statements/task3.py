#Simulate traffic light:RED=Stop,YELLOW=Wait,GREEN=Go.

Traffic_light=(input("Which light you see (RED,YELLOW,GREEN) :")).upper()

if Traffic_light=="RED":
    print("STOP")
elif Traffic_light=="YELLOW":
    print("WAIT")
elif Traffic_light=="GREEN":
    print("GO")