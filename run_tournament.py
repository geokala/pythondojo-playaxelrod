#! /usr/bin/env python
import axelrod
import teams

strategies = [s() for s in teams.players]

print('Competitors are:')
for s in strategies:
    print(s)

tournament = axelrod.Tournament(strategies)

print('')
print('')
print('... playing ...')
results = tournament.play()
print('')
print('')

print('Results:')
for result in results.ranked_names:
    print(result)
