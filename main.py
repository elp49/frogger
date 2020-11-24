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
    SCREEN = 'hard'
    STEPS = 3000


    # -----------------------------
    # TRAINING_FILE = 'q9_alpha0.1'
    # TRAINING_FILE = 'q9_alpha0.2'
    # TRAINING_FILE = 'q9_alpha0.3'
    # TRAINING_FILE = 'q9_alpha0.4'
    # TRAINING_FILE = 'q9_alpha0.5'
    # -----------------------------
    

    TRAINING_FILE = 'qx.1'
    # TRAINING_FILE = 'qx.2'
    # TRAINING_FILE = 'qx.3'
    # TRAINING_FILE = 'qx.4'
    SPEED = 'fast'
    RESTART = 8 # 1, 2, 3, 4, 5, 6, 7, 8
    # OUTPUT = 'graphic'
    OUTPUT = 'text'


    # --------------------------------------
    # output_file = 'test_runs_alpha0.1.txt'
    # output_file = 'test_runs_alpha0.2.txt'
    # output_file = 'test_runs_alpha0.3.txt'
    # output_file = 'test_runs_alpha0.4.txt'
    # output_file = 'test_runs_alpha0.5.txt'
    # --------------------------------------


    output_file = 'qx.1.log'
    # output_file = 'qx.2.log'
    # output_file = 'qx.3.log'
    # output_file = 'qx.4.log'

    player = args.get('player', 'agent')
    screen = args.get('screen', SCREEN)
    steps = args.get_int('steps', STEPS)
    train = args.get('train', TRAINING_FILE)
    speed = args.get('speed', SPEED)
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


    ## ===== ===== = ===== ===== ##
    ## === == =========== == === ##
    ## ===== ===== = ===== ===== ##
    with open(output_file, 'a') as f:
        f.write(f'\r\nRun:TRAINING_FILE={TRAINING_FILE}\n')
        f.write(f'\tSCREEN\t= {SCREEN}\n')
        f.write(f'\tSTEPS\t= {STEPS}\n')
        f.write(f'\tRESTART\t= {restart}\n')
        score = '\t'.join([str(score) for score in scores])
        f.write(f'\tscor\t= {score}\n')
        f.write(f'\ttime\t= {round(minutes, 2)} minutes\n')
        interval = Agent.DEFAULT_E_INTERVAL
        count = interval
        f.write(f'## == Average Rewards per {interval} episodes == ##')
        for r in agent.episode_rewards:
            f.write(f'\t{count} - {r/interval}')
