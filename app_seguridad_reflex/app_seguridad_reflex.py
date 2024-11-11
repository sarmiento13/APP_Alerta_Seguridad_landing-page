import reflex as rx

def index()->rx.components:
    return rx.container(
        rx.hstack(
            rx.heading("APP INSTALL",margin_top="6px"),
            rx.spacer(),
            rx.hstack(
                rx.link("inicio",href="/#"),
                rx.link("sobre nosostros",href="/#"),
                rx.link("contacto",href="/#", weight="bold"
                        color="white"),
                margin_top="2px"
            ),
            bg="red"
            height="50px"
        )
 )
app=rx.App()
app. add_page(index,title=".:ejercicios:.")
