import pytest

from euclidean.rhythm import EuclideanRhythm


@pytest.mark.parametrize('steps,active,offset,expected_error', [
    (2, 4, 0, ValueError),
    (2, 2, 3, ValueError),
])
def test_fail_euclideanRhythms(steps, active, offset, expected_error):
    with pytest.raises(expected_error):
        EuclideanRhythm(steps, active, offset)


g8_4_0 = [True, False, True, False, True, False, True, False ]
e8_4_0 = EuclideanRhythm(8, 4, 0)

g13_5_0 = [True, False, False, True, False, True, False, False, True, False, True, False, False]
e13_5_0 = EuclideanRhythm(13, 5, 0)


@pytest.mark.parametrize('gates,expected_rhythm', [
    (g8_4_0, e8_4_0), # Trivial example
    (g13_5_0, e13_5_0), # Example from the paper
])
def test_euclidean_rhythm_from_gates(gates, expected_rhythm):
    assert EuclideanRhythm.from_gates(gates) == expected_rhythm


@pytest.mark.parametrize('rhythm,expected_gates', [
    (e8_4_0, g8_4_0), # Trivial example
    (e13_5_0, g13_5_0), # Example from the paper
])
def test_euclidean_rhythm_to_gates(rhythm, expected_gates):
    assert rhythm.to_gates() == expected_gates
