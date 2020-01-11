# Robo Larry

Do you love programming and semi trucks but hate the monotony of having to spend hours checking the speed limit and
driving safe? Well fear no more, I'm attempting to do away with all that boring tedious work by spending many hours
automating it! No problem.... right? 



# Dev Diary

## Day 1 - 2 hours

This assumes Python is already set up and ready to run along with your development environment. I won't be going over
all the here as there are many, many tutorials on line for that. I am using Neovim and the Ubuntu shell to run python
programs. Pretty simple.

What I acheieved

- Install game
- Hack game to get unlimited credits to buy truck and wonder around free

### Notes

#### Get out of the game window

Open the steam tab thing by using `shift + teb`

Game location is: `~/.local/share/Steam/steamapps/common/American Truck Simulator/`... but this isn't where the config
information is located. That would be `/home/tony/.local/share/Steam/userdata/130211624/270880/remote/profiles`. Yeah,
that was a lot of fun to try and find. To go into developer mode and activate console commands:

    g_developer "1"
    g_console "1"


## Day 2 - 1.5 hours

Mainly just getting enough in-game money to actually do a free drive event

Can reset by presssing F7 and be transported to nearest repair station

FOUND THE CONSOLE COMMANDS!!! `~/.local/share'American Truck Simulator'`

Finally got a truck to work with

## Day 3 - 3 Hours

Finally got the delievery done. $250k later and we're good to start programming just need to fix my rig....

Oh my. Do not press F9 while it in the air. It will drop your truck from very high up causing a godo amount of damage.
Just need to figure how to teleport properly now. 

Free cam! Move to ground and teleport truck. Except I need a numpad to do that. Cool, luckily I have a wireless keyboard
laying around that my wife hasn't thrown out yet. Pair that and.. it worked! Which also means I should be able to make
huge deliveries in secs. Woo hoo! 

Let's figure out this whole video thing here soon. 

And... actually starting in programming. First step, getting the video from the game. Initial attempts were not good.
ImageGrab is apparently only for Windows and Mac and doesn't work on Linux. Which is odd because it works on Mac. Oh
well, time to find an alternative

Yes! Exactly what I was looking for - https://python-mss.readthedocs.io/examples.html#opencv-numpy This guy must be
watching the same tutorial I am. That page references the tutorial that I'm working with. Appears to work well enough
and looks like it is returning frame rates of 150-200 FPS. Which seems suspect, but I'll check that out later

Got the controls working for the game. Pyautogui was good enough for me, so I'm going to stick with it. 

Changing the ROI to be the just the area of interest. Duh. Installed mod to move the position of the GPS so program can
see the whole lanes


## Day 4 - 3 hours

Okay, this morning I was just editing video. Got most of the first video done. Would like to start work on line
detection this afternoon if possible.

Spent a good amount of time diagnosing a new gaming headset that should hopefully increase the audio quality. Turns out
I didn't plug it in correctly.... ugh. Did second video on controls and uploaded first video

## Day 5 - 1.5 hour

Trying to get the frames to process reasonably fast. Trying to fix lines result is 1 frames a second instead of 100+
FPS. Which is really bad.

Updated the FPS to about 60 by copying and pasting the code from sentdex's tutorial. No idea why / how it fixed it. I'm
guessing I was doing some double processing or something. Oh well. Need to tune the parameter to get it to correctly
recogonize the lines. Currently not recogonizing them, but it is working on the menu screens so it is at least trying. 

## Day 6 - 0.25 hours

Getting the contrast to work much better. Was barely picking up on the lines before so I went in an looked at the raw
grayscale image. 


Before 
![Image before equalizeHist applied][before_hist]

After
![Image after equalizeHist applied][after_hist]

As you can see this made a HUGE difference in the raw Grayscale image. After this change it went from detecting maybe
one line to detecting many lines as I would expect it to. Very short day, but rather productive


[before_hist]: ./docfiles/equalizeHistEffect/before_equalizeHist.png
[after_hist]: ./docfiles/equalizeHistEffect/after_equalizeHist.png

## Day 7 - 0.5 hours

Attempted to add the lane finding function into the program. Did not get very with it - unable to find any lines. Will
want to look over program and update later

## Day 8 - 1.5 hours

Debugging lane finding. The many try and except loops were hiding errors since they would just print it out and pass it.
Stepped through and fixed these. Also, the "lane" that it was finding was basically a horizontal line so it attempted to
graph a horizontal starting at min and max y resulting in rediculous x values
