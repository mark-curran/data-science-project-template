# Unit Tests

This page explains how to run unit tests.

## Unit tests using pytest

By default, the template installs [pytest](https://docs.pytest.org/en/7.1.x/index.html) into the local environment. This allows one to run any non-resource intensive unit tests on the local host.

To run the example unit tests, run this code from the root folder of repository.

`pytest -v tests/test_regurgitator.py`

## Integration Testing

Integration testing is beyond the scope of the Data Science Template, though it is recommended to use a separate environment from dev or prod to run these tests, i.e., a staging environment.
