def create_test_request(patient_id, test_name):
    return {
        "patient_id": patient_id,
        "test_name": test_name,
        "status": "Requested"
    }