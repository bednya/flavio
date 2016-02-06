import unittest
import numpy as np
from .bvlnu import *
from flavio.physics.bdecays.formfactors.b_v import bsz_parameters
from flavio.physics.eft import WilsonCoefficients
from flavio.parameters import default_parameters
import copy
import flavio

constraints = default_parameters
wc_obj = WilsonCoefficients()
par = constraints.get_central_all()

class TestBVll(unittest.TestCase):
    def test_brhoee(self):
        q2 = 3.5
        self.assertEqual(
            dBRdq2(q2, wc_obj, par, 'B0', 'rho+', 'e'),
            flavio.Observable.get_instance("dBR/dq2(B0->rhoenu)").prediction_central(constraints, wc_obj, q2=q2) )
