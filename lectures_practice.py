# lectur workspace for 6.00 6.100L | Fall 2022 | Undergraduate
# Introduction To CS And Programming Using Python

# lecture 11
# l = [1,2,3,4]
# lcopy = l[:]
#  now we have two lists that are the same but are different objects
# print(lcopy)
l = [1,4,4]
e = 2
def remove_all(l,e):
    l1 = l[:]
    l.clear()
    for i in l1:
        if e != i:
            print(i)
            l.append(i)

# remove_all(l,e)
# print(l)

def remove_all(l,e):
    while e in l:
            l.remove(e) # removes the first instance of the element and has no return value
 
# remove_all(l,4)
# print(l)
# del l[0] # removes the first element and has no return value


# just removed the last element and also returned it 

def duplicate_list(l1,l2):

    for i in l1:
        l2.remove(i)
    return l2   

# l1 = [1,2,3,4]
# l2 = [1]
# l2 = duplicate_list(l1,l2)
# print(l2)








# alias


#  list that contain list itself
import copy
old = [[1,2,3],[4,5,6],[7,'hello','jaan']]

new_copy = copy.copy(old)

old.append(7)
old[1][1] = 'hello'

# print(new_copy)

# print(old)

# shallow



# deep 



# list comprehension

def f():
    listt = []
    for i in range(10):
        listt.append(i**2)

    return listt
#  here we are creating a list of list which output is a list of list
lnew = [[e,e**2] for e in range(10) if e%2 == 0]
print(lnew )

lnew1= [len(l) for x in ['xy','abcd',7,'4.0'] if type(x) == str]
print(lnew1)
print(type(lnew1))


# default parameters
# include the bisection function for guessing the number

# what is the best epsilon to use for bisection search
#  we can have a default value for the epsilon
def make(a):
    def g(b):
        return a+b
    return g

# val= make(3)(2)
dobler = make(2)
val = dobler(3)
print(val)



