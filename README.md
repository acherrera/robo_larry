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


Video from this day: https://youtu.be/N1dOGgtShr4

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

Tuning and tuning and more tuning to try and get that dang left lane to be found. Maybe be better / eaiser to just
rewrite the land finding from scratch as I barely understand how it is currently working.


## Day 9 - 4 hours

Refactored code and found a duplicate chunk of code that was likely causing some FPS issues. Next up is updated the lane
finder so that it actually works. Line finding appears to be adequate. 

After some more tuning lane finding is working better and driving in grass doesn't cause the frame rate to drop as much
due to less line being detected. The key is just more blurring I guess. 

Looked over the control code and updated.

First attempts at letting the computer drive itself. Not bad.... Not great either. Sometimes corrected too much,
sometimes not enough. Still having framerate issues, need to try and reduce the image size before processing - that
should help considerably


## Day 10 - 1.2 hour


Reduced image size by 50% before processing resulting in much higher frames per second. Afterwards, fiddled with the
edge detection and blur parameters and ended up with a very good result. Tuned the parameters on the controls and
finally settles on one "turn" every 1.5 seconds (basically). Turn decay is not based on time, not frame rate which
appears to have stabilized the turning significant.

Took a chance and just added logic to accelerate when the lines are not the same slope (IE when the vehicle is in the
middle of the lane and it works swimmingly

Results after this day: https://youtu.be/98NeVOI6AkU

## Day 12 - 1.5 hours

Mainly just messed around and showed off what the program could do. Afterwards went hunting for a way to save the
keypress input. Found a way to do it, but the program seems very limited. Basically it can get key presses but it runs
in a class so I need to hack that class to make it work with the image processing

## Day 13 - 3 hours

Attempting to use socket communication to send the required data to a local server that will process and save the data
as needed. The socket communication is easy enough, but once again there is a time issue. The key logger runs based on
events, whiche mean syncing it with the images will be a challenge even if the socket communication worked perfectly. 

Okay, think I figured out to sync it all together. This should be interesting. First time using sockets programming and
I kind of like it. I can see how it would be super useful for multiprocessing images. Hmm.... this might help immensely
with the framerate. Get around the GIL (Global Interpreter Lock) by run running multiple programs. 

Socket communication suffered from the same class based issues. Ended up just writing the keys to a file and will read
them in later with some logic for turning that into an array. It's not pretty but it should work well enough

## Day 14 - 5 hours

Breakthrough finally. Got the key logging working and translating this into a control array. Took WAY, WAY longer than I
would have liked it to. But it appears to be working now. Sentdex didn't put the code to view the data in the tutuorial,
but it was in the video and is extremely useful.

Got some training data and am ready to move on to actually training the model.

## Day 15 - 2 hours

Fighting with CUDA installation. Looking towards next steps

## Day 16 - 2 hours

CUDA installed almost immediately from deb. So that's nice. Tensorflow and TFlearn install went pretty smooth as well.
Trained first model and attempted to run. Did not go well. Tried to open ATS and discovered CUDA installed from deb
makes steam and other games not work. So bad to installing from the .run file. This time with (maybe) better
instructions!

https://github.com/ValveSoftware/steam-for-linux/issues/5778

Hey, finally got CUDA installed. For real this time. At least, ATS works now. Ran the initial model and it was complete
and total trash. Will got more training data and train it with that. I had gotten 100k images previously but this was
narrowed down to about 1600*4 once I had balanced the data a little more. Next time I'm going to shoow for 100k images
to train with. That is, images after balancing

## Day 17 - 4 hours

Okay, I put a few more days into the project than this but I forgot to record it. Trained up model number two and it was
also garbage. Looking at the number it seemed like the inputs were far too few for how much time I was putting into it.
Turns out, my input capture was only capture between 1/2 and 1/30 of the data I was actually making. So... back to the
drawing board for the input capture. Most likely going to use a bash script as the root level so I can get raw input.

Wow, somehow managed to get the contro inputs working in one day. Used a slightly different method and it requires sudo
permissions, but it appears to work MUCH better. After one sessions the number of value looks like this: Previously I
have nearly 129k empty valies with about 16k forward values which is... wrong. Very wrong. I also broke these up into
combined commands instead of only 'forward', 'left', 'right', 'backwards'. Now we can got forward AND right. Wow, such
advanced driving

    Forwards: 28057
    Front Left: 2575
    Front Right: 1873
    Left: 2246
    Right: 1334
    Backwards: 1410
    Back Left: 189
    back_right: 187
    Empty: 9129

## Day 18 and nearly a year later

Converted it all to windows
