import base64
from pathlib import Path

import flet as ft


TEXT = "#E5EEF8"
MUTED = "#8DA2B8"
PANEL = "#07111F"
PANEL_2 = "#0D1B2A"
BORDER = "#20364D"
GREEN = "#48F838"
BLUE = "#38BDF8"
PURPLE = "#8B5CF6"
AMBER = "#F59E0B"
PINK = "#EC4899"


def home_page():
    profile_path = Path(__file__).parent.parent.joinpath("assets", "Pic2.JPEG")
    profile_image = ""
    if profile_path.exists():
        with open(profile_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
        profile_image = f"data:image/jpeg;base64,{encoded}"

    def outline_border(color=BORDER, left_color=None):
        return ft.Border(
            left=ft.BorderSide(3, left_color or color),
            right=ft.BorderSide(1, color),
            top=ft.BorderSide(1, color),
            bottom=ft.BorderSide(1, color),
        )

    def border_all(color):
        return ft.Border(
            left=ft.BorderSide(1, color),
            right=ft.BorderSide(1, color),
            top=ft.BorderSide(1, color),
            bottom=ft.BorderSide(1, color),
        )

    def chip(icon, label, color):
        return ft.Container(
            padding=ft.Padding(10, 6, 10, 6),
            border_radius=8,
            bgcolor="#0F1E2D",
            border=border_all(color),
            content=ft.Row(
                [
                    ft.Icon(icon, size=14, color=color),
                    ft.Text(label, size=11, color=TEXT, weight=ft.FontWeight.W_600),
                ],
                spacing=6,
                tight=True,
            ),
        )

    def metric(value, label, color, icon):
        return ft.Container(
            col={"sm": 12, "md": 6, "lg": 3},
            height=108,
            padding=14,
            border_radius=8,
            bgcolor=PANEL,
            border=outline_border(BORDER, color),
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Icon(icon, size=19, color=color),
                            ft.Text(label.upper(), size=10, color=MUTED, weight=ft.FontWeight.BOLD),
                        ],
                        spacing=8,
                    ),
                    ft.Text(value, size=29, color=TEXT, weight=ft.FontWeight.BOLD),
                ],
                spacing=9,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        )

    def action(label, icon, color, route=None, url=None):
        return ft.Container(
            height=44,
            padding=ft.Padding(14, 0, 14, 0),
            border_radius=8,
            bgcolor="#10263A",
            border=border_all(color),
            ink=True,
            on_click=(lambda e, target=route: e.page.go(target)) if route else None,
            url=url,
            content=ft.Row(
                [
                    ft.Icon(icon, size=18, color=color),
                    ft.Text(label, size=12, color=TEXT, weight=ft.FontWeight.BOLD),
                ],
                spacing=8,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        )

    def capability(title, desc, icon, color, route):
        return ft.Container(
            col={"sm": 12, "md": 6, "lg": 4},
            padding=18,
            border_radius=8,
            bgcolor=PANEL,
            border=outline_border(BORDER, color),
            ink=True,
            on_click=lambda e, target=route: e.page.go(target),
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Container(
                                width=42,
                                height=42,
                                border_radius=8,
                                bgcolor="#0F1E2D",
                                border=border_all(color),
                                alignment=ft.Alignment(0, 0),
                                content=ft.Icon(icon, size=22, color=color),
                            ),
                            ft.Icon(ft.Icons.ARROW_FORWARD, size=18, color=MUTED),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Text(title, size=16, color=TEXT, weight=ft.FontWeight.BOLD),
                    ft.Text(desc, size=12, color=MUTED),
                ],
                spacing=12,
            ),
        )

    def stack_row(title, value, color):
        return ft.Container(
            padding=ft.Padding(10, 8, 10, 8),
            border_radius=8,
            bgcolor="#07111F",
            border=border_all(BORDER),
            content=ft.Row(
                [
                    ft.Container(width=8, height=8, border_radius=4, bgcolor=color),
                    ft.Text(title, size=12, color=TEXT, expand=True),
                    ft.Text(value, size=12, color=color, weight=ft.FontWeight.BOLD),
                ],
                spacing=10,
            ),
        )

    hero = ft.Container(
        padding=24,
        border_radius=8,
        bgcolor=PANEL_2,
        border=outline_border(BORDER, GREEN),
        content=ft.ResponsiveRow(
            [
                ft.Container(
                    col={"sm": 12, "md": 5, "lg": 4},
                    content=ft.Stack(
                        [
                            ft.Container(
                                height=318,
                                border_radius=8,
                                bgcolor="#07111F",
                                border=outline_border(BORDER, BLUE),
                            ),
                            ft.Container(
                                left=14,
                                top=14,
                                right=14,
                                bottom=14,
                                border_radius=8,
                                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                                content=ft.Image(src=profile_image, fit=ft.BoxFit.COVER),
                            ),
                            ft.Container(
                                left=24,
                                bottom=24,
                                padding=ft.Padding(10, 7, 10, 7),
                                border_radius=8,
                                bgcolor="#07111F",
                                border=border_all(GREEN),
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.Icons.ENGINEERING, size=16, color=GREEN),
                                        ft.Text("MECH ENG + CODE", size=11, color=TEXT, weight=ft.FontWeight.BOLD),
                                    ],
                                    spacing=7,
                                    tight=True,
                                ),
                            ),
                        ]
                    ),
                ),
                ft.Container(
                    col={"sm": 12, "md": 7, "lg": 8},
                    padding=ft.Padding(20, 8, 8, 8),
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    chip(ft.Icons.VERIFIED, "Computer Programming I", GREEN),
                                    chip(ft.Icons.AUTO_GRAPH, "Evidence Driven", BLUE),
                                    chip(ft.Icons.SCHOOL, "MATLAB Ready", AMBER),
                                ],
                                wrap=True,
                                spacing=8,
                                run_spacing=8,
                            ),
                            ft.Text(
                                "Mechanical Engineering Portfolio",
                                size=44,
                                weight=ft.FontWeight.BOLD,
                                color=TEXT,
                            ),
                            ft.Text("Kambonde Lehabeam", size=24, color=GREEN, weight=ft.FontWeight.BOLD),
                            ft.Text(
                                "A technical workspace for engineering projects, programming progress, MATLAB learning, and visible GitHub evidence.",
                                size=15,
                                color=MUTED,
                            ),
                            ft.Container(
                                padding=16,
                                border_radius=8,
                                bgcolor="#07111F",
                                border=outline_border(BORDER, BLUE),
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.Icons.TERMINAL, size=24, color=BLUE),
                                        ft.Column(
                                            [
                                                ft.Text("Current Focus", size=12, color=MUTED, weight=ft.FontWeight.BOLD),
                                                ft.Text(
                                                    "Turning engineering coursework into documented software artifacts.",
                                                    size=14,
                                                    color=TEXT,
                                                    weight=ft.FontWeight.W_600,
                                                ),
                                            ],
                                            spacing=3,
                                            expand=True,
                                        ),
                                    ],
                                    spacing=12,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                            ),
                            ft.Row(
                                [
                                    action("View GitHub Evidence", ft.Icons.CODE, AMBER, "/github"),
                                    action("Read Blog", ft.Icons.ARTICLE, PINK, "/blog"),
                                    action("Contact", ft.Icons.EMAIL, GREEN, "/contact"),
                                ],
                                wrap=True,
                                spacing=10,
                                run_spacing=10,
                            ),
                        ],
                        spacing=14,
                    ),
                ),
            ],
            spacing=18,
            run_spacing=18,
        ),
    )

    metrics = ft.ResponsiveRow(
        [
            metric("7", "Portfolio Views", GREEN, ft.Icons.DASHBOARD),
            metric("6+", "MATLAB Courses", AMBER, ft.Icons.SCHOOL),
            metric("100+", "Commit Evidence", BLUE, ft.Icons.COMMIT),
            metric("2026", "Programming Track", PURPLE, ft.Icons.TIMELINE),
        ],
        spacing=12,
        run_spacing=12,
    )

    capability_grid = ft.ResponsiveRow(
        [
            capability(
                "GitHub Evidence",
                "Contribution history, repository notes, and traceable project work.",
                ft.Icons.CODE,
                AMBER,
                "/github",
            ),
            capability(
                "Technical Blog",
                "Short engineering explanations with programming and problem-solving context.",
                ft.Icons.ARTICLE,
                PINK,
                "/blog",
            ),
            capability(
                "MATLAB Hub",
                "Learning milestones, certificates, and computational engineering practice.",
                ft.Icons.SCHOOL,
                GREEN,
                "/matlab",
            ),
        ],
        spacing=12,
        run_spacing=12,
    )

    systems_panel = ft.ResponsiveRow(
        [
            ft.Container(
                col={"sm": 12, "lg": 7},
                padding=18,
                border_radius=8,
                bgcolor=PANEL_2,
                border=outline_border(BORDER, PURPLE),
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Icon(ft.Icons.HUB, size=22, color=PURPLE),
                                ft.Text("Engineering Delivery Map", size=18, color=TEXT, weight=ft.FontWeight.BOLD),
                            ],
                            spacing=10,
                        ),
                        ft.Row(
                            [
                                stack_row("Requirements", "Defined", GREEN),
                                stack_row("Implementation", "Active", BLUE),
                            ],
                            wrap=True,
                            spacing=10,
                            run_spacing=10,
                        ),
                        ft.Row(
                            [
                                stack_row("Documentation", "Evidence", AMBER),
                                stack_row("Reflection", "Blog", PINK),
                            ],
                            wrap=True,
                            spacing=10,
                            run_spacing=10,
                        ),
                    ],
                    spacing=12,
                ),
            ),
            ft.Container(
                col={"sm": 12, "lg": 5},
                padding=18,
                border_radius=8,
                bgcolor=PANEL,
                border=outline_border(BORDER, GREEN),
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Icon(ft.Icons.BOLT, size=22, color=GREEN),
                                ft.Text("Signal", size=18, color=TEXT, weight=ft.FontWeight.BOLD),
                            ],
                            spacing=10,
                        ),
                        ft.Text(
                            "This portfolio connects code, engineering reasoning, and learning records in one place.",
                            size=13,
                            color=MUTED,
                        ),
                        ft.Container(
                            height=8,
                            border_radius=4,
                            bgcolor=GREEN,
                        ),
                        ft.Row(
                            [
                                ft.Text("Traceable", size=11, color=GREEN, weight=ft.FontWeight.BOLD),
                                ft.Text("Practical", size=11, color=BLUE, weight=ft.FontWeight.BOLD),
                                ft.Text("Documented", size=11, color=AMBER, weight=ft.FontWeight.BOLD),
                            ],
                            wrap=True,
                            spacing=10,
                        ),
                    ],
                    spacing=12,
                ),
            ),
        ],
        spacing=12,
        run_spacing=12,
    )

    return ft.Column(
        [
            hero,
            metrics,
            capability_grid,
            systems_panel,
        ],
        spacing=16,
    )
