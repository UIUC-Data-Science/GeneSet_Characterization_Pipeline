import yaml
import unittest
from unittest import TestCase
import geneset_characterization_toolbox as tl
import pandas as pd
import numpy as np


class TestRun_DRaWR(TestCase):
    def setUp(self):
        self.run_parameters = {"gg_network_name_full_path":"../../data/networks/test1_gene_gene.edge",
                               "pg_network_name_full_path":"../../data/networks/test1_property_gene.edge",
                               "spreadsheet_name_full_path":"../../data/spreadsheets/test1_spreadsheet.tsv",
                               "results_directory":"../../data/verification",
                               "rwr_max_iterations":500,
                               "rwr_convergence_tolerence":1.0e-4,
                               "rwr_restart_probability":0.5}
        # with open("unit_test_run_dir/DRaWR.yml", 'r') as file_handle:
        #     self.run_parameters = yaml.load(file_handle)

    def tearDown(self):
        del self.run_parameters

    def test_run_DRaWR(self):
        ret = tl.run_DRaWR(self.run_parameters)
        ret.index = np.arange(ret.shape[0])
        res = pd.DataFrame(['P7', 'P6'], columns=['user1'])
        comp = ret.equals(res)
        self.assertEqual(True, comp)

if __name__ == '__main__':
    unittest.main()