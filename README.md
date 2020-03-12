# Pacman-MultiAgentSearch

In this project, you will design agents for the classic version of Pacman, including ghosts. Along the way, you will implement both minimax and expectimax search and try your hand at evaluation function design.


## Part 1 - Reflex Agent

A capable reflex agent will have to consider both food locations and ghost locations to perform well. 

```bash
$ python pacman.py -p ReflexAgent -l testClassic
```

## Part 2 - Minimax

The correct implementation of minimax will lead to Pacman losing the game in some tests. This is not a problem: as it is correct behaviour, it will pass the tests.

```bash
$ python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4
```

```bash
$ python pacman.py -p MinimaxAgent -l trappedClassic -a depth=3
```

## Part 3 - Alpha-Beta Pruning

```bash
$ python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic
```

## Part 4 - Expectimax


```bash
$ python pacman.py -p ExpectimaxAgent -l trappedClassic -a depth=3 -q -n 10
```




