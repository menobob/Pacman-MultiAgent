# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent


class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"

        score = successorGameState.getScore()

        for ghostState in newGhostStates:
            ghostPos = ghostState.getPosition()
            manhattanDistance = util.manhattanDistance(newPos, ghostPos)

            if manhattanDistance > 0 and manhattanDistance < 5:
                score -= 1.0 / manhattanDistance

        for foodPos in newFood.asList():
            manhattanDistance = util.manhattanDistance(newPos, foodPos)

            if manhattanDistance > 0:
                score += 1.0 / manhattanDistance

        return score



def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"

        bestAction = self.maxAgent(gameState, 0)
        return bestAction


    def maxAgent(self, gameState, depth):

        if gameState.isLose() or gameState.isWin():
            return self.evaluationFunction(gameState)

        actions = gameState.getLegalActions(0)

        value = float("-inf")

        values = []

        for action in actions:
            values.append(self.minAgent(gameState.generateSuccessor(0, action), 1, depth))

        if depth == 0:
            index = max(xrange(len(values)), key=values.__getitem__)
            return actions[index]

        else:
            return max(values)

    def minAgent(self, gameState, agent, depth):

        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        actions = gameState.getLegalActions(agent)

        value = float("inf")

        next_agent = (agent+1) % gameState.getNumAgents()

        for action in actions:

            next_State = gameState.generateSuccessor(agent, action)

            if next_agent == 0:
                if depth == self.depth - 1:
                    next_value = self.evaluationFunction(next_State)
                else:
                    next_value = self.maxAgent(next_State, depth + 1)
            else:
                next_value = self.minAgent(next_State, next_agent, depth)

            value = min(next_value, value)

        return value



class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        bestAction = self.maxAgent(gameState, 0, float("-inf"), float("inf"))
        return bestAction


    def maxAgent(self, gameState, depth, alpha, beta):

        if gameState.isLose() or gameState.isWin():
            return self.evaluationFunction(gameState)

        actions = gameState.getLegalActions(0)

        values = []

        for action in actions:

            values.append(self.minAgent(gameState.generateSuccessor(0, action), 1, depth, alpha, beta))

            alpha = max(alpha, max(values))

            if max(values) >= beta:
                return max(values)

        if depth == 0:
            index = max(xrange(len(values)), key=values.__getitem__)
            return actions[index]

        else:
            return max(values)

    def minAgent(self, gameState, agent, depth, alpha, beta):

        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        next_agent = (agent+1) % gameState.getNumAgents()

        value = float("inf")

        actions = gameState.getLegalActions(agent)

        for action in actions:

            next_State = gameState.generateSuccessor(agent, action)

            if next_agent == 0:
                if depth == self.depth - 1:
                    next_value = self.evaluationFunction(next_State)
                else:
                    next_value = self.maxAgent(next_State, depth + 1, alpha, beta)
            else:
                next_value = self.minAgent(next_State, next_agent, depth, alpha, beta)

            value = min(next_value, value)
            beta = min(beta, value)

            if value <= alpha:
                return value

        return value


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"

        actions = gameState.getLegalActions(0)
        value = float("-inf")

        bestAction = None

        for action in actions:

            current_state = gameState.generateSuccessor(0, action)
            prev_value = value

            value = max(self.expectedValue(current_state, 1, self.depth), value)

            if prev_value < value:
                bestAction = action

        return bestAction


    def maxValue(self, gameState, depth):

        if gameState.isWin() or gameState.isLose() or depth == 0:
            return self.evaluationFunction(gameState)

        actions = gameState.getLegalActions(0)

        value = float("-inf")

        for action in actions:

            next_state = gameState.generateSuccessor(0, action)

            next_value = self.expectedValue(next_state, 1, depth)

            if next_value > value:
                value = next_value

        return value


    def expectedValue(self, gameState, agent, depth):

        value = 0
        total_values = 0

        if gameState.isWin() or gameState.isLose() or depth == 0:
            return self.evaluationFunction(gameState)

        actions = gameState.getLegalActions(agent)

        number_Of_Ghosts = gameState.getNumAgents() - 1

        for action in actions:

            next_state = gameState.generateSuccessor(agent, action)

            if agent == number_Of_Ghosts:
                total_values += self.maxValue(next_state, depth - 1)
                value = total_values
            else:
                total_values += self.expectedValue(next_state, agent+1, depth)
                value = total_values

        avg = value / len(actions)

        return avg


def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>

        The evaluated score is dependent on the ghosts positions, scare times and food positions. Each feature which
        has an impact on the score have different values multiplied to them to signify importance. Finding the
        manhattan distance between pacman and the ghosts effects the score negatively and is considered the one of the
        most important features due to the risk of gameOver. Finding the manhattan distance between all the food has a
        positive effect on the score. Scared Times left over for the ghosts is also very valuable as pacman essentially
        has the power to free roam during those times so the score is increased with a high value multiple

    """
    "*** YOUR CODE HERE ***"

    position = currentGameState.getPacmanPosition()

    food = currentGameState.getFood()
    foodList = food.asList()

    ghostStates = currentGameState.getGhostStates()
    ghostScaredTimes = [ghostState.scaredTimer for ghostState in ghostStates]

    score = currentGameState.getScore()

    for ghostState in ghostStates:
        ghostPos = ghostState.getPosition()
        manhattanDistance = util.manhattanDistance(position, ghostPos)

        if manhattanDistance > 0 and manhattanDistance < 5:
            score -= 1.0 / manhattanDistance * 3

    for foodPos in foodList:
        manhattanDistance += util.manhattanDistance(position, foodPos)

        if manhattanDistance > 0:
            score += 1.0 / manhattanDistance * 2

    score += sum(ghostScaredTimes) * 4

    return score

# Abbreviation
better = betterEvaluationFunction