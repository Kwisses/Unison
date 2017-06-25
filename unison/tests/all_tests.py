"""AllTests runs all developer-generated project tests."""

from unison.tests.dependencies_test import Dependencies
# Developer-generated tests
from unison.tests.input_test import InputTest
from unison.tests.output_test import OutputTest


class AllTests:

    def __init__(self):
        """Initialize test objects."""
        # Test objects
        dep_test = Dependencies()
        input_test = InputTest()
        output_test = OutputTest()

        # Tests iterator
        self.tests = [dep_test, input_test, output_test]

    def run(self):
        """Run all available tests."""
        for test in self.tests:
            print("\n***\n")
            test.run()

if __name__ == "__main__":
    all_tests = AllTests()
    all_tests.run()
