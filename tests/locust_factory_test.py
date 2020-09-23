import pytest
import inspect

from crucible import locust_factory


def test_create_route_locusts():
    actual = locust_factory.create_route_locusts('/health', ['get'])
    # Since the classes are dynamically generated the best way to assert on the
    # naming convention is to get the classname as a string otherwise I'd have
    # to recreate the dynamic class name in the test which I don't want to do
    # because that adds to much logic to the tests and my philosophy is tests
    # should be simple
    assert actual.__name__ == 'CrucibleHealthUser'
    # Good conversation on checking callable fields are callable
    # https://stackoverflow.com/questions/624926/how-do-i-detect-whether-a-python-variable-is-a-function
    assert inspect.isfunction(actual.wait_time)
    assert inspect.isfunction(actual.get_health)


def test_create_route_locust():
    actual = locust_factory.create_route_locusts('/health', ['get', 'post'])
    assert actual.__name__ == 'CrucibleHealthUser'
    assert inspect.isfunction(actual.wait_time)
    assert inspect.isfunction(actual.get_health)
    assert inspect.isfunction(actual.post_health)


def test_create_route_locust_with_post_body():
    """
    TODO Add test verifying a post action can be generated with a post test.
    """


1. Documentation
2. Follow up with James Grande
3. Add a note for Ken detailing everything I know about the scalar-qa tests and fakeoptics
