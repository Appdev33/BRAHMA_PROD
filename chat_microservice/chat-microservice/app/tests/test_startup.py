import pytest
from unittest.mock import AsyncMock, patch
from app.main import app, settings

@pytest.fixture
def mock_mongodb():
    with patch('motor.motor_asyncio.AsyncIOMotorClient', new_callable=AsyncMock) as mock:
        yield mock

@pytest.mark.asyncio
async def test_startup_db_client(mock_mongodb):
    # Setup the mock to return a specific value when called
    mock_mongodb.return_value.__aenter__.return_value.list_collection_names.return_value = ['test_collection']
    
    # Simulate the startup event
    await app.router.startup()

    # Verify the MongoDB client was instantiated with the correct URI
    mock_mongodb.assert_called_once_with(settings.mongodb_uri.get_secret_value())
    
    # Verify that the correct database is set
    assert app.mongodb == mock_mongodb.return_value.__aenter__.return_value

    # Optionally, you can check for logs or other behaviors
    # For example, use a logging handler to capture log outputs if necessary


# import pytest
# from unittest.mock import AsyncMock, patch
# from fastapi import FastAPI
# from app.main import app, settings

# @pytest.fixture
# def mock_mongodb():
#     with patch('motor.motor_asyncio.AsyncIOMotorClient', new_callable=AsyncMock) as mock:
#         yield mock

# @pytest.mark.asyncio
# async def test_startup_db_client(mock_mongodb):
#     mock_mongodb.return_value.__aenter__.return_value.list_collection_names.return_value = ['test_collection']
    
#     # Run the startup event
#     await app.router.startup()

#     # Check if the MongoDB client was called
#     mock_mongodb.assert_called_once_with(settings.mongodb_uri.get_secret_value())
    
#     # Check if the correct database was set
#     assert app.mongodb == mock_mongodb.return_value.__aenter__.return_value

#     # Check the log output (optional)
#     # You can use a logging handler to capture logs if needed
