# test_app_with_fixtures.py
# --------------------------------------------------------------
# Demonstrates:
# - A pytest fixture that prepares a mock for external_api.get_user
# - Using the `mocker` fixture from pytest-mock
# - Tests stay clean: they just depend on fixtures
# --------------------------------------------------------------

# pip install pytest pytest-mock
import pytest
import app


@pytest.fixture
def mock_get_user(mocker):
    """
    Fixture that mocks external_api.get_user and returns a fake user.

    - mocker.patch(...) comes from pytest-mock plugin.
    - It replaces external_api.get_user with a Mock object for the duration
      of the test that uses this fixture.
    """
    fake_user = {"name": "Alice"}
    mock = mocker.patch("external_api.get_user", return_value=fake_user)
    return mock   # The test can still inspect this mock if needed


def test_get_user_name_uses_mocked_api(mock_get_user):
    # Because we requested mock_get_user fixture, external_api.get_user
    # is already patched to return {"name": "Alice"}.
    assert app.get_user_name(1) == "Alice"

    # We can also assert the mocked function was called as expected:
    mock_get_user.assert_called_once_with(1)
