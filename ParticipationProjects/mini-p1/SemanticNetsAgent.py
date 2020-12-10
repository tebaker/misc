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

    def getLBank(self):
        return self.leftBank

    def getRBank(self):
        return self.rightBank

    def print(self):
        print("\tLeft Bank:  ", self.leftBank.getSheep(), self.leftBank.getWolves())
        print("\tRight Bank: ", self.rightBank.getSheep(), self.rightBank.getWolves())
        print("\tBoat Loc:   ", self.boatLoc, "\n")

class Bank:
    def __init__(self, initial_sheep, initial_wolves):
        self.sheep = initial_sheep
        self.wolves = initial_wolves

    def setSheepWolves(self, newSheep, newWolves):
        self.sheep = newSheep
        self.wolves = newWolves

    def getSheep(self):
        return int(self.sheep)
    
    def getWolves(self):
        return int(self.wolves)

class SemanticNetsAgent:
    def __init__(self):
        # Holding list of tuples required to solve the problem
        self.listOfTuples = []

        self.previouslyEncounteredStates = []

        # Holding the generations
        self.unevaluatedStates = []

        # If the game is still in progress, inProgress is True
        self.inProgress = True

    # Solve will take in an initial sheep, wolves amount and run a loop while
    # the game is still in progress
    def solve(self, initial_sheep, initial_wolves):
        # Setting initial state
        leftBank = Bank(initial_sheep, initial_wolves)
        rightBank = Bank(0, 0)
        currentState = State(leftBank, rightBank, "left")
        
        print("Current State:")
        currentState.print()

        print("++++++++++++++++++++++++++++++++++++++++")
        print("++++++++++++++++++++++++++++++++++++++++")

        self.unevaluatedStates.append(currentState)
        self.previouslyEncounteredStates.append(currentState)

        self.generateAndTest(currentState)

    # Generate will populate a list of all possible next-states the game
    # progress to regardless of legality or not
    def generateAndTest(self, currentState):
        while self.inProgress:
            for i in self.unevaluatedStates:
                i.print()

            print("========================================")

            # Getting left bank sheep, wolves
            lBankSheep = currentState.leftBank.getSheep()
            lBankWolves = currentState.leftBank.getWolves()

            # Getting right bank sheep, wolves
            rBankSheep = currentState.rightBank.getSheep()
            rBankWolves = currentState.rightBank.getWolves()

            # Getting current boat location
            currBoatLoc = currentState.getBoatLoc()

            if currentState.leftBank.getSheep() == 0 and currentState.leftBank.getWolves() == 0:
                self.inProgress = False
                print("FINISHED!")
                print(self.listOfTuples)
            
            elif currBoatLoc == "left":
                # Possible generations for LEFT bank:
                # 1 sheep, 1 wolf
                if lBankSheep - 1 >= 0 and lBankWolves - 1 >= 0:
                    holdState = State(Bank(lBankSheep-1, lBankWolves-1), Bank(rBankSheep+1, rBankWolves+1), "right")
                    if self.test(holdState, "left"):
                        self.unevaluatedStates.append(holdState)
                        self.listOfTuples.append((1, 1))
                        self.previouslyEncounteredStates.append(holdState)
                # 1 sheep, 0 wolves
                if lBankSheep -1 >= 0:
                    holdState = State(Bank(lBankSheep-1, lBankWolves), Bank(rBankSheep+1, rBankWolves), "right")
                    if self.test(holdState, "left"):
                        self.unevaluatedStates.append(holdState)
                        self.listOfTuples.append((1, 0))
                        self.previouslyEncounteredStates.append(holdState)
                # 0 sheep, 1 wolf
                if lBankWolves -1 >= 0:
                    holdState = State(Bank(lBankSheep, lBankWolves-1), Bank(rBankSheep, rBankWolves+1), "right")
                    if self.test(holdState, "left"):
                        self.unevaluatedStates.append(holdState)
                        self.listOfTuples.append((0, 1))
                        self.previouslyEncounteredStates.append(holdState)
            else:
                # Possible generations for RIGHT bank:
                # 1 sheep, 1 wolf
                if rBankSheep - 1 >= 0 and rBankWolves - 1 >= 0:
                    holdState = State(Bank(lBankSheep+1, lBankWolves+1), Bank(rBankSheep-1, rBankWolves-1), "left")
                    if self.test(holdState, "right"):
                        self.unevaluatedStates.append(holdState)
                        self.listOfTuples.append((1, 1))
                        self.previouslyEncounteredStates.append(holdState)
                # 1 sheep, 0 wolves
                if rBankSheep -1 >= 0:
                    holdState = State(Bank(lBankSheep+1, lBankWolves), Bank(rBankSheep-1, rBankWolves), "left")
                    if self.test(holdState, "right"):
                        self.unevaluatedStates.append(holdState)
                        self.listOfTuples.append((1, 0))
                        self.previouslyEncounteredStates.append(holdState)
                # 0 sheep, 1 wolf
                if rBankWolves -1 >= 0:
                    holdState = State(Bank(lBankSheep, lBankWolves+1), Bank(rBankSheep, rBankWolves-1), "left")
                    if self.test(holdState, "right"):
                        self.unevaluatedStates.append(holdState)
                        self.listOfTuples.append((0, 1))
                        self.previouslyEncounteredStates.append(holdState)
                        

    # Test will take in list of generated possible next-states and evaluate
    # them for legality, discarding the illegal next-states
    def test(self, checkState, fromLoc):
        lSheep  = checkState.getLBank().getSheep()
        lWolves = checkState.getLBank().getWolves()

        rSheep  = checkState.getRBank().getSheep()
        rWolves = checkState.getRBank().getWolves()

        checkPass = True

        # The following will make a state illegal:
        # If the boat took only one animal to an empty side
        if fromLoc == "left":
            if rSheep + rWolves == 1:
                checkPass = False
        else:
            if lSheep + lWolves == 1:
                checkPass = False
        
        # If the number of wolves outweight the number of sheeps on either side
        if lWolves > lSheep:
            checkPass = False
        elif rWolves > rSheep:
            checkPass = False
        
        # If the check state has been incountered before (contained within generatedStates list),
        # it is an illegal state
        if checkPass:
            for state in self.previouslyEncounteredStates:
                if state.getLBank().getSheep() == lSheep:
                    if state.getLBank().getWolves() == lWolves:
                        if state.getRBank().getSheep() == rSheep:
                            if state.getRBank().getWolves() == rWolves:
                                # State encountered before; illegal
                                checkPass = False

        if checkPass:
            return True
        else:
            return False


test_agent = SemanticNetsAgent()
# print(test_agent.solve(1, 1))
print(test_agent.solve(2, 2))
# print(test_agent.solve(3, 3))
# print(test_agent.solve(5, 3))
# print(test_agent.solve(6, 3))
# print(test_agent.solve(7, 3))
# print(test_agent.solve(5, 5))