from axelrod import Player
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
        print('Opp: %s' % opponent.history)
        print('Me: %s' % self.history)
        return 'D' or 'C'
