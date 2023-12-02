import pytest

# pytest_plugins = ["tests"]

@pytest.fixture(scope="session")
def oversize_objects_all_five():
    return {
        'name0': 99999999999,
        'name1': 99999999999,
        'name2': 99999999999,
        'name3': 99999999999,
        'name4': 99999999999,
    }


@pytest.fixture(scope="session")
def oversize_objects_two_out_five():
    return {
        'name0': 1,
        'name1': 99999999999,
        'name2': 2,
        'name3': 99999999999,
        'name4': 4,
    }
