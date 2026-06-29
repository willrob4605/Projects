activity={"Baseball":2,"Gym":5}
def addActivity(text,streak):
    activity[text]=streak
def viewAll():
    for key in activity:
        print(f"You have a streak of {activity[key]} days for {key}")
def viewAllInOrder(arr):
    for key in arr:
        print(f"You have a streak of {activity[key]} days for {key}")

#def readFromFile():
#def addToFile():
def sortByHighestStreak():
    temp=activity
    highest=0
    res=[]
    for i in range(len(activity)):
        highest=0
        for key in temp:
            if temp[key]>highest:
                highest=temp[key]
                result=key
        res.append(result)
        del temp[key]
    return res
def removeActivity(key):
    del activity[key]
    
#def deleteFromFile
def resetStreak(key):
    activity[key]+=1
def addToStreak(key):
    activity[key]+=1

    
choice=2
while choice !=1:
    print("Choose what to do.")
    print("1. Exit")
    print("2. Add new activity.")
    print("3. View Highest Streak")
    print("4. Remove Activity")
    print("Show all activities")
    choice=int(input())
    if choice==2:
        text=input("Whats the new activity? ")
        streak=input("Whats your current streak ")
        addActivity(text,streak)
    elif choice==3:
        arr=sortByHighestStreak()
        viewAllInOrder(arr)

    elif choice==4:
        viewAll()
        number=int(input("Which activty to remove? "))
        removeActivity(number)

