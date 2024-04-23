# Chessboard

This assignment wound up being quite difficult, but I was eventually able to get the chessboard to print properly.

My main problem was my lack of understanding on how the Javascript Console functions, as it doesn't handle printing the same way as Python.

I set up a for loop to accept a submitted value (converted to integer using the Number function) and output '#' repeated based on the value

The main problem was that any time the same string is printed twice in a row, the console will "stack" them together and put a number next to how many "stacks" there are of the same result.

This means that I had to find a way to never print the same string twice in a row.

I used an if/else statement to alternate where the spaces went between the characters, depending on if the current iteration through the for loop was even or odd. This resulted in a "chessboard" that printed properly, and in fact looks more like the chessboard in the example.

I added some polish with a notification that tells you to open the javascript console so you can actually see what it's doing, as well as a paragraph to give some context to the random input. 
