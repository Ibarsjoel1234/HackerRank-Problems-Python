QUESTION:
 ---------
          Given a number n, for each integer i in the range from 1 to n inclusive, print one value per lines as follows:
              1. If i is a mulitple of both 3 and 5, print "FizzBuzz".
              2. If i is a mulitple of 3(but not 5), print "Fizz".
              3. If i is a multiple of 5(but not 3), print "Buzz".
              4. If i is a multiple of 3 or 5, print the value  of i.
              
FUNCTION DESCRIPTION:
---------------------
  Complete the function fizzbuzz in the editor below.
  fizzbuzz has the following parameter(s):
    int n: upper limit of values to test(inclusive)
    Returns: NONE
    Prints:
      The function must print the appropriate response for each value i in the set {1,2,..n} in ascending order, each on a swparate line.

CONSTRAINTS:
------------
  
  1. 0 < n < 2 * 10^5.
--------------------------------------------------  

PROGRAM:
--------

def fizzBuzz(n):
 for i in range(1,n+1):
  if i % 3 == 0 and i % 5 == 0:
    print( "FizzBuzz")
  elif i % 3 == 0:
    print( "Fizz")
  elif i % 5 == 0:
    print( "Buzz")
  else:
    print(i)
    
    
    
if __name__ == '__main__':
  
  n  = int(input().strip())
  fizzBuzz(n)
  print(n)
  
------------------------------------------- 
