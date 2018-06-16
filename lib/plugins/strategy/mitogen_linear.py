# This is just a wrapper to workaround Ansibles inability to access PYTHONPATH
# from plugin config.

from ansible_mitogen.plugins.strategy.mitogen_linear import  StrategyModule
