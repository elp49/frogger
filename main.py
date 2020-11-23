import importlib
import sys

# *
## === ADDING IMPORTS === ##
# *

import time

# *
## === === ====== === === ##
# *

from util import Arguments

if __name__ == '__main__':

    args = Arguments()

#//# ===== ===== ==== = === = === = ==== ===== ===== #\\#
#//# ===== = = == === ORIGINAL CODE === == = = ===== #\\#
#//# ===== ===== ==== = === = === = ==== ===== ===== #\\#
    # player = args.get('player', 'agent')
    # screen = args.get('screen', 'medium')
    # steps = args.get_int('steps', None)
    # train = args.get('train', None)
    # speed = args.get('speed', 'fast' if train else 'slow')
    # restart = args.get_int('restart', None)
    # output = args.get('output', 'graphics')
#//# ===== ===== ==== = === = === = ==== ===== ===== #\\#
#//# ===== = = == === ************* === == = = ===== #\\#
#//# ===== ===== ==== = === = === = ==== ===== ===== #\\#



    ## ===== ===== = ===== ===== ##
    SCREEN = 'medium' # finished after 19.04 minutes with 
    # a score of 969605
    STEPS = 100000
    TRAINING_FILE = 'q8'
    RESTART = 4
    OUTPUT = 'text'

    player = args.get('player', 'agent')
    screen = args.get('screen', SCREEN)
    steps = args.get_int('steps', STEPS)
    train = args.get('train', TRAINING_FILE)
    speed = args.get('speed', 'fast')
    restart = args.get_int('restart', RESTART)
    output = args.get('output', OUTPUT)
    ## ===== ===== = ===== ===== ##

    from frogger.settings import settings
    settings['use_graphics'] = (output.lower() != 'text')

    from frogger.frogger import Frogger
    game = Frogger(screen)

    if player != 'human':
        agent_module = importlib.import_module(player)
        agent = agent_module.Agent(train=train)
        game.add_agent(agent)


    ## ===== ===== = ===== ===== ##
    ## === == =========== == === ##
    ## ===== ===== = ===== ===== ##
    then = time.time()
    ## ===== ===== = ===== ===== ##
    ## === == =========== == === ##
    ## ===== ===== = ===== ===== ##


    scores = game.run(steps=steps, speed=speed, restart=restart)
    

    ## ===== ===== = ===== ===== ##
    ## === == =========== == === ##
    ## ===== ===== = ===== ===== ##
    now = time.time()
    seconds = now - then
    minutes = seconds / 60
    print(f'{round(minutes, 2)} minutes')
    ## ===== ===== = ===== ===== ##
    ## === == =========== == === ##
    ## ===== ===== = ===== ===== ##


    print('\t'.join([str(score) for score in scores]))
