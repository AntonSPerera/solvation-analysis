import numpy as np
import pytest

from solvation_analysis.analysis_library import (
    _IonSpeciation,
    _CoordinationNumber,
    _Pairing,
    _SolvationData
)


def test_solvation_data(solvation_results):
    solvation_data = _SolvationData(solvation_results)


@pytest.mark.parametrize(
    "name, percent",
    [
        ((4, 0, 0), 0.295),
        ((5, 0, 0), 0.357),
        ((3, 3, 0), 0.004),
        ((3, 0, 1), 0.016),
    ],
)
def test_ion_speciation(name, percent, solvation_data):
    speciation = _IonSpeciation(solvation_data).average_speciation
    np.testing.assert_allclose(percent, speciation[name], atol=0.05)


@pytest.mark.parametrize(
    "name, cn",
    [
        ("fec", 0.25),
        ("bn", 4.33),
        ("pf6", 0.15),
    ],
)
def test_coordination_numbers(name, cn, solvation_data):
    coord_dict = _CoordinationNumber(solvation_data).average_dict
    np.testing.assert_allclose(cn, coord_dict[name], atol=0.05)


@pytest.mark.parametrize(
    "name, percent",
    [
        ("fec", 0.21),
        ("bn", 1.0),
        ("pf6", 0.14),
    ],
)
def test_pairing(name, percent, solvation_data):
    pairing_dict = _Pairing(solvation_data).percentage_dict
    np.testing.assert_allclose([percent], pairing_dict[name], atol=0.05)
