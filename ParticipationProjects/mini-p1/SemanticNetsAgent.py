class Bank:
    def __init__(self, initial_sheep, initial_wolves):
        self.sheeps = initial_sheep
        self.wolves = initial_wolves

    def setSheepWolves(self, newSheep, newWolves):
        self.sheeps = newSheep
        self.wolves = newWolves

class SemanticNetsAgent:
    def __init__(self):
        # Holding list of tuples required to solve the problem
        self.listOfTuples = []

        # Holding list of previosly explored states
        self.previousStates = []

        # Holding current states of left, right banks for sheep, wolf information.
        # leftBank = [[sheep, wolves]], rightBank = [[sheep, wolves]]
        self.leftBank = Bank(0, 0)
        self.rightBank = Bank(0, 0)

        # Indicating if the boat is currently on the left or right bank
        self.boatLeft = True

        # Bool for if win condition is reached
        self.stillComputing = True

    def solve(self, initial_sheep, initial_wolves):
        # Loading left, right banks with their animals
        self.leftBank.setSheepWolves(initial_sheep, initial_wolves)
        self.rightBank.setSheepWolves(0, 0)

        while self.stillComputing:
            # Loading the first previous state - the initial state
            self.previousStates.append([self.leftBank, self.rightBank])

            # If left bank is empty, game complete. Return list of moves (tuples)
            if self.leftBank == [0, 0]:
                return self.listOfTuples
            # If left bank not empty, generate list of moves to consider
            else:
                # If boat on left, generate possible moves for left bank to right bank
                if self.boatLeft:
                    self.generateAndTest(self.leftBank, self.rightBank)
                # If boat is right, generate from right to left
                else:
                    self.generateAndTest(self.rightBank, self.leftBank)


    def generateAndTest(self, fromBank, toBank):        
        # Three possible ways to fill the boat:
        # 1) 1 sheep, 1 wolf:
        #    If sheep AND wolves greater than 0 and if wolves don't outnumber sheep
        if fromBank.sheep > 0 and fromBank.wolves > 0 and fromBank.sheep - 1 < fromBank.wolves - 1:
            # Checking if sheep greater than or equal to wolves on other side of bank
            if toBank.sheep + 1 >= toBank.wolves + 1:
                # Checking if previous state has been seen before
                for states in self.previousStates:
                    # Checking left bank sheeps, wolves
                    if 

        # 2) 1 sheep, 0 wolf
        # 3) 0 sheep, 1 wolf

test_agent = SemanticNetsAgent()
print(test_agent.solve(1, 1))
print(test_agent.solve(2, 2))
print(test_agent.solve(3, 3))
print(test_agent.solve(5, 3))
print(test_agent.solve(6, 3))
print(test_agent.solve(7, 3))
print(test_agent.solve(5, 5))