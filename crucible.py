import locust
from locust.env import Environment
from yaml import load

import tests

# TODO workout how to run locust in distributed mode.


if __name__ == '__main__':
    #TODO parse the yaml file nows
    with open('sandbox/openapiv3.yml', 'r') as spec_f:
        raw_spec = spec_f.read()
        spec = load(raw_spec)

    # Sweet! I can dynamically set the host by attaching it to the class.
    # Won't do me good with test scenarios if I have to split up users into multiple
    # classes since they are pass by reference.
    tests.CrucibleUser.host = 'http://localhost:8000'
    env = Environment(
        # TODO figure out what user_classes expects here...but I think this is correct
        user_classes=[tests.CrucibleUser], # TODO there's a catch-22 here if Crucible is going to write these classes then call this. Actually it's not to bad since I get to define when this is called.
        events=locust.events,
        # host='http://localhost:8000'
    )

    runner = env.create_local_runner()
    env.events.init.fire(environment=env, runner=runner, web_ui=None)
    num_users = 1
    hatch_rate=10 # in seconds
    runner.start(num_users, hatch_rate)
    env.runner.greenlet.join()
    print("runner started")
