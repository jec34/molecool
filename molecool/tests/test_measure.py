"""
Tests for the measure module.
"""

#imports
import molecool
import numpy as np
import pytest

def test_calculate_distance():
    """
    Testing the calculate_distance function
    """
    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])
    expected_distance = 1

    calculated_distance = molecool.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance

def test_calculate_angle():
    """
    Testing the calculate_angle function
    """
    r1 = np.array([0, 0, -1])
    r2 = np.array([0, 0, 0])
    r3 = np.array([1, 0, 0])
    expected_angle = 90
    calculated_angle = molecool.calculate_angle(r1, r2, r3, degrees=True)

    expected_angle_rad = np.pi/2
    calculated_angle_rad = molecool.calculate_angle(r1, r2, r3)

    assert pytest.approx(expected_angle) == calculated_angle
    assert pytest.approx(expected_angle_rad) == calculated_angle_rad

@pytest.mark.parametrize('p1, p2, p3, expected_angle',
    [(np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0]), np.array([0, 0, 0]), np.array([1, 0, 0]), 45),
    (np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60)]
)
def test_calculate_angle_many(p1, p2, p3, expected_angle):
    calculated_value = molecool.calculate_angle(p1, p2, p3, degrees=True)
    assert pytest.approx(expected_angle) == calculated_value
