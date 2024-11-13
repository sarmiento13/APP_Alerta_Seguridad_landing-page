import reflex as rx
from ..componentes.mi_button import mi_button_p
def seccion_mobile()->rx.Component:
  return rx.mobile_and_tablet(
    rx.heading(
      "Tu compañero para un entorno mas seguro",
      color="#eff9ff",
      size="8",
      align="center"
    ),
    rx.heading(
      " ",
      rx.text.em("Secure Path",color="#92dafe"),
      color="#eff9ff",
      size="9",
      align="center"
    ),
    rx.hstack(
      rx.text(rx.text.em("Secure Path",color="#92dafe",weight="bold")," (camino seguro) Una herramienta que te ayuda a sentirte mas  seguro en tu dia a dia. Te avisa sobre posibles peligros en tu zona, te ayuda a planificar rutas seguras y consejos para prevenir delitos.    ",size="5",color="#eff9ff",text_align="center"),
    ),
    rx.vstack(
      rx.link(mi_button_p("user","Inicia Sesion"),href="/login"),
      margin_top="4em",
      align="center"
    ),
    width="90vw",
  )