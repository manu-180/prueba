import reflex as rx

class AuthState(rx.State):
    # Esta función se llama cuando se envía el formulario
    async def handle_submit(self, form_data: dict):
        username = form_data.get("username")
        password = form_data.get("password")
        print(username)
        print(password)
        print(form_data)
        # Verifica si el usuario y la contraseña son correctos
        if username == "ivanna.risaro@hotmail.com" and password == "123456789":
            # Redirecciona a otra página si los datos son correctos
            return rx.redirect("/login")


@rx.page(
    route="/login_page", 
    title= "login",
    description="Taller de ceramica")
def login_page():
    return rx.form.root(
        rx.form.field(
            rx.form.label("usuario"),
            rx.input(name="username"),  # Campo para el nombre de usuario
            name="username",
            
        ),
        rx.form.field(
            rx.form.label("contraseña"),
            rx.input(name="password", type="password"),  # Campo para la contraseña
            name="password",
        ),
        rx.button("Iniciar sesión", type="submit"),
        on_submit=AuthState.handle_submit,  # Establece el manejador para el evento de envío
    )