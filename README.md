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
