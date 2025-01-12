import unittest

import deepchem as dc
from deepchem.splits.splitters import ScaffoldSplitter


class TestScaffoldSplitter(unittest.TestCase):

    def test_scaffolds(self):
        tox21_tasks, tox21_datasets, transformers = \
          dc.molnet.load_tox21(featurizer='GraphConv')
        train_dataset, valid_dataset, test_dataset = tox21_datasets

        splitter = ScaffoldSplitter()
        scaffolds_separate = splitter.generate_scaffolds(train_dataset)
        scaffolds_train, scaffolds_valid, _ = splitter.split(train_dataset)

        # The amount of datapoints has to be the same
        data_cnt = sum([len(sfd) for sfd in scaffolds_separate])
        self.assertTrue(data_cnt == train_dataset.X.shape[0])

        # The number of scaffolds generated by the splitter
        # has to be smaller or equal than number of total molecules
        scaffolds_separate_cnt = len(scaffolds_separate)
        self.assertTrue(scaffolds_separate_cnt <= train_dataset.X.shape[0])
