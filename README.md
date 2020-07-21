# Crucible
Crucible is an open-source python stress testing service for RESTful API's. The routes, actions and
responses used to test and verify an API are read in from the target API's OpenAPIv3 spec making
Crucible easily configurable, and reusable.

## Roadmap
 - [ ] Support stress testing GET actions.
 - [ ] Support validating response body schema. 
 - [ ] Support stress testing POST, PUT, PATCH, and DELETE actions.
 - [ ] Support OAUth2.0 protected API's. (Probably a Premium Feature)
 - [ ] Support Running in a distributed env. Premium feature?

## Next Steps
 - [] cli
 - [] architecture/design
 - [] tests

```
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
```

1. Yaml is passed in and converted to Objects by Yaml Parser
2. Objects are passed to test_generator which returns preconfigured locust test classes
3. locust test classes are passed to locust (Test Runner)
4. Results are gathered by crucible and returned to the user.


## Getting Started
### Sample App
I have provided a smaple API and OpenAPIv3 spec file for you to see how Crucible
works. This is the best starting place so you see a complete working instance of
Crucible before you start making changes. The following commands will start the
sample app and Crucible will start the load test.
```bash
python samples/main.py
python crucible.py -s sample/openapiv3.yml
```
