from patient import register_patient
from test_catalog import get_available_tests
from test_request import create_test_request


def main():
    print("Medical Laboratory Test Management System")
    print("-----------------------------------------")

    # Patient Registration
    patient = register_patient("P001", "Gokul", 21, "9150268660")

    print("\nPatient Registered:")
    print(patient)

    # Display Available Tests
    print("\nAvailable Laboratory Tests:")

    available_tests = get_available_tests()

    for test in available_tests:
        print("-", test)

    # Create Test Request
    request = create_test_request(
        "P001",
        "Blood Glucose Test"
    )

    print("\nTest Request:")
    print(request)


if __name__ == "__main__":
    main()