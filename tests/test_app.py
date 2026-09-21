from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_delete_participant_removes_email():
    activity_name = "Soccer Club"
    email = "new.student@mergington.edu"

    client.post(f"/activities/{activity_name}/signup?email={email}")

    response = client.delete(f"/activities/{activity_name}/participants/{email}")

    assert response.status_code == 200
    assert response.json()["message"] == f"Removed {email} from {activity_name}"

    details = client.get("/activities").json()[activity_name]
    assert email not in details["participants"]
