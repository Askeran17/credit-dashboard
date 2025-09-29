def test_create_and_list_and_delete_institution(test_client):
    payload = {
        "name": "TestBank",
        "country": "Sweden",
        "founding_year": 2020,
        "total_portfolio": 1000000,
        "credit_risk_score": 0.1,
        "product_type": "Business",
        "website_url": "https://example.com",
        "contacts": ["info@example.com"]
    }

    # Create
    r = test_client.post("/api/institutions", json=payload)
    assert r.status_code == 200
    inst_id = r.json()["id"]
    assert len(inst_id) >= 10

    # List
    r = test_client.get("/api/institutions")
    assert r.status_code == 200
    items = r.json()
    assert any(it["_id"] == inst_id for it in items)

    # Delete
    r = test_client.delete(f"/api/institutions/{inst_id}")
    assert r.status_code == 200
    assert r.json().get("status") == "deleted"
