from pydantic import BaseModel, EmailStr, constr


class SignupSchema(BaseModel):
    name: str
    email: EmailStr  # Required string that must be a valid email address
    password: constr(
        min_length=8
    )  # Password with a minimum length of 6 characters


class LoginSchema(BaseModel):
    email: EmailStr  # Required string that must be a valid email address
    password: str

class ChangePasswordSchema(BaseModel):
    current_password: constr(min_length=6)
    new_password: constr(
        min_length=6
    )  # Password with a minimum length of 6 characters
