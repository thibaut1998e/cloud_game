Cloud game :
This is a little game coded in python in which you control a small cloud. You win when you reach the arrival with all the coins caught.
There are some existing levels in the folder levels, but you you can also edit your own levels with the edition mode, 
they will be saved in a text file.

1) Launch the code:
To launch a level type in a terminal (assuming you are in the right folder)

python cloud_game.py --location path_of_level

If the corresponding path exists it will open the level and you will be able to play. 
Otherwise it will open the edition mode with an empty level. When you have finished editing you can close the window 
and your level will be saved at the specified location. Please refer to the playing and edition mode instructions to know how to
edit a level and to control the character.
If you want to edit an existing level :

python cloud_game.py --location path_of_level --edition



Overrview of the code 

2) how to code a new Object

There is a general class for all the object of the game : Game_object, any object of the game must extends this class. 
An object of this class is a rectangle, its main attributes are :
- height and width
- pos : its postion (the top left corner)
- initial_pos : some object move during the game, when a new game starts their postion are reset to this value
- image : the image of the object, in the constructor you provide the image path and a transparency color. If you provide -1 as 
transparency color, it is set to the color of the top left corner
- game : an object of the class Game. It contains all the information about the game. In particular an attribute of the class game is 
the list objects it contains. Then our object is able to fully interact with all other objects.

To add a new object, it must extends this class. You also need to override some methods :
- display : this method is called at each iteration of the game loop before updating the screen, it displays the object on the screen.
You might not need to overide it since it covers most of the cases in the parent class (with and without image).
- interact, this method is called each time in the game loop before updating the screen. You can do anything in it to make your object interact with 
the game, such as moving or ending the game by setting the attribute 'continuer' of game to False. It returns a message which is displayed
at the screen if the game ends. 
- reset : called each time a new game start, you might want to reset some attributes
- process_event : it processes the event of the keyboard, you might want to modify the value of some attributes according to what
has been pressed on the keyboard. You might not need to override it since its mainly the charcater which need to interact with the keyboard.
- process_event_edition_mode : it processes the event in the edition mode. Here again you might not need to override, since most of the
events are processed in the parent class. (such as changing the size, selcting, add buttons etc)
- create_buttons : Buttons only exist in the edition mode. They are used to change the values of some attributes (such
as the speed of the character or  period of the walls). This method is called when the key b is pressed on a selected object in the edition
mode.  Buttons associated with this object are created here, you can set in the constructor the value max, min and step of your buttons. If you do not override, no button will appear when pressing b
- save_buttons_values : this method is called when the buttons are removed from the game. You can save here the values recorded by the 
buttons in some attributes of your object.
- attributes_to_save : return the list of attributes to save in the text file when the window is closed. In the parent class this list is
initial_pos, height and width. This attributes must be string, float, list or tuple.

Note : For all of these methods, do not forget to also call the method of the parent class with super unless its not needed

Note 2 : There is a class Monster which extends Game_object. This class has a method which ends the game when the character collides with it. 
If you want to create an objets which kill the character, it must extends this class so that you do not need to rewrite this method. For
example wall and DangerousMonster extend this class

3) Add your object in the edition mode :
- Once you've finished coding your class, there is an easy way to add a controle/key in the edition mode which will pop an object from this class
on the screen. The class which represents the edition mode is 'LevelDesigner' (which extends Game). One of its attributes is a dictionnary 'controles', 
simply add your class to the dictionnary. The key is the controle and the value the Class.
- You also need to add the class to the dictionnary 'dict_class_name' at the end of the file. This is used in the method 'create_game_with_file' (in main.py)
in order to get the Class from its string name


