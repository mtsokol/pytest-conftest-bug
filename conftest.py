

def pytest_collection_modifyitems(config, items):

    test_id = items[0].nodeid
    option = config.getoption('--my-option')

    print(test_id, option)


def pytest_addoption(parser):
    parser.addoption(
        "--my-option",
        action="store"
    )
