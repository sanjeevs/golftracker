'''
State machine to trace the golf swing through the poses.
'''

class SwingStateMachine:

    def start(self):
        self.state = self.start_state

    
    def step(self, inp):
        (s, o) = self.get_next_value(self.state, inp)
        self.state = s
        return o


    def feeder(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]


class RhGolfSwing(SwingStateMachine):
    start_state = IDLE

    def get_next_value(self, state, inp):
        if state == IDLE and inp[0] == gt.GolfPose.RhStart:
            return (START, inp[1])
        elif state == START and inp[0] == gt.GolfPose.RhTop:
            return (TOP, inp[1])
        elif state == TOP and inp[0] == gt.GolfPose.RhStart:
            return (START, inp[1])
        elif state == START and inp[0] == gt.GolfPose.RhFinish:
            return (FINISH, inp[1])
        else:
            return (IDLE, 0)
