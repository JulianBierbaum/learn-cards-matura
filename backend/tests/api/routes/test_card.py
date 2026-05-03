
def test_get_all_ok(client_without_superuser, test_card1, test_card2):
    response = client_without_superuser.get("/api/card/")

    assert response.status_code == 200
    assert "test_card_1" in str(response.json())
    assert len(response.json()[0]["tags"]) == 2

def test_delete_not_found(client_without_superuser):
    response = client_without_superuser.delete(f"/api/card/10")

    assert response.status_code == 404
    assert "not found" in str(response.json())