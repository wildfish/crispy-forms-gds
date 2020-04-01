from tests.utils import configure_django


def pytest_sessionstart(session):
    configure_django()
