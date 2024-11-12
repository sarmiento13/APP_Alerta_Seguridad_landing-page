import reflex as rx
from .componentes.navbar import navbar
from .componentes.seccion import seccion
def index()->rx.componentes:
  return rx.vstack(
    navbar(),
    seccion(),
    bg="#1d5cb0",
    height="100vh",
    align="center"
  )
app=rx.App()
app.add_page(index)

