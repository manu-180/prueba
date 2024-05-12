import reflex as rx
from prueba.pages.index import index
from prueba.pages.login import login
from prueba.pages.login_page import login_page
from prueba.api.api import hello, authenticate, hello_manu

app = rx.App()

app.add_page(index)
app.add_page(login, route="/login")
app.add_page(login_page, route="/login_page")


app.api.add_api_route("/hello/{user}", hello)
app.api.add_api_route("/login", authenticate)
app.api.add_api_route("/hello", hello_manu)