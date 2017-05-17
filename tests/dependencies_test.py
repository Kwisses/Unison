"""DependenciesTest tests the project's necessary dependency imports.

If the test fails, one of the dependencies will have failed to import.
A printout to the console will tell what dependency failed to import.
If this occurs, make sure that your project's environment has the
necessary package(s) installed on it. 

If the above instructions do not solve the issue, please notify the
project's author(s) and contributors of the issue. For more information, check 
out the project's GitHub repository at https://github.com/Kwistech/Unison
"""

# Used to get all project dependencies
from classes.settings import Settings


class Dependencies(object):

    def __init__(self):
        """Initialize Settings object and set to get dependencies."""
        self.settings_obj = Settings(cd="..")
        self.settings = self.settings_obj.set()

        # Get project dependencies (split necessary)
        self.deps = self.settings["dependencies"].split(", ")

    @staticmethod
    def display_start():
        """Print test instructions to the console."""
        print("Dependencies Test\n")
        print("This test will try to import all the necessary\n"
              "project dependencies.\n")

    @staticmethod
    def display_end(result):
        """Additional console end-of-test messages.
        
        Args:
            result (str): Result of test.
        """
        print("\nDependencies test {}!".format(result))

    def test(self):
        """Try to import all dependencies.
        
        Returns:
            bool: True if all dependencies were imported, 
                  False otherwise.
        
        Raises:
            Exception: If dependency import fails.
        """
        for dep in self.deps:
            try:
                __import__(dep)
            except Exception as e:
                print(dep, "failed with error code:", e)
                return False
            else:
                print("Successfully imported:", dep)
        return True

    def run(self):
        """Run DependenciesTest."""
        # Display test instructions
        self.display_start()

        # Run import test
        if self.test():
            result = "passed"
        else:
            result = "failed"

        # Display test result
        self.display_end(result)

if __name__ == "__main__":
    dep_test = Dependencies()
    dep_test.run()
