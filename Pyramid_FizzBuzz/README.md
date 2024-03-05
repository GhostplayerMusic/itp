# Pyramid/FizzBuzz

This week's homework was the first actual programming we've done in Intro to Programming. It went very smoothly! I have some experience in Python, as my senior year of high school I took an online Python class as an independent study for math credit.

When creating the pyramid, the challenge was in adapting the "square" code to form a pyramid. I figured out that instead of nesting loops, I could just have the for loop print out i times "#" each time through the loop. However, my pyramid printed out facing the wrong way.

It looked like this:

    #
    ##
    ###
    ####
    #####
    ######
    #######

But I wanted it to look like this:

         #
        ##
       ###
      ####
     #####
    ######
   #######

  So I appended (a - i) times ' ' to the print command, where a is the input. This added a decreasing number of spaces before each line, causing the pyramid to face the right direction. Hooray!


For the FizzBuzz file, I created a for loop with a control flow that looked like this:

for i in (1,101):
  if:
  elif:
  elif:
  else:

The first if command checked to see if i was divisible by both 3 and 5. If so, it prints "FizzBuzz".

The first elif command then checks if i is divisible by 3, and NOT by 5. The key was to use the and logic operand, because it would ovverride the FizzBuzz part if I just checked if it was divisible by 3.
If i is only divisible by 3, it prints "Fizz".

The next elif command checks if i is divisible by 5 and NOT by 3.
If i is only divisible by 5, it prints "Buzz".

Finally, the else statement simply prints i, to get us the remaining integers without alteration. 
