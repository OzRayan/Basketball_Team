# Project 2 - Python Web Development Techdegree

## Project Instructions

### Create a new script
- [x] The very first step you will want to do after opening the workspace or unzipping the .zip file into your project folder is to create a new and blank Python script named app.py or application.py.

### Proper use of Dunder Main
- [x] Make sure the script doesn't execute when imported; Anything that is a calculation, callable function, or a block of logic that needs to run, ensure you put all of your logic and function calls inside of a dunder main block at the bottom of your file:

Dunder main statement looks like this:

`if __name__ == "__main__":`

*HINT*: Unit 1 project files/workspace had an example of this.

*NOTE*: This does not mean everything you write has to be contained within Dunder Main. You can still import and define functions outside of dunder main, you can still extract pieces of logic into those functions. The main calls to your program should be protected inside Dunder Main to prevent automatic execution if your script is imported.

### Import player data
- [x] Import from constants.py the players' data to be used within your program.

*NOTE*: Python has no concept of actual constants like other languages have. But it is a convention you may see in the real world. When you see ALL CAPS variable name you are meant to treat it as if it were a constant or a value that you cannot change/alter.

### Clean the data
- [x] Write the logic to read the existing player and team data from the PLAYERS and TEAMS constants provided in constants.py. Build a new collection with what you have learned up to this point.

*HINT*: Think Lists with nested Dictionaries might be one way.

*NOTE*: Ensure you do not directly modify the data in PLAYERS or TEAMS constants. This data you should iterate and read from to build your own collection and would be ideal to clean the data as you loop over it building your new collection.

### Balance on total players
- [x] Balance the players across the three teams: Panthers, Bandits and Warriors. Make sure the teams have the same number of total players on them when your team balancing process has finished.

### Console readability matters
- [x] When the menu or stats display to the console, it should display in a nice readable format. Use extra spaces or line breaks to break up lines if needed.

### Displaying the stats
- [x] When displaying the selected teams' stats to the screen you will want to include:
    - [x] Team's name
    - [x] Total players on that team
    - [x] The player names separated by commas.
*NOTE*: When displaying the player names it should not just display the List representation object. It should display them as if they are one large comma separated string so the user cannot see any hints at what data type players are held inside.

### An Example Run
Here is an example of what the running application might look like in the console (the design of the menus and how things are displayed are totally up to you, though it should be readable and display the proper stats)

```bash
BASKETBALL TEAM STATS TOOL

---- MENU----

 Here are your choices:
  1) Display Team Stats
  2) Quit

Enter an option > 1

1) Panthers
2) Bandits
3) Warriors

Enter an option > 1

Team: Panthers Stats
--------------------
Total players: 6

Players on Team:
  Karl Saygan, Chloe Alaska, Phillip Helm, Suzane Greenberg, Herschel Krustofski, Joe Smith

Press ENTER to continue...
```

## Exceeds
-      
### Cleaning guardian field
- [x] When cleaning the guardian field before adding it into your newly created collection, split up the guardian string into a List.

*NOTE*: There can be more than one guardian, indicated by the " and " between their names.

### Additional balancing to the team
- [x] Additionally, balance the teams so that each team has the same number of experienced vs. inexperienced players.

If this is done correctly each team stats should display the same number count for experienced total and inexperienced total as well as the same total number of players on the team.

### Include additional stats for a given displayed team:
- [x] number of inexperienced players on that team
- [x] number of experienced players on that team
- [x] the average height of the team
- [x] the guardians of all the players on that team (as a comma-separated string)
*HINT*: You can calculate the average height for a given team by keeping a running sum total of each players height on the team and dividing that total by the total number of players on that team.
