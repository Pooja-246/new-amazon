from loginpage import LoginPage
from pytest import mark
header="email,password"
data=[
        ("hello.world@company.com","Password123"),
        ("vanya@gmail.com","vanya@123")
]
@mark.parametrize(header,data)
def test_login(set_tear,email,password):
    login=LoginPage(set_tear)
    login.login(email,password)
    assert True==login.is_displayed_email(email)
