"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
def encabezado()->rx.Component:
  return rx.hstack(
      rx.hstack(
        rx.icon(tag="cake"),
        rx.heading("DessertHouse...",size="6",weight="bold"),
        align_items="center"
      ),
      justify="between",
      align_items="center",
      padding="1em",
      width="100%",
      bg=rx.color("pink",10)
    )