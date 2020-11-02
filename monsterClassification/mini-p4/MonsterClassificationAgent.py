class MonsterClassificationAgent:
    def __init__(self):
        # In this classification, 'None' designates that the outcome doesn't matter
        self.aMonster = {
            'size': {'huge', 'large'},
            'color': {'black', 'white'},
            'covering': 'fur',
            'foot-type': {'paw', 'foot'},
            'leg-count': {1, 2},
            'arm-count': {3, 4},
            'eye-count': 2,
            'horn-count': 0,
            'lays-eggs': True,
            'has-wings': True,
            'has_gills': None,
            'has-tail': None
        }
    
    def solve(self, samples, new_monster):
        #Add your code here!
        #
        #The first parameter to this method will be a labeled list of samples in the form of
        #a list of 2-tuples. The first item in each 2-tuple will be a dictionary representing
        #the parameters of a particular monster. The second item in each 2-tuple will be a
        #boolean indicating whether this is an example of this species or not.
        #
        #The second parameter will be a dictionary representing a newly observed monster.
        #
        #Your function should return True or False as a guess as to whether or not this new
        #monster is an instance of the same species as that represented by the list.
        return False

