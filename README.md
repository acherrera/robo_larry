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

## Day 3 - 2 Hours

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
