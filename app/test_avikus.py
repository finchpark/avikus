from app.main import app
from fastapi.testclient import TestClient
from httpx import AsyncClient

client = TestClient(app)

async def test_read_vessels():
	#response = client.get("/vessels/")
	async with AsyncClient(base_url="http://127.0.0.1:8000") as ac:
		response = await ac.get("/vessels/")
		assert response.status_code == 200
		assert response.json() == []

async def test_create_vessel():
	"""
	response = client.post(
		"/vessels/",
		json={
			"created": "2024-04-27T10:51:12.026000",
			"name": "Avikus",
			"content": "Avikus vessel create test"
		}
	)
	"""

	async with AsyncClient(base_url="http://127.0.0.1:8000") as ac:
		response = await ac.post(
			"/vessels/",
			json={
				"created": "2024-04-27T10:51:12.026000",
				"name": "Avikus",
				"content": "Avikus vessel create test"
			}
		)

		assert response.status_code == 200
		assert response.json() == {
			"created": "2024-04-27T10:51:12.026000",
			"name": "Avikus",
			"content": "Avikus vessel create test",
			"id": 1
		}

async def test_read_vessel():
	# response = client.get("/vessels/1")
	async with AsyncClient(base_url="http://127.0.0.1:8000") as ac:
		response = await ac.get("/vessels/1")
		assert response.status_code == 200
		assert response.json() == {
			"created": "2024-04-27T10:51:12.026000",
			"name": "Avikus",
			"content": "Avikus vessel create test",
			"id": 1
		}

async def test_update_vessel():
	"""
	response = client.put(
		"/vessels/1",
		json={
			"created": "2024-04-27T11:55:40.744Z",
			"name": "Avikus",
			"content": "Update Test"
		}
	)
	"""

	async with AsyncClient(base_url="http://127.0.0.1:8000") as ac:
		response = await ac.put(
			"/vessels/1",
			json={
				"created": "2024-04-27T11:55:40.744Z",
				"name": "Avikus",
				"content": "Update Test"
			}
		)

		assert response.status_code == 200
		assert response.json() == {
			"created": "2024-04-27T11:55:40.744000",
			"name": "Avikus",
			"content": "Update Test",
			"id": 1
		}

async def test_delete_vessel():
	#response = client.delete("/vessels/1")
	async with AsyncClient(base_url="http://127.0.0.1:8000") as ac:
		response = await ac.delete("/vessels/1")
		assert response.status_code == 200
		assert response.json() == {
			"message": "Vessel [1] deleted"
		}