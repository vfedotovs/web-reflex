import reflex as rx

from reflex_dash.navigation import navbar
from reflex_dash.template import template


@template
def team() -> rx.Component:
    return rx.box(
            navbar(heading="Team"),
            rx.box(
            rx.text("Please redirect any feedback or sugestions",
                rx.link(" here.", href=" https://groups.google.com/g/propertydatalv"),
                ),
                margin_top="calc(50px + 2em)",
                padding="2em",
            ),
            padding_left="250px",
        )

