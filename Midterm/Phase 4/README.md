# Phase 4

After much trial and error, I got it to work! The hardest part was figuring out how to set up a for loop in processing. It took about 20 minutes to realize that I was missing the word "range" so nothing was working.

After that hurdle, I was able to quickly put together the nested for loops to call drawObject with the correct x and y position based on an input grid division. However, I had a really hard time getting the scaling to be correct. I finally figured out that to get the scaling, I had to divide the size of each tile by the size of the shape. The tile size is represented by the variable t, and the scale factor s is computed by dividing the size of each tile by the size of the shape, which came out to be 159 pixels.

Overall, I was very happy to get it working, and feel like things went well. 
