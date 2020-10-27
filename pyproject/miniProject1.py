class SemanticNetsAgent:
    def __init__(self):
        # Setting boat to LEFT bank initially
        self.boat = "LEFT"
        
        # Left, right banks hold (0, 0) (sheeps, wolves)
        self.leftBank = (0,0)
        self.rightBank = (0,0)


    def solve(self, initial_sheep, initial_wolves):
        # Loading initial sheep, wolves on left bank
        self.leftBank = (initial_sheep, initial_wolves)
    #Add your code here! Your solve method should receive
	#the initial number of sheep and wolves as integers,
	#and return a list of 2-tuples that represent the moves
	#required to get all sheep and wolves from the left
	#side of the river to the right.

test_agent = SemanticNetsAgent()

print(test_agent.solve(1, 1))
print(test_agent.solve(2, 2))
print(test_agent.solve(3, 3))
print(test_agent.solve(5, 3))
print(test_agent.solve(6, 3))
print(test_agent.solve(7, 3))
print(test_agent.solve(5, 5))