activity={"Baseball":2,"Gym":5}
def addActivity(text,streak):
    activity[text]=streak
def viewAll():
    for key in activity:
        print(f"You have a streak of {activity[key]} days for {key}")

#def readFromFile():
#def addToFile():
#def sortByHighestStreak():
    #sorts the keys by highest streak
    #for loop that goes through all the keys in order
#def removeActivity
    #remove data given key
#def deleteFromFile
#def resetStreak()
    #set activity streak value to 0
#def addToStreak()
    #add 1 to current streak
choice=2
while choice !=1:
    print("Choose what to do.")
    print("1. Exit")
    print("2. Add new activity.")
    print("3. View Highest Streak")
    print("4. Remove Activity")
    if choice==2:
        text=input("Whats the new activity? ")
        streak=input("Whats your current streak ")
        addActivity(text,streak)
    elif choice==3:
        sortByHighestStreak()
    elif choice==4:
        viewAll()
        number=int(input("Which activty to remove? "))
        removeActivity(number)

