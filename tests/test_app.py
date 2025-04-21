import pytest
from app.models import TravelDestination


# Test GET /destinations
def test_get_destinations(db_session, client):
    # Clear existing data
    db_session.query(TravelDestination).delete()
    db_session.commit()

    # Add a test destination
    destination = TravelDestination(name="Seoul", country="South Korea", description="A vibrant city")
    db_session.add(destination)
    db_session.commit()

    # GET request
    response = client.get("/destinations/")
    assert response.status_code == 200

    data = response.json()
    assert len(data) > 0
    assert data[0]["name"] == "Seoul"
    assert data[0]["country"] == "South Korea"


# Test POST /destinations
def test_create_destination(db_session, client):
    new_destination = {
        "name": "Tokyo",
        "country": "Japan",
        "description": "The capital of Japan"
    }

    response = client.post("/destinations/", json=new_destination)
    assert response.status_code == 200

    data = response.json()
    assert data["name"] == "Tokyo"
    assert data["country"] == "Japan"
    assert data["description"] == "The capital of Japan"

    # Confirm in DB
    db_destination = db_session.query(TravelDestination).filter_by(name="Tokyo").first()
    assert db_destination is not None


# Test PUT /destinations/{id}
def test_update_destination(db_session, client):
    destination = TravelDestination(name="Paris", country="France", description="The city of love")
    db_session.add(destination)
    db_session.commit()

    updated_data = {
        "name": "Paris Updated",
        "country": "France",
        "description": "The updated city of love"
    }

    response = client.put(f"/destinations/{destination.id}", json=updated_data)
    assert response.status_code == 200

    data = response.json()
    assert data["name"] == "Paris Updated"
    assert data["description"] == "The updated city of love"

    # Confirm DB update
    db_destination = db_session.query(TravelDestination).filter_by(id=destination.id).first()
    assert db_destination.name == "Paris Updated"


# Test DELETE /destinations/{id}
def test_delete_destination(db_session, client):
    destination = TravelDestination(name="Berlin", country="Germany", description="The capital of Germany")
    db_session.add(destination)
    db_session.commit()

    response = client.delete(f"/destinations/{destination.id}")
    assert response.status_code == 200

    # Confirm deletion
    db_destination = db_session.query(TravelDestination).filter_by(id=destination.id).first()
    assert db_destination is None
