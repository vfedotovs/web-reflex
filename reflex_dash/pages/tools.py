import reflex as rx

from reflex_dash.navigation import navbar
from reflex_dash.template import template


@template
def tools() -> rx.Component:
    return rx.box(
            navbar(heading="API"),
            rx.box(
                rx.text("The Latvia Residential Apartment API", weight="bold"),
                    rx.text( "A collection of JSON API endpoints providing data on residential properties in Latvia."),
                    rx.text("Overview and list of Available API endpoints", weight="bold"),
                    rx.text("We are working hard to update this information shortly."),
                    rx.text("What data is included?", weight="bold"),
                    rx.text("Examples of data available via the API include property prices, sq meter prices, size, street location, floor location, house type and more."),
                    rx.text("Where does the property data come from?", weight="bold"),
                    rx.text("Data is sourced from publicly available clasified ads."),
                    rx.text("Which areas does the data cover?", weight="bold"),
                    rx.text("Currently data is avialble for Ogre city, but we are working hard to add more locations. "),
                    rx.text("How much does the data cost?", weight="bold"),
                    rx.text("API data is free of charge"),
                margin_top="calc(50px + 2em)",
                padding="4em",
            ),
            padding_left="250px",
    )
