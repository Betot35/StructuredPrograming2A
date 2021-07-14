import sys
import random as rd 



myList = list()
otherlist =[]  
myInt=3

def isAnyUpper (str):
        for element in str:
                if element.isupper():
                        return True
        return False

if __name__ =="__main__":
    print("DataStructures!")
    print(type(myList)) 
    print(type(otherlist))
    print(type(myInt))
    myList.append ("Data1")
    myList.append ("Data2")
    myList.append ("Data3")
    myList.append ("Data4")
    myList.append ("Data5")


    for index in range(0, len(myList)):
            print(f'Mylist[{index}]:',myList[index],",Current Index:", index) 

    for iteracion in range(0, 11):
            otherlist.append(rd.randint(0,100))
    print(otherlist)

    myList.extend(otherlist)
    print(myList)

  
    myList.reverse() 
    print(myList)

    newlist =myList[0::5] 
    print(newlist)

    usersAdmin =["Luis","Rafa","Jose","Fernando","Ricardo"]
    print(usersAdmin)
    print(usersAdmin[0].lower()) 
    
   

    for usuario in usersAdmin:                   
            print(usuario, type(usuario))


    for element in range(0,len(usersAdmin)): 
            if (isAnyUpper(usersAdmin[element])):
                print(f'usersAdmin[{element}] modificated')
                usersAdmin[element] = usersAdmin[element].lower()  
                

    print(usersAdmin) 

         


    sensor = "$GPGGA,134658.00,5106.9792,N,11402.3003,W,2,09,1.0,1048.47,M,16.27,M,08,AAAA*60"
        
       
    strVariable = "ThisIsAnApple"
    newString  =  strVariable[::-1]
    print(   f'strVariable[{1}]: {strVariable[1]}' )
    print(   f'newString: {newString}' )
       
    listaSensor =   sensor.split(   ","  )
    hr = listaSensor[1][:2]
    min =  listaSensor[1][2:4]
    sec = listaSensor[1][4:6]
     
    listaSensor[1] = f'hr: {hr}, min: {min}, sec: {sec}'
    print(listaSensor)
    
    sensorFixed  = ",".join(listaSensor)
    print(sensorFixed)