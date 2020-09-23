import click
import locust
from locust.env import Environment
from yaml import load

# TODO workout how to run locust in distributed mode.

@click.command()
@click.option('--spec-file', '-s', required=True, type=click.Path(exists=True), help="Path to OpenAPIv3 spec file")
def crucible(spec_file):
    with open(spec_file, 'r') as spec_f:
        raw_spec = spec_f.read()
        spec = load(raw_spec)

    print(spec)


if __name__ == '__main__':
    crucible()
