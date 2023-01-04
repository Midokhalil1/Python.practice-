# while loops
# n = 0
# while n < 5:
#     print(n)
#     n += 1

# if statment

#A = 20
#B = 20
#C = 11

# if A == C :
#     print('Yes')
# else :
#     print('No')

#logic operator

#if A > 10 or C > 10 :
   # print("Yes")
#else : 
    #print("No")


 #identity operator 
 
#if A is B :
    #print("Yes")
#else : 
    #print("No")



#membership operator 

Names = ["Mido","Ryan","Emily"]
if "Mido" in Names:
    print("Mido Found!")
else: 
    print("Not Found!")

#test

X = 50
Array =[30,64,77,81]

if 77 in Array :
    print ("Yes")

if X > 77 :
    print("Yes")

else :
    print("No")


#LOOPS

list_names= ["Mido", "Ryan", "Khalil", "Emily", "Amira", "Athar"]
for x in list_names:
    print(x)
    
# Loops using Range
for i in range(10):
    print ("Hello World")

#While loops   

Magic_number = 0
while Magic_number < 10 :
    print("Its Magic!")
    Magic_number = Magic_number + 1

# list of numbers
list1 = [10, 24, 4, 45, 66, 93]
num = 0
 
for num in list1:
    if num % 2 == 0:
        print(num, end=" ")


#User-defined Functions 

def My_func ():
    print("Hello World!") 
My_func()    

# Parameters 

def Hello (name):
    print("Hello " + name )

Hello("mido ")
 
 #Return
def Add (x,y) :
    return x + y 
print(Add(4,7))


#functions 
#takes 2 num and return the sum if them and the diffrence 



def My_func(a,b):
    print(max(a,b))
    print(max(a,b)-min(a,b))

My_func(5,8)


#list1 = [10, 24, 4, 45, 66, 93]
#for i in range(10000):
    #print(list1)

# 2 sum 

def twoSum(nums, target):
    complements = {}
    for i in range(len(nums)):
        if nums[i] in complements:
            return [i,complements[nums[i]]]
        else:
            complements[target - nums[i]] = i
print(twoSum([2,11,15,3],14))

#2num

class Solution(object):
    def twoSum(self, nums, target):

        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[target - nums[i]] = i 
            else:
                return hashmap[nums[i]], i 
            
            
 #fizzBuzz 
 
for n in range(1, 101):
    if n % 15 == 0:
         print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
         print('Buzz')
    else:
        print(n)           
         
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
#list = [2, 7, 15, 16]      Target = 9 

#return an array with the index of the two numbers who's sum equals the target

def twoSum(nums, target):
    hashmap = {}       #store the value # intionlizing the hashmap so i can use it later 
    for i in range(len(nums)):    #creating a seqnce of numbers from 0 up to the length of list
        if nums[i] not in hashmap: # if value (nums) not in the hashmap 
            hashmap[target-nums[i]] = i    #making an entry to the hashmap so the value be 7 
        else: 
            return [
                hashmap[ nums[i] ],     # gets the index from the hashmap
                i                       # index of current number
            ]
        
# hashmap = {   7 : 0   }  9 (target) - 2  (value on first loop) = 7, this was at index 0
# hashmap = {   2: 1    }  9 (target) - 7 (value on second loop) = 2, this is at index 1
            
            
        

      
      
    


          

