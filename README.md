# Buckshot Roulette
Terminal Buckshot Roulette recreation for fun using Python.  
Original: https://store.steampowered.com/app/2835570/Buckshot_Roulette/  

# Rules:  
- The player and the dealer gets a random number of lives from 2 to 5.
- Each round, the shotgun is loaded with a random amount of shells from 2 to 8. The number of live and blank shells in that amount is also randomized, and will be inserted into the shotgun in a random order.
- The player and the dealer takes turn pulling the trigger, either at themselves or their opponent. The player's choice is controlled by user input, while the dealer's choice is randomized (Future developments may include AI calculated dealer's choice, although taking into account my experience with the base game, this feature may have already been developped by the original creator. Again, this is a just-for-fun project.)
- The person getting shot by a live round will lose a life, and the next turn goes to the person not holding the shotgun in the previous turn.
- If someone shoots themselves with a blank round, they are granted another turn. If someone shoots their opponent with a blank round, the next turn goes to their opponent.
- When the shells in the shotgun run out, they will be randomized and re-inserted again as mentioned above.
- The game ends when the player or the dealer runs out of lives. The person who runs out of lives first loses.

# Dev Log:  
5/5/2024: Barebones algorithm for a game of Buckshot Roulette.
