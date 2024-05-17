#implementing List functions
def ListData():
    
    lst = []
    #create new list
    def newlist(): 
        n = int(input("Enter size of list: "))
       
        for i in range(n):
            data = int(input("Enter integer element: "))
            lst.append(data)  
        print(lst)

    #display list
    def display():
        print("Elements in the list: ")
        print(lst)

    #extend()
    def extendlist():
        n = int(input("Enter size for new list: "))
        lst2 = []
        for i in range(n):
            data = int(input("Enter integer element: "))
            lst2.append(data) 
        lst.extend(lst2) 
        print("List after extending ")
        print(lst)

    #add at index insert()
    def insertat():
        data = int(input("Enter new element to insert "))
        pos = int(input("Enter position to insert element "))
        lst.insert(pos,data)
        print(lst)
    
    #remove by value
    def removeElement():

        d = int(input("Enter value to delete "))
        if d in lst:
            lst.remove(d)
            print("List after remove ",lst)
        else:
            print(d + "Not Fount")
    
   #remove by position
    def removebyindex():
        d = int(input("Enter index to delete "))
        popdata = lst.pop(d)
        print("List after remove ",lst)
        print("Deleted element" , popdata)
    
    
    #find element in list
    def findElement():

        d = int(input("Enter element to find "))
        if d in lst:
            ans = lst.index(d)
            print("Element is present at " , ans , "index ")
        else:
            print("Not found")

    #check occurance of element
    def checkoccur():
        d = int(input("Enter element "))
        count = lst.count(d)
        print(count," times ",d," present")

   #sort list in ascending order
    def sortlst():
        lst.sort()
        print("sorted list ",lst)
       

    #reverse list
    def reverselst():

        print("Original List")
        print(lst)
        lst.reverse()
        print("List after Reverse ",lst)

    #copy list
    def copylst():
        print("Original list ",lst)
        lst_copy = lst.copy()
        print("Copy of lst ",lst_copy)

    #clear
    def clearlst():
        lst.clear()
        print(lst)
    while True:  
        print("")  
        print("1:Create new list")
        print("2.Exted existing list")
        print("3:Displa List")
        print("4:Insert at index")
        print("5:Remove by value")
        print("6:Remove by index")
        print("7:To Find")
        print("8:Check Occurance of element")
        print("9:To Sort")
        print("10:To Revverse")
        print("11:To copy")
        print("12:to Clear")
        print("13:exit")
        print("")
        choice = int(input("Enter your choice "))
        if choice == 1:
            newlist()
            
        elif choice == 2:
                extendlist()

        elif choice == 3:
            display()
        elif choice == 4:
            insertat()
        elif choice == 5:
            removeElement()
        elif choice == 6:
            removebyindex()
        elif choice == 7:
            findElement()
        elif choice == 8:
            checkoccur()
        elif choice == 9:
            sortlst()
        elif choice == 10:
            reverselst()
        elif choice == 11:
            copylst()
        elif choice == 12:
            clearlst()
        elif choice == 13:
            break
        else:
            print("ENTER valid choice!!!")

#implementing 
def TupleData():
    
   
       
    #creating tuple
    def create():
        n = int(input("Enter size for tuple "))
        tplLst = []
        for i in range(n):
            data = input("Enter element for tuple ")
            tplLst.append(data)
        return tuple(tplLst)
        
    def Disply(tpl):
        print(tpl) 

    #counting occurance of element
    def Count(tpl):
        #print(tpl)
        d = input("Enter element ")
        ans = tpl.count(d)
        print(d," is ",ans," times in tuple")

    #get index of element
    def Index(tpl):
        d = input("Enter element to check ")
        if d in tpl:
            ans = tpl.index(d)
            print("Index of ",d,"is = ",ans)
        else:
            print("Not Found")
    
    while True:
        print("")
        print("1:creat new tuple")
        print("2:Count Occurance of")
        print("3:Find Index")
        print("4:Display Tuple")
        print("5:Exit")
        print("")
        choice = int(input("Enter your choice "))
        
        if choice == 1:
            tpl = create()
            print(tpl)
        elif choice == 2:
            Count(tpl)
        elif choice == 3:
            Index(tpl)
        elif choice == 4:
            Disply(tpl)
        elif choice == 5:
            break
        else:
            print("ENTER VALID CHOICE!!!")
            
#Implementing all set operations
def setData():
    Set = set()
    new_set = set()
    
    #create sets
    def newset():
        n = int(input("Enter size for set "))
        for i in range(n):
            d = int(input("Enter integer element for set "))
            Set.add(d)
        print(Set)
        
        n = int(input("Enter size for set which will used in union,intersection,update: "))
        for i in range(n):
         data = int(input("Enter integer element "))
         new_set.add(data)
        print(new_set)


    #update existing set
    def updateset():
        
        print("New set:", new_set)
        Set.update(new_set) 
        print("Updated Set:", Set) 

    #remove by element using remove.remove() gives error if element not in set
    def remove():
        d = int(input("Enter element to delete "))
        if d in Set:
            Set.remove(d)
            print("After remove ",Set)
        else:
            print("Not found")
            
    #remove by element using discard,it dont give error if element not found
    def discarde():
        d = int(input("Enter element to delete "))
        Set.discard(d)
        print("After Discard ",Set)
        
    #popelement to remove and return arbitary element
    def popelement():
        poppedData = Set.pop()
        print("Popped Element is = ",poppedData)
        print(Set)

    
    def union():
         print("set first ",Set)
         print("New set:", new_set)
         ans = Set.union(new_set) 
         print( "After Union ",ans)

    def intersection():
        print("Set first ",Set)
        print("Set second " ,new_set)
        ans = Set.intersection(new_set)
        print("After Intersection ",ans)

    def Diffrence():
        print("Set first ",Set)
        print("Set second " ,new_set)
        ans = Set.difference(new_set)
        print("After difference ",ans)        


    def SymetricDiffrence():
        print("Set first ",Set)
        print("Set second " ,new_set)
        ans = Set.symmetric_difference(new_set)
        print("After Symmetric difference ",ans)

    def issubset():
        print("Set first ",Set)
        print("Set second " ,new_set)
        ans = Set.issubset(new_set)
        print("answer of issubset ",ans)
    
    def issuperset():
        print("Set first ",Set)
        print("Set second " ,new_set)
        ans = new_set.issubset(Set)
        print("answer of superset ",ans)

    def copyset():
        set_copy = Set.copy()
        print("Copy of Set is = " ,set_copy)

    def clear():
        print("Set is ", Set)
        Set.clear()
        print("Set after clear() ", Set)
    while True:
        print("")
        print("1:create new set with one element ")
        print("2:Update element in existing set ")
        print("3:Remove element using remove")
        print("4:Remove using Discard")
        print("5:Pop Element")
        print("6:Union")
        print("7:Intersection")
        print("8:Difference")
        print("9:symmetric Difference")
        print("10:is subset")
        print("11:is superset")
        print("12:copy set")
        print("13:clear")
        print("14:EXIT")
        print("")
        choice = int(input("Enter your choice "))

        if choice == 1:
            newset()
        elif choice == 2:
            updateset()
        elif choice ==3:
            remove()
        elif choice == 4:
            discarde()
        elif choice == 5:
            popelement()
        elif choice == 6:
            union()
        elif choice == 7:
            intersection()
        elif choice == 7:
            Diffrence()
        elif choice == 8:
            SymetricDiffrence()
        
        elif choice == 9:
            SymetricDiffrence()
        elif choice == 10:
            issubset()
        elif choice == 11:
            issuperset()
        elif choice == 12:
            copyset()
        elif choice == 13:
            clear()
        elif choice == 14:
            break
        else:
            print("ENTER VALID CHOICE")

#Implementing all dictionary operations
def DictData():
    dict = {}
    def create():
        
        n = int(input("Enter the number of key-value pairs: "))
        for _ in range(n):
            key = input("Enter key: ")
            value = input("Enter value: ")
            dict[key] = value
        print("Dictionary created with user inputs:")
        print(dict) 
    
    def copy():
        print("Original dict ",dict)
        dict_copy = dict.copy()
        print("copy of Dic ", dict_copy)
    
    def usefromkeys():
        keys = ["Name","age","email","mobile"]
        default_value = 0
        new_dict = dict.fromkeys(keys,default_value)
        print("Output of fromkeys ",new_dict)
    
    def useget():
        ans= dict.get('Name','Not Found')
        print("Output of get() " ,ans)
    
    def useitems():
        print("Output of itms ")
        for key,value in dict.items():
            print(key,value)
    
    def usekeys():
        keys = dict.keys()
        print("output of Keys()")
        for k in keys:
            print(k)
        
    def usepop():
        print(dict)
        k = input("Enter key to pop ")
        result = dict.pop(k)
        print("Dict after pop ",dict)
        print("Poped value ",result)
    
    def usepopitem():
        print(dict)
        
        result = dict.popitem()
        print("Dict after popitem ",dict)
        print("Poped value ",result)
    
    def usesetdefault():
        print(dict)
        
        d = dict.setdefault('address','satara')
        d = dict.setdefault('Name','Pratiksha')
        print("Dict after setdefault ",dict)
    
    def updateDict():
        dict2 = {'class':'mca','college':"xyz"}
        print("First dictionary ",dict)
        print("second dictionary ",dict2)
        dict.update(dict2)
        print("Dict after update ",dict)

    def usevalues():
        print(dict)
        values = dict.values()
        print("Values of dict = ")
        for v in values:
            print(v)

    while True:
        print("")
        print("1:Create dictionary ")
        print("2:Make copy() if existing dictionary")
        print("3:using fromkeys")
        print("4:get()")
        print("5:Items()")
        print("6:Keys()")
        print("7:Pop()")
        print("8:popitem()")
        print("9:setdefault()")
        print("10:Update")
        print("11:Get values()")
        print("12:EXIT")
        print("")
        choice = int(input("Enter your choice "))

        if choice == 1:
            create()
        elif choice == 2:
            copy()
        elif choice ==3:
            usefromkeys()
        elif choice == 4:
            useget()
        elif choice == 5:
            useitems()
        elif choice == 6:
            usekeys()
        elif choice == 7:
            usepop()
        elif choice == 8:
            usepopitem()
        elif choice == 9:
            usesetdefault()
        elif choice == 10:
            updateDict()
        elif choice == 11:
            usevalues()
        elif choice == 12:
            break
        else:
            print("Enter valid Choice")
     




while True:
    print("")
    print("Press 1 to work with List")
    print("Press 2 to work with Tuple")
    print("Press 3 to work with Set")
    print("Press 4 to work with dictionary")
    print("Press 5 to Exit")
    print("")
    DataType = int(input())
    if DataType == 1:
        ListData()
    elif DataType == 2:
        TupleData()
    elif DataType == 3:
        setData()
    elif DataType == 4:
        DictData()
    elif DataType == 5:
        break

 
