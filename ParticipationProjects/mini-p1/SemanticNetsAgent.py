class SemanticNetsAgent:
    def __init__(self):
        self.listOfTuples = []
        pass

    def solve(self, initial_sheep, initial_wolves):
        '''
        Given the initial number of sheeps and wolves, what are my legal moves
        
        '''
        pass





# The wolves can never outnumber the sheep
# The boat must take 1 or 2 animals per trip

test_agent = SemanticNetsAgent()
print(test_agent.solve(1, 1))
print(test_agent.solve(2, 2))
print(test_agent.solve(3, 3))
print(test_agent.solve(5, 3))
print(test_agent.solve(6, 3))
print(test_agent.solve(7, 3))
print(test_agent.solve(5, 5))