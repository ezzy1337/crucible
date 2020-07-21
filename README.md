# Crucible
Crucible is an open-source stress testing service for RESTful API's written in Python. The routes, actions and
responses used to test and verify an API are read in from the target API's OpenAPI v3 spec making Crucible easily
configurable, and reusable.

## Roadmap
 - [ ] Support stress testing GET actions.
 - [ ] Support validating response body schema. 
 - [ ] Support stress testing POST, PUT, PATCH, and DELETE actions.
 - [ ] Support OAUth2.0 protected API's. (Probably a Premium Feature)
 - [ ] Support Running in a distributed env. Premium feature?

## Next Steps
 - [x] cli
 - [] architecture/design
 - [] tests


          +--------------+                       
yaml  --> |              |
          |  yaml_parser |
          |              |
          +--------------+
                 |
           Object Notation   
                 |
                 V
         +----------------+      +-----------------+
         |                | ---> |  test_generator |
         |    Crucible    |      +-----------------+
<-stdout-|                |               |
         |                |<--------------+
         +----------------+
             |       ^
           tests    results
             V       |
         +----------------+
         |   test_runner  |
         +----------------+

1. Yaml is passed in and converted to Objects by Yaml Parser
2. Objects are passed to test_generator which returns preconfigured locust test classes
3. locust test classes are passed to locust (Test Runner)
4. Results are gathered by crucible and returned to the user.


## Getting Started
### Sample App
1. python sandbox/app/main.py # TODO make an actual example/sample folder
2. python crucible.py -s sandbox/openapiv3.yml


## Contributing
1. Setup virtual environment
2. Run unit tests

## Unit Tests
pytest test
