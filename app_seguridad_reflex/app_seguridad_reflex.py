import reflex as rx
from .componentes.navbar import navbar
from .componentes.seccion import seccion
def index()->rx.components:
  return rx.vstack(
    navbar(),
    seccion(),
    bg="#b4efff",
    height="100vh",
    align="center"
  )
app=rx.App()
app.add_page(index)

