# itp

## Scratch Project by Ruben

I added two random sprites, which gave me a soccer ball and a dinosaur. This was all the inspiration I needed to make a game where you're a dinosaur playing soccer.

The main elements of the game are scripts that test for pushing the arrow keys, which move the dinosaur as well as changing the sprites so he is facing the right direction.

I couldn't think of a good way to add physics to the game, so I just have the ball moving in a random direction every time it is "kicked."

The **kick** function works by checking if the soccer ball is touching the dinosaur, and if it is, it moves to a random location on the screen. I then have a test for if the x position is above 200 or below -200 (near the two goalposts on the background). If it is, a cheering sound effect plays, the score goes up, and the ball is returned to the center of the screen.

I created the score with a custom variable that increases whenever the ball goes to the edge of the screen, and changes the text on the actual sprite to show the score.

I made a simple victory screen that shows when you get to 10 points, and all of the sprites are hidden so they don't show up on the end screen.

Overall it was a pretty fun project and I definitely enjoy pseudo-coding :)
