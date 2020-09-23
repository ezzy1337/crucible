import click
import locust
from locust.env import Environment
from yaml import load

import locust_factory
# TODO workout how to run locust in distributed mode.

@click.command()
@click.option('--spec-file', '-s', required=True, type=click.Path(exists=True), help="Path to OpenAPIv3 spec file")
def crucible(spec_file):
    with open(spec_file, 'r') as spec_f:
        raw_spec = spec_f.read()
        spec = load(raw_spec)

    test_classes = []
    for route in spec['paths']:
        actions = [a for a in spec['paths'][route]]
        test_classes.append(locust_factory.create_route_locusts(route, actions[0]))

    env = Environment(
        # TODO figure out what user_classes expects here...but I think this is correct
        user_classes=test_classes,
        events=locust.events,
        host='http://localhost:8000'
    )

    runner = env.create_local_runner()
    env.events.init.fire(environment=env, runner=runner, web_ui=None)
    num_users = 1
    hatch_rate=10 # in seconds
    runner.start(num_users, hatch_rate)
    env.runner.greenlet.join()
    print("runner started")


if __name__ == '__main__':
    crucible()
