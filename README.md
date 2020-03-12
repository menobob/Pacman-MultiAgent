# PROJECT OVERVIEW

![pacman game](http://ai.berkeley.edu/images/pacman_game.gif)


###### Pacman - Search
> Implement depth-first, breadth-first, uniform cost, and A* search algorithms. These algorithms are used to solve navigation and traveling salesman problems in the Pacman world.


###### Pacman - Multi-Agent Search
> Classic Pacman is modelled as both an adversarial and a stochastic search problem. Implement multiagent minimax and expectimax algorithms, as well as designing evaluation functions.

###### Ghostbusters
> Probabilistic inference in a hidden Markov model tracks the movement of hidden ghosts in the Pacman world. Implement exact inference using the forward algorithm and approximate inference via particle filters.

# FIRST SECTION 
## Pacman-Search

Implemented depth-first, breadth-first, uniform cost, and A* search algorithms. These algorithms were used to solve navigation and traveling salesman problems in the Pacman world.


### Part 1 - Finding a Fixed Food Dot using Depth First Search

The command below tells the SearchAgent to use tinyMazeSearch as its search algorithm, which is implemented in search.py. Pacman should navigate the maze successfully.

```bash
$ python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch
```

The commands below utilises the DFS algorithm to allow Pacman to nagivate the different sized mazes successfully.

```bash
$ python pacman.py -l tinyMaze -p SearchAgent
```

```bash
$ python pacman.py -l mediumMaze -p SearchAgent
```

```bash
$ python pacman.py -l bigMaze -z .5 -p SearchAgent
```

### Part 2 - Breadth First Search

The commands below utilises the DFS algorithm to allow Pacman to nagivate the different sized mazes successfully.

```bash
$ python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
```

```bash
$ python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
```

**Note:** If Pacman moves slowly for you, try the option **--frametime 0**

### Part 3 - Varying the Cost Function

The commands below utilises the UCS algorithm to allow Pacman to nagivate the different sized mazes successfully.

```bash
$ python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
```

```bash
$ python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
```

```bash
$ python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
```

### Part 4 - A* search

The command below utilises the A* Search algorithm to allow Pacman to nagivate the different sized mazes successfully.

```bash
$ python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

### Part 5 - Finding All the Corners

In corner mazes, there are four dots, one in each corner. Our new search problem is to find the shortest path through the maze that touches all four corners (whether the maze actually has food there or not). **Note** that for some mazes like tinyCorners, the shortest path does not always go to the closest food first! 

```bash
$ python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```

```bash
$ python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```


### Part 6 - Eating All The Dots

Now we'll solve a hard search problem: eating all the Pacman food in as few steps as possible. 

```bash
$ python pacman.py -l trickySearch -p AStarFoodSearchAgent
```

### Part 7 - Suboptimal Search

Sometimes, even with A* and a good heuristic, finding the optimal path through all the dots is hard. In these cases, we'd still like to find a reasonably good path, quickly. In this section, you'll write an agent that always greedily eats the closest dot. 

```bash
$ python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5 
```

# SECOND SECTION
## Pacman-MultiAgentSearch

In this project, you will design agents for the classic version of Pacman, including ghosts. Along the way, you will implement both minimax and expectimax search and try your hand at evaluation function design.


### Part 1 - Reflex Agent

A capable reflex agent will have to consider both food locations and ghost locations to perform well. 

```bash
$ python pacman.py -p ReflexAgent -l testClassic
```

### Part 2 - Minimax

The correct implementation of minimax will lead to Pacman losing the game in some tests. This is not a problem: as it is correct behaviour, it will pass the tests.

```bash
$ python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4
```

```bash
$ python pacman.py -p MinimaxAgent -l trappedClassic -a depth=3
```

### Part 3 - Alpha-Beta Pruning

```bash
$ python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic
```

### Part 4 - Expectimax


```bash
$ python pacman.py -p ExpectimaxAgent -l trappedClassic -a depth=3 -q -n 10
```




