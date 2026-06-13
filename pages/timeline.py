import json
from datetime import datetime
from pathlib import Path

import flet as ft


SURFACE = "#07111F"
PANEL = "#0D1B2A"
PANEL_ALT = "#10263A"
TEXT = "#E5EEF8"
MUTED = "#8DA2B8"
BORDER = "#20364D"
ACCENT = "#48F838"

PHASES = [
    {
        "phase": "Foundation",
        "status": "Architecture",
        "icon": ft.Icons.ACCOUNT_TREE,
        "color": "#38BDF8",
        "tags": ["Repository", "Planning", "Structure"],
    },
    {
        "phase": "Interface",
        "status": "Navigation",
        "icon": ft.Icons.DASHBOARD_CUSTOMIZE,
        "color": "#8B5CF6",
        "tags": ["Routes", "Sidebar", "Caching"],
    },
    {
        "phase": "Content Systems",
        "status": "Modules",
        "icon": ft.Icons.SCHOOL,
        "color": "#10B981",
        "tags": ["MATLAB", "Contact", "Cards"],
    },
    {
        "phase": "Evidence Layer",
        "status": "Integration",
        "icon": ft.Icons.CLOUD_SYNC,
        "color": "#F59E0B",
        "tags": ["GitHub", "API", "Commits"],
    },
    {
        "phase": "Data Wiring",
        "status": "Dynamic",
        "icon": ft.Icons.DATA_OBJECT,
        "color": "#EC4899",
        "tags": ["JSON", "Blog", "Timeline"],
    },
    {
        "phase": "Release",
        "status": "Polish",
        "icon": ft.Icons.ROCKET_LAUNCH,
        "color": "#EF4444",
        "tags": ["Spacing", "Motion", "Deploy"],
    },
]

DEFAULT_EVENTS = [
    {
        "date": "Week 1",
        "title": "Repository setup and planning",
        "desc": "Initialized repo, created project plan and wireframes.",
    },
    {
        "date": "Week 2",
        "title": "Developed user interface",
        "desc": "Built main views, navigation and responsive layout.",
    },
    {
        "date": "Week 3",
        "title": "Testing and debugging",
        "desc": "Unit tests, bug fixes and polishing UI interactions.",
    },
    {
        "date": "Week 4",
        "title": "Final touches and deploy",
        "desc": "Performance tweaks and deployment preparations.",
    },
]


def box_border(color=BORDER, left_color=None, left_width=1):
    return ft.Border(
        left=ft.BorderSide(left_width, left_color or color),
        right=ft.BorderSide(1, color),
        top=ft.BorderSide(1, color),
        bottom=ft.BorderSide(1, color),
    )


def load_timeline_events():
    data_path = Path(__file__).parent.parent.joinpath("data", "timeline.json")
    try:
        with open(data_path, encoding="utf-8") as f:
            events = json.load(f)
        if isinstance(events, list):
            return events
    except Exception:
        pass

    return DEFAULT_EVENTS


def format_date(value):
    try:
        return datetime.strptime(value, "%Y-%m-%d").strftime("%d %b %Y")
    except (TypeError, ValueError):
        return value


def chip(label, color=ACCENT):
    return ft.Container(
        padding=ft.Padding(10, 5, 10, 5),
        bgcolor="#0B1726",
        border=box_border("#1D334B", color),
        border_radius=20,
        content=ft.Text(label, size=10, color=TEXT, no_wrap=True),
    )


def metric(label, value, icon, color="#38BDF8"):
    return ft.Container(
        expand=True,
        padding=14,
        bgcolor=PANEL,
        border=box_border(),
        border_radius=8,
        content=ft.Row(
            [
                ft.Icon(icon, color=color, size=22),
                ft.Column(
                    [
                        ft.Text(value, size=18, weight=ft.FontWeight.BOLD, color=TEXT),
                        ft.Text(label.upper(), size=10, color=MUTED),
                    ],
                    spacing=0,
                ),
            ],
            spacing=10,
        ),
    )


def event_card(event, index, total):
    phase = PHASES[index % len(PHASES)]
    color = phase["color"]

    return ft.Container(
        bgcolor=PANEL,
        border=box_border(left_color=color, left_width=4),
        border_radius=8,
        padding=18,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(
                            width=44,
                            height=44,
                            bgcolor="#07111F",
                            border=box_border(color),
                            border_radius=8,
                            alignment=ft.Alignment(0, 0),
                            content=ft.Icon(phase["icon"], size=24, color=color),
                        ),
                        ft.Column(
                            [
                                ft.Row(
                                    [
                                        ft.Text(phase["phase"].upper(), size=10, color=color, weight=ft.FontWeight.BOLD),
                                        ft.Text("|", size=10, color="#35516B"),
                                        ft.Text(f"Milestone {index + 1:02d}/{total:02d}", size=10, color=MUTED),
                                    ],
                                    spacing=7,
                                ),
                                ft.Text(event.get("title", "Untitled"), size=18, weight=ft.FontWeight.BOLD, color=TEXT),
                            ],
                            spacing=2,
                            expand=True,
                        ),
                        chip(phase["status"], color),
                    ],
                    spacing=14,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),
                ft.Text(event.get("desc", ""), size=13, color="#B8C7D8"),
                ft.Container(
                    bgcolor="#06101C",
                    border=box_border("#1E3A53"),
                    border_radius=8,
                    padding=12,
                    content=ft.Row(
                        [
                            ft.Icon(ft.Icons.EVENT_AVAILABLE, size=18, color=color),
                            ft.Column(
                                [
                                    ft.Text("TIMELINE DATE", size=10, color=color, weight=ft.FontWeight.BOLD),
                                    ft.Text(format_date(event.get("date", "")), size=13, color="#EAF2FF"),
                                ],
                                spacing=2,
                                expand=True,
                            ),
                            ft.Icon(ft.Icons.ARROW_FORWARD, size=18, color=color),
                        ],
                        spacing=10,
                    ),
                ),
                ft.Row([chip(tag, color) for tag in phase["tags"]], wrap=True, spacing=8, run_spacing=8),
            ],
            spacing=14,
        ),
    )


def timeline_item(event, index, total):
    phase = PHASES[index % len(PHASES)]
    color = phase["color"]
    is_last = index == total - 1

    marker = ft.Column(
        [
            ft.Container(
                width=34,
                height=34,
                bgcolor="#07111F",
                border=box_border(color),
                border_radius=17,
                alignment=ft.Alignment(0, 0),
                content=ft.Text(f"{index + 1}", size=12, color=color, weight=ft.FontWeight.BOLD),
            ),
            ft.Container(width=2, height=118 if not is_last else 0, bgcolor="#29435C"),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=8,
    )

    return ft.Row(
        [
            ft.Container(width=54, content=marker),
            ft.Container(expand=True, content=event_card(event, index, total)),
        ],
        spacing=8,
        vertical_alignment=ft.CrossAxisAlignment.START,
    )


def timeline_page():
    events = load_timeline_events()
    total = len(events)

    header = ft.Container(
        bgcolor="#081827",
        border_radius=8,
        border=box_border(),
        padding=22,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text("Project Timeline", size=32, weight=ft.FontWeight.BOLD, color=TEXT),
                                ft.Text(
                                    "A milestone map of architecture, interface work, integrations, and final delivery.",
                                    size=14,
                                    color=MUTED,
                                ),
                            ],
                            spacing=4,
                            expand=True,
                        ),
                        ft.Container(
                            padding=ft.Padding(12, 8, 12, 8),
                            bgcolor="#0B1726",
                            border_radius=20,
                            content=ft.Row(
                                [
                                    ft.Icon(ft.Icons.TIMELINE, size=16, color=ACCENT),
                                    ft.Text("BUILD LOG", size=11, color=TEXT, weight=ft.FontWeight.BOLD),
                                ],
                                spacing=6,
                            ),
                        ),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),
                ft.Row(
                    [
                        metric("Milestones", str(total), ft.Icons.FLAG, ACCENT),
                        metric("Phase Coverage", "6", ft.Icons.HUB, "#38BDF8"),
                        metric("Status", "Complete", ft.Icons.VERIFIED, "#10B981"),
                    ],
                    spacing=12,
                ),
            ],
            spacing=18,
        ),
    )

    return ft.Container(
        content=ft.Column(
            [
                header,
                ft.Row(
                    [
                        chip("Architecture", "#38BDF8"),
                        chip("UI Systems", "#8B5CF6"),
                        chip("Data Driven", "#EC4899"),
                        chip("Integration", "#F59E0B"),
                        chip("Deployment", "#EF4444"),
                    ],
                    wrap=True,
                    spacing=10,
                    run_spacing=10,
                ),
                ft.Container(
                    bgcolor="#081827",
                    border=box_border(),
                    border_radius=8,
                    padding=18,
                    content=ft.Column(
                        [timeline_item(event, index, total) for index, event in enumerate(events)],
                        spacing=14,
                    ),
                ),
            ],
            spacing=18,
        ),
        padding=20,
        bgcolor=SURFACE,
        expand=True,
    )
