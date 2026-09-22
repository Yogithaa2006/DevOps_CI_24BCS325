from src.sample_collection import track_sample


def test_sample_collection():
    sample = track_sample("S001", "P001", "Collected")

    assert sample["sample_id"] == "S001"
    assert sample["patient_id"] == "P001"
    assert sample["status"] == "Collected"