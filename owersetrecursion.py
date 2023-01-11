#This a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each).
#Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops.

powerset = []
count = []

def recursive_powerset(set,upper):
  count.append(1)
  if upper >= 0:

    recursive_powerset(set,upper-1)
    #print(powerset)
    #copyset = powerset.copy()
    empty = []
    for i in powerset :
      tempi = i.copy()
      tempi.append(set[upper])
      empty.append(tempi)
    for i in empty :
      powerset.append(i)

  if upper == -1:
    powerset.append([])

def powersetrecursion(cset) :
  if len(cset) == 0 :
    return [[]]

  smaller = powersetrecursion(cset[:-1])
  extra = cset[-1:]       #Deliberately stored it as a list so this can be concatenated further with the returned list of items conveniently.
  new = []
  for i in smaller :
    new.append(i+extra)   #Concatenating lists instead of appending a singular value in the existing list

  return smaller + new    #A cool way of concatenating lists

set = [1,2,3,4]
n = len(set)
#recursive_powerset(set,n-1)
#print(powerset)
#print(len(powerset))
#print("Number of recursions:", len(count))

#print(powersetrecursion(set))
a = [[1],[2]]
b = [[3],[4]]
new = []
c = ['i']
for i in a:
  new.append(i + c)
print(new)
print(a)
print(a+b)