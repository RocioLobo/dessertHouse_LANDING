"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

def seccion()->rx.Component:
  return rx.vstack(
      rx.heading(
        rx.text.span("DessertHouse",color=rx.color("sky",10)),
        " podras hacer postres con ingredientes a la mano",size="9"),

      rx.container(
        rx.hstack(
          rx.text("prepara postres con ingedientes a la mano y sin horno visitandonos a nuestra app,donte te facilitara opciones de tipos de postres , con un acceso facil,visualizar diferentes tipos de recetas.¡no hay nada mas que ser la unica repostera!",
            margin_top="4em",
            weight="bold",
            size="5"
            ),
          rx.image(src="https://png.pngtree.com/png-clipart/20190516/original/pngtree-cartoon-donut-dessert-cake-png-image_3594490.jpg",
          alt="mi imagen",
          width="200px",
          margin_top="2em",
          align_items="right"
          ),
          spacing="3"
        ),
          rx.link(
            rx.button("Registrate",margin_top="6em",size="4"),
            href="https://forms.gle/w6rJHTaSkFPNKsCd6",
            is_external=False),
            margin_top="4em",
            position="relative",
      ),
      rx.image(
        src="https://i.pinimg.com/originals/ac/df/a4/acdfa4792e7ea15b2bcafb07d9167160.png",
        width="300px",
        position="absolute",
        bottom="0",
        left="0"
      ),
      padding_top="4em",
      align="center",
      text_align="center",
      height="676px",
      background=rx.color("purple",6)
  )