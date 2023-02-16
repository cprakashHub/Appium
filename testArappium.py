import pytest
from Createacct import welcreate

@pytest.mark.usefixtures("setup")
class Test_Arapp:

    def testwel(self):
        welc = welcreate(self.driver)
        welc.invalid()
        welc.welcome()
        welc.home()

