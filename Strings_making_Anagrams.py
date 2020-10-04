from collections import Counter

def anagram(a,b):
  d1 = Counter(a)
  print("\n")
  print("Details of a: ")
  print(d1.keys())
  print(d1.values())
  print("\n")
  d2 = Counter(b)
  print("Details of b: ")
  print(d2.keys())
  print(d2.values())
  print("\n")
  print("Details of Total1: ")
  total1 = (d1-d2)
  print(total1)
  print(total1.keys())
  print(total1.values())
  print("\n")
  print("Details of Total2: ")
  total2 = d2-d1
  print(total2)
  print(total2.keys())
  print(total2.values())
  print("\n")
  tot = total1 + total2
  print(tot)
  print("Details of tot: ")
  print(tot.keys())
  print(tot.values())
  print("\n")
  val = sum(tot.values())
  print("Final result: ")
  return val


a = input("Enter the values for a : ")
b = input("Enter the values for b : ")
c = anagram(a,b)
print(c)
