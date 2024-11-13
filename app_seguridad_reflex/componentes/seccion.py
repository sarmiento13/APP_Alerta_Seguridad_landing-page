import reflex as rx
from ..componentes.seccion_pc import seccion_pc
from ..componentes.seccion_mobile import seccion_mobile
def seccion()->rx.Component:
  return rx.section(
    seccion_pc(),
    seccion_mobile(),
  )