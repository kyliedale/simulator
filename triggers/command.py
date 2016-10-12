class CommandTrigger():
    '''Generate signals from a block command'''

    def simulate(self):
        sigs = self.generate_signals()
        # If a generator is returned, build the list
        if not isinstance(sigs, list):
            sigs = list(sigs)
        self.notify_signals(sigs)
