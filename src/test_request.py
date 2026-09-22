def create_test_request(patient_id, test_name):
    if not test_name:
        raise ValueError("Test name cannot be empty")

    return {
        "patient_id": patient_id,
        "test_name": test_name,
        "status": "Requested"
    }