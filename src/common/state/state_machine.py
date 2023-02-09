from common.state.state import State

class StateMachine:
    state: State

    def __init__(self, initial_state: State):
        self.state = initial_state
    
    def enter(self, state: State):
        # self.state.exit()
        self.state = state
        # self.state.execute()