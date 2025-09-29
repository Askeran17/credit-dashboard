import os
from pathlib import Path
import sys
import mongomock
import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope="session")
def test_client():
    # Ensure env vars so backend imports cleanly
    os.environ.setdefault("ENV", "test")
    os.environ.setdefault("MONGO_URI", "mongodb://localhost:27017")

    project_root = Path(__file__).resolve().parents[1]
    # Ensure backend dir is on sys.path so `routes` and `main` are importable
    sys.path.insert(0, str(project_root))

    # Ensure static dir exists for StaticFiles mount in non-dev
    static_dir = project_root / "static"
    static_dir.mkdir(exist_ok=True)

    # Import app after env prepared
    from routes import institutions as inst_mod
    from routes import loans as loans_mod
    from main import app

    # Replace real db with in-memory mongomock
    mock_client = mongomock.MongoClient()
    mock_db = mock_client["credit_dashboard_test"]
    inst_mod.db = mock_db
    loans_mod.db = mock_db

    with TestClient(app) as client:
        yield client
