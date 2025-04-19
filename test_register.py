from pytest import mark
from registerpage import RegisterPage
header="gender,fname,lname,email,password"
data=[
    ("male","ishan","a","ishan@gamil.com","ishan@123"),
    ("female","vanya","a","vanya@gmail.com","vanya@123")
]
@mark.parametrize(header,data)
def test_register(set_tear,gender,fname,lname,email,password):
    register=RegisterPage(set_tear)
    register.register(gender,fname,lname,email,password)