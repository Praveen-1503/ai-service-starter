from pydantic import BaseModel


class Resume(BaseModel):
    name : str
    email : str
    skills : list[str]
    experience : int


resume = Resume(
    name = "Praveen V",
    email = "praveen.connects1@gmail.com",
    skills = ["FastAPI", "Python", "Java"],
    experience = "one"
)

print(resume)