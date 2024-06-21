"""Mock data to populate the dashboard charts and tables."""

import reflex as rx
from reflex_dash.graphs import Area, Line

stat_card_data = [
    [
        "Today's Listed ads in Ogre",
        "44",
        "+10%",
    ],
    [
        "Total delisted ads since Y22",
        "1,400",
        "+5%",
    ],
    [
        "City Postal Code",
        "5001",
        "+0%",
    ]
]

line_chart_data = [
    {"name": "JUN09", "New": 1, "Removed": 2, "amt": 2400},
    {"name": "JUN10", "New": 5, "Removed": 1, "amt": 2210},
    {"name": "JUN11", "New": 2, "Removed": 0, "amt": 2290},
    {"name": "JUN12", "New": 2, "Removed": 3, "amt": 2000},
    {"name": "JUN13", "New": 2, "Removed": 0, "amt": 2181},
    {"name": "JUN14", "New": 3, "Removed": 3, "amt": 2500},
    {"name": "JUN15", "New": 3, "Removed": 1, "amt": 2500},
    {"name": "JUN16", "New": 4, "Removed": 2, "amt": 2100},
]


lines = [
    Line(data_key="New", stroke="#8884d8"),
    Line(data_key="Removed", stroke="var(--accent-8)"),
]


pie_chart_data = [
    {"name": "Single room", "value": 9, "fill": "var(--red-7)"},
    {"name": "Two rooms", "value": 20, "fill": "var(--green-7)"},
    {"name": "Three rooms", "value": 7, "fill": "var(--purple-7)"},
    {"name": "Four rooms", "value": 4, "fill": "var(--blue-7)"},
]

area_chart_data = line_chart_data

areas = [
    Area(data_key="New listed ads", stroke="#8884d8", fill="#8884d8"),
    Area(data_key="Removed ads", stroke="var(--accent-8)", fill="var(--accent-8)"),
]


tabular_data = [
    ["ID", "Rooms", "Street", "Price", "SQM"],
    ["1", "2", "Malkalnes 5", "45000", "44"],
    ["2", "1", "Skolas 13", "37000", "36"],
    ["3", "2", "Malkalnes 21", "55000", "48"],
    ["4", "4", "Tinuzu 3", "78000", "70"],
    ["5", "1", "Vidzemes 11", "3900", "40"],
]
