import reflex as rx
from ..componentes.mi_button import mi_button_p
def seccion_mobile()->rx.Component:
  return rx.mobile_and_tablet(
    rx.heading(
      "Tu compañero para un entorno mas seguro",
      color="#a62f2f",
      size="8",
      align="center"
    ),
    rx.heading(
      " ",
      rx.text.em("Secure Path",color=""),
      color="#098c25",
      size="9",
      align="center"
    ),
    rx.hstack(
      rx.text(rx.text.em("Secure Path",color="#1faa6b",weight="bold")," (camino seguro) Una herramienta que te ayuda a sentirte mas  seguro en tu dia a dia. Te avisa sobre posibles peligros en tu zona, te ayuda a planificar rutas seguras y consejos para prevenir delitos.    ",size="5",color="#454545",text_align="center"),
    ),
    rx.vstack(
      rx.link(mi_button_p("user","Inicia Sesion"),href="/login"),
      margin_top="4em",
      align="center"
    ),
    width="90vw",
  )