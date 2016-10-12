from unittest.mock import MagicMock
from time import sleep
from ...triggers.command import CommandTrigger
from nio import Signal, Block
from nio.testing.block_test_case import NIOBlockTestCase

class SampleCommandBlock(CommandTrigger, Block):
    pass

class TestCommand(NIOBlockTestCase):

    def test_command_default(self):
        '''Test that signals are notified when command is triggered'''
        block = SampleCommandBlock()
        self.configure_block(block, {})
        returns = [Signal()]
        block.generate_signals = MagicMock(return_value=returns)
        block.start()
        self.assert_num_signals_notified(0)
        block.simulate()
        block.stop()
        self.assert_num_signals_notified(1)
