from axelrod import Player
import random

class TeamDarkRed(Player):
    name = 'Player 1 Team Dark (Red)'

    classifier = {
        'memory_depth': 2,  # Long memory, memory-2
        'stochastic': False,
        'inspects_source': False,
        'manipulates_source': False,
        'manipulates_state': False,
    }

    def strategy(self, opponent):
        total_played = opponent.defections + opponent.cooperations 
        if total_played > 0:
            weight = opponent.cooperations / total_played
        else:
            weight = 0.0 

        r = random.random()
        if r < weight:
            return 'C'
        return 'D' 
        

