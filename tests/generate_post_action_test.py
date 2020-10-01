import pytest
import inspect

from crucible import locust_factory


def test_generate_locust_for_post_action():
    actual = locust_factory.create_route_locusts('/health', ['post'])
    assert actual.__name__ == 'CrucibleHealthUser'
    assert inspect.isfunction(actual.wait_time)
    assert inspect.isfunction(actual.post_health)


def test_generate_locust_for_post_action_with_body():
    pass
