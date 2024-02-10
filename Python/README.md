# itp

## Python Reading

### Chapter 1:
#### New Info:
I didn't realize that Python can run through command line prompts. In my experience with Python we ran it through an app called Anaconda
#### Old News:
I knew the syntax for exponents, as well as the difference between integers and floating point numbers. I also have some understanding of bitwise operations, at least with shifting binary digits left and right

### Chapter 3:
#### New Info:
I am starting to pick up on some clues on how to use Python in the online interpreter, which I imagine is similar to running it in a command terminal. The difference between "interactive mode" and "script" in particular seems important. I spent a few minutes trying to remember how to define a recursive function, but got stuck on incrementing a count to terminate the function.
#### Old News:
I remember the process of defining functions, and using functions within function. The concept of "Flow of Excecution" makes a lot of sense. I also successfully wrote a "right justify" program, which was in the exercises:

def right_justify(r):
...     if len(r) < 70:
...             print (' ' * (70-len(r)) + r)
...     else:
...             print('Error: Too Long')

### Chapter 5:
#### New Info:
Ah, this chapter solved my problem (sort of) on how to set up a recursive function. I was trying to create a function with no input that would recur 5 times, but I couldn't figure out how to set an initial value for the counter while incrementing it. By expecting a value, you can call the function with the value+1 to have it increment recursively. I still wanted my final function to not require input, so I set up the recursive function, and then another function to call it with an initial value of 0.

Also, the modulus and floor division functions are interesting, and not something I've used before.
#### Old News:
I am familiar with recursive functions, and I have written the Fibonacci Sequence as a recursive function in Python before.
