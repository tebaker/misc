# State will hold one instance of the game state in the form of:
# 1) Amount of sheep, wolves on left bank
# 2) Amount of sheep, wolves of right bank
# 3) Current location of the boat; left bank or right bank 
class State:
    def __init__(self, lBank, rBank, boatLocation):
        self.leftBank = lBank
        self.rightBank = rBank
        self.boatLoc = boatLocation
    
    def getBoatLoc(self):
        return self.boatLoc

    def print(self):
        print("Left Bank: ", (self.leftBank.getSheep(), self.leftBank.getWolves()))
        print("Right Bank: ", (self.rightBank.getSheep(), self.rightBank.getWolves()))
        print("Boat Loc: ", self.boatLoc, "\n")

class Bank:
    def __init__(self, initial_sheep, initial_wolves):
        self.sheeps = initial_sheep
        self.wolves = initial_wolves

    def setSheepWolves(self, newSheep, newWolves):
        self.sheeps = newSheep
        self.wolves = newWolves

    def getSheep(self):
        return self.sheeps
    
    def getWolves(self):
        return self.wolves

class SemanticNetsAgent:
    def __init__(self):
        # Holding list of tuples required to solve the problem
        self.listOfTuples = []

        # Holding list of all previous states
        self.listOfPreviousStates = []

        # If the game is still in progress, inProgress is True
        self.inProgress = True

    # Solve will take in an initial sheep, wolves amount and run a loop while
    # the game is still in progress
    def solve(self, initial_sheep, initial_wolves):
        # Setting initial state
        leftBank = Bank(initial_sheep, initial_wolves)
        rightBank = Bank(0, 0)
        currentState = State(leftBank, rightBank, "left")
        
        # Adding initial state to list of previous states
        self.listOfPreviousStates.append(currentState)

        while self.inProgress:
            self.generate(currentState)
            break

    # Generate will populate a list of all possible next-states the game
    # progress to regardless of legality or not
    def generate(self, currentState):
        # Holding the generations
        generatedStates = []

        # Getting left bank sheep, wolves
        lBankSheep = currentState.leftBank.getSheep()
        lBankWolves = currentState.leftBank.getWolves()

        # Getting right bank sheep, wolves
        rBankSheep = currentState.rightBank.getSheep()
        rBankWolves = currentState.rightBank.getWolves()

        # Getting current boat location
        currBoatLoc = currentState.getBoatLoc()

        if currBoatLoc == "left":    
            # Possible generations for left bank:
            # 1 sheep, 1 wolf
            if lBankSheep - 1 >= 0 and lBankWolves - 1 >= 0:
                generatedStates.append()
            # 1 sheep, 0 wolves
            # 0 sheep, 1 wolf

    # Test will take in list of generated possible next-states and evaluate
    # them for legality, discarding the illegal next-states
    def test(self):
        pass

    def printStates(self, statesList):
        for state in statesList:
            print(state.getState())

test_agent = SemanticNetsAgent()
print(test_agent.solve(1, 1))
print(test_agent.solve(2, 2))
print(test_agent.solve(3, 3))
print(test_agent.solve(5, 3))
print(test_agent.solve(6, 3))
print(test_agent.solve(7, 3))
print(test_agent.solve(5, 5))