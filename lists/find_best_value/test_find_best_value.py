from unittest import TestCase
from find_best_value import find_best_value, binary_search

class BinarySearchTest(TestCase):

    def setUp(self):
        self.bs_arr = [i for i in range(100)]

    def test_01_binary_search(self):
        self.assertEqual(binary_search(self.bs_arr, 34), 34)

    def test_02_binary_search(self):
        self.assertEqual(binary_search(self.bs_arr, 99), 99)

    def test_03_binary_search(self):
        self.assertEqual(binary_search(self.bs_arr, 0), 0)


class FindBestValueTest(TestCase):

    def test_01_find_best_value(self):
        test_result = find_best_value([4,9,3], 10)
        self.assertEqual(test_result, 3)

    def test_02_find_best_value(self):
        test_result = find_best_value([2,3,5], 10)
        self.assertEqual(test_result, 5)

    def test_03_find_best_value(self):
        test_result = find_best_value([60864,25176,27249,21296,20204], 56803)
        self.assertEqual(test_result, 11361)

    def test_04_find_best_value(self):
        test_result = find_best_value([98331,74849,36554,76848,67364,37774,36474,86098,47985,79997,93263,8977,55296,70201,57183,25088,34571,66968,59393,93574,65113,94975,44717,81346,88218,85683,73928,72939,21302,63139,91102,21384,87858,10037,7500,51972,8821,82881,82949,95897,26754,41909,80371,7761,85719,88377,7905,65679,28087,91911,59868,93562,44999,35212,11325,83327,51170,71475,66396,25904,84006,74076,97039,91699,79111,11193,44149,36111,85768,6481,99389,23982,29960,3671,56279,48263,80369,34039,26653,2463,25725,1465,21895,91468,72513,74036,78972,97328,66223,33906,8983,89888,34473,19688,40471,11250,6103,25664,40821,40240,17165,81072,23514,94510,87222,41864,21279,12748,40052,90551,40534,24036,78569,67743,73449,85998,61102,6578,34268,28364,68598,77215,99452,68465,97702,38153,29107,24352,77368,3288,61290,58407,54260,64894,27951,25037,14087,79619,40676,68806,30628,19239,59526,19091,10014,35576,75763,27633,56108,93884,84082,66264,82354,10029,21122,37293,7638,65895,30655,15512,2192,90441,1186,89284,48713,78697,98556,54222,6980,10242,16479,45481,10988,37308,6497,81827,41660,21700,84351,80393,30638,70897,16543,11680,96748,53529,60768,79998,70655,21212,65980,26919,11833,34637,61413,82505,81241,80034,27271,85638,17373,69597,87139,3104,97261,73508,67542,43730,84814,60771,74978,88240,49431,43559,50939,12175,44159,51873,97383,17498,98105,53561,3160,91570,79110,18607,54923,62582,75648,93567,82579,64671,23534,30592,35461,21555,16390,21506,68216,33793,24860,22041,64427,15331,73480,1786,25674,15398,56777,87649,53264,2714,82276,81006,41715,69811,45817,36684,98422,85662,43492,43470,93576,85814,7705,41316,47527,73452,12532,13580,31918,47233,45099,30693,40660,16509,14207,65907,35990,62311,7749,82916,15416,56145,83858,51040,37819,96989,1154,65187,46219,13302,31193,62433,93326,89301,59128,93860,28307,45645,75682,77281,3425,50973,94656,366,35654,76605,59102,64229,50018,75178,57057,13021,52850,48265,45778,40795,97937,45224,69220,70920,34549,79786,9178,12887,96702,31491,19744,57111,71611,31373,9031,55848,27560,85231,2805,40915,52892,82794,95867,26168,66784,94531,20123,86186,67022,79748,13184,88226,56515,34423,64766,85931,22892,91624,74486,24218,41865,23689,29992,95465,12592,30423,95058,57266,45424,798,85823,68320,31103,98925,45540,98868,18166,86561,74260,56266,89911,9129,83371,97484,22500,99295,69568,40693,90452,37517,66393,6657,92784,64080,16568,75540,48116,72821,27576,7365,80772,48543,93509,87384,43040,25891,67722,91874,6001,63729,39797,84517,87534,21062,69167,1879,40680,54010,81103,3630,40346,43903,83165,8313,41816,66548,66442,51197,48698,1225,21885,93398,43341,43533,33051,38075,77122,61771,65330,94428,7679,6085,29606,93522,95206,69219,66702,13418,38693,76415,93045,97898,32810,40164,93470,62377,11158,86758,24882,67441,86224,74427,19169,92144,88604,8201,65903,30473,28793,45833,88290,93845,64824,92321,80994,11318,64175,97208,3317,17313,1097,68395,20915,15299,95460,95991,16309,93175,30529,29369,16019,23449,26759,29622,99688,2569,55021,33419,67726,51598,92142,99404], 61732)
        self.assertEqual(test_result, 123)