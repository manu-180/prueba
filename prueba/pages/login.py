import reflex as rx
import requests as rq
import re



class AuthStatee(rx.State):
    # Esta función se llama cuando se envía el formulario
    def handle_submit(self, form_data: dict):
        username = form_data.get("username")
        password = form_data.get("password")
        # Verifica si el usuario y la contraseña son correctos
        if username == "ivanna.risaro@hotmail.com" and password == "123456789":
            # Redirecciona a otra página si los datos son correctos
            return rx.redirect("/")



class LoginState(rx.State):
    loader: bool = False
    username:str = "example@mail.com"
    password:str 
    error = False
    response: dict = {}
    
    @rx.background
    async def login_service(self, data:dict):
        async with self:
            self.loader = True
            self.error = False
            response = rq.post("https://pagina-web-production-4d43.up.railway.app/login", data = {"username": "ivanna.risaro@hotmail.com", "password": "123456789"}, headers={"Content-Type":"application/json"})
            print(response)
            if response.status_code == 405:
                self.response = response.json()
                self.loader = False
                return rx.redirect("/")
            else:
                self.loader = False
                self.error = True
    
    @rx.var
    def user_invalid(self)->bool:
        return not (re.match(r"[^@]+@[^@]+.[^@]+", self.username) and "example@mail.com" )
    
    @rx.var
    def user_empty(self) -> bool:
        return not self.username.strip()
    
    @rx.var
    def password_empty(self) -> bool:
        return not (self.password.strip())
    
    @rx.var
    def validate_fields(self) -> bool:
        return(
            self.user_empty
            or self.user_invalid
            or self.password_empty
        )



@rx.page(
    route="/login", 
    title= "login",
    description="Taller de ceramica")
def login() -> rx.Component:
    return rx.section(
        rx.center(
            rx.flex(
            rx.image(
            src="/logintaller.jpeg",
            width= "240px",
            border_radius="10%"
            ),
            rx.heading("Inicio de sesión"),
            rx.form.root(
                rx.flex(
                    field_from_component_general("Usuario", "Ingrese su usuario", "ingrese un correo valido", "username",
                                                 LoginState.set_username, LoginState.user_invalid),
                    field_form_component("Contraseña", "Ingrese su contraseña", "password",
                                         LoginState.set_password, "password"),
                    rx.form.submit(
                        rx.cond(
                            LoginState.loader,
                            rx.chakra.spinner(color="red", size= "xs"),
                            rx.button(
                                "iniciar sesión",
                                disabled=LoginState.validate_fields,
                                width = "250px"
                            ),
                        ),
                        as_child=True,
                    ),
                    direction="column",
                    justify="center",
                    align="center",
                    spacing="2"
                ),
                rx.cond(
                    LoginState.error,
                    rx.callout(
                        "Credenciales incorrectas",
                        icon="triangle_alert",
                        color_scheme="red",
                        role= "alert",
                        style={"margin_top": "10px"}
                    ),
                ),
                on_submit = AuthStatee.handle_submit,
                reset_on_submit=True,
                width="80%"
            )
        ,
        width="100%",
        direction="column",
        align="center",
        justify="center")
    ),
    style= style_section,
    justify="center",
    width= "100%")

def field_form_component(label:str, palaceholder: str, name_var:str,
                         on_change_function, type_field: str) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input.input(
                    placeholder=palaceholder,
                    on_change=on_change_function,
                    name=name_var,
                    type= type_field,
                    required=True,
                ),
                as_child=True,
            ),
            rx.form.message(
                "El campo no puede ser nulo",
                match="valueMissing",
                color="red",
            ),
            direction="column",
            spacing="2",
            align="stretch",
        ),
        name=name_var,
        width= "250px"
    )
    
def field_from_component_general(label:str, placeholder:str, massage_validated:str, name:str,
                                 on_change_function, show) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input.input(
                    placeholder=placeholder,
                    on_change=on_change_function,
                    name=name,
                    required=True
                ),
                as_child=True
            ),
            rx.form.message(
                massage_validated,
                name=name,
                match="valueMissing",
                force_match=show,
                color= "red"
            ),
            direction="column",
            spacing="2",
            align="stretch"
        ),
        name=name,
        width="250px"
    )
    
style_section = {
    "height": "90px",
    "width":"80%",
    "margin": "auto"
}
