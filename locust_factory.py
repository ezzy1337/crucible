import types

from locust import (
    HttpUser,
    task,
    between
)

def __create_test_action(route, action):
    def test_get_action(self):
        self.client.get(route)

    if action == 'get': # This should be an Enum
        return task(test_get_action)


def create_route_locusts(route, actions):
    """
    Creates a Locust Test Class for all actions available for a specific route.
    :param route str: The route to generate tests for
    :param action str: The HTTP Action to use for the test
    TODO Make action a list of actions.
    """
    # This is defined before the bootstrap_class function just for organization.
    route_name = route[1:].capitalize()

    def bootstrap_class(cls):
        """
        Callback for bootstrapping the new class definition.
        :param self: A reference to the Class namespace as you would expect cls to be
        """
        cls['wait_time'] = between(1,2) #TODO make these dynamic
        for action in actions:
            cls[f'{action}_{route_name.lower()}'] = __create_test_action(route, action)

    test_class = types.new_class(
        f'Crucible{route_name}User', # name of the new Class
        (HttpUser,), # Tuple of classes the new one should inherit from
        None,
        bootstrap_class # Callback that initializes the class namespace
    )
    return test_class