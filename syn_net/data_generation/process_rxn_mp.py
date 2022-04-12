"""
This file processes a set of reaction templates and finds applicable
reactants from a list of purchasable building blocks.

Usage:
    python process_rxn_mp.py
"""
import multiprocessing as mp
from time import time

from syn_net.utils.data_utils import Reaction, ReactionSet
import syn_net.data_generation._mp_process as process
import shutup
shutup.please()


if __name__ == '__main__':
    name = 'pis'
    path_to_rxn_templates = '/home/ec2-user/SynNet/data/rxn_set_hb.txt'
    rxn_templates = []
    for line in open(path_to_rxn_templates, 'rt'):
        rxn = Reaction(line.split('|')[1].strip())
        rxn_templates.append(rxn)

    pool = mp.Pool(processes=64)

    t = time()
    rxns = pool.map(process.func, rxn_templates)
    print('Time: ', time() - t, 's')

    r = ReactionSet(rxns)
    r.save('/home/ec2-user/SynNet/reactions_' + name + '.json.gz')
