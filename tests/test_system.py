import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from patient import register_patient
from test_catalog import get_available_tests
from test_request import create_test_request


def test_patient_registration():
    patient = register_patient("P001", "Gokul", 21)

    assert patient["patient_id"] == "P001"
    assert patient["name"] == "Gokul"
    assert patient["age"] == 21


def test_test_catalog():
    tests = get_available_tests()

    assert "Complete Blood Count (CBC)" in tests
    assert len(tests) > 0


def test_test_request():
    request = create_test_request(
        "P001",
        "Blood Glucose Test"
    )

    assert request["patient_id"] == "P001"
    assert request["test_name"] == "Blood Glucose Test"
    assert request["status"] == "Requested"