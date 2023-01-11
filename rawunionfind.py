#This a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each).
#Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops.

class UF:
  def __init__(self, n):
    print("Initializing a list of", n, "objects.")
    self.list_of_comps = []

  def union(self, p, q):
    self.component1 = self.find(p)
    self.component2 = self.find(q)
    print('I checked')
    if self.component1 != False and self.component2 != False:
      self.component1 += self.component2
      self.list_of_comps.remove(self.component2)
    elif self.component1 == False and self.component2 != False:
      self.component2 = [p] + self.component2
    elif self.component2 == False and self.component1 != False:
      # print('Here')
      # print(self.component1)
      # print([q])
      self.component1 += [q]
    else:
      # print('I ran')
      newcomp = [p, q]
      self.list_of_comps.append(newcomp)

    # return component1  #Do we really need to return this ?

  def find(self, c):
    for i in self.list_of_comps:
      if c in i:
        return i
    return False

  def connected(self, p, q):
    for i in self.list_of_comps:
      if p in i and q in i:
        print('path exists at', i)
        return True
    # self.union(p,q)
    print('No such path exists as of now.')
    # return False

  def count():
    return len(self.list_of_comps)


n = 10
connection = UF(n)
connection.union(1, 2)
connection.union(2, 3)
connection.union(5, 6)
connection.union(5, 1)
connection.union(7, 4)
connection.connected(3, 4)
connection.union(0, 9)
connection.union(20, 10)
connection.union(16, 18)
connection.union(16, 20)
connection.connected(18, 20)
print(connection.list_of_comps)

print('How many objects do you wish to process?')
num = int(input())
for i in range(num):
  print('Enter the desired connections.')
  p = int(input())
  q = int(input())
  connection.connected(p, q)
  print(connection.list_of_comps)

print('See you next time')

