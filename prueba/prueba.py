import reflex as rx
from prueba.pages.index import index
from prueba.pages.login import login
from prueba.api.api import hello, login_auth

app = rx.App()

app.add_page(index)
app.add_page(login, route="/login")


app.api.add_api_route("/hello/{user}", hello)
app.api.add_api_route("/login", login_auth)
#app.api.add_api_route("/hello", hello)