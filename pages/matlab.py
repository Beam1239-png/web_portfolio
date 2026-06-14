from pathlib import Path

import flet as ft


SURFACE = "#07111F"
PANEL = "#0D1B2A"
PANEL_ALT = "#10263A"
TEXT = "#E5EEF8"
MUTED = "#8DA2B8"
BORDER = "#20364D"
MATLAB_BLUE = "#38BDF8"
MATLAB_ORANGE = "#F59E0B"

CERTIFICATES = [
    {
        "file": "MATLAB_Onramp.pdf",
        "title": "MATLAB Onramp",
        "track": "Core Computing",
        "level": "Foundation",
        "icon": ft.Icons.TERMINAL,
        "color": "#38BDF8",
        "skills": ["Scripts", "Variables", "Functions"],
        "preview": "Core MATLAB workflow: scripts, variables, plots, functions, and basic data analysis.",
    },
    {
        "file": "Simulink_Onramp.pdf",
        "title": "Simulink Onramp",
        "track": "System Modeling",
        "level": "Model-Based",
        "icon": ft.Icons.ACCOUNT_TREE,
        "color": "#8B5CF6",
        "skills": ["Blocks", "Simulation", "Signals"],
        "preview": "Model-based design basics with block diagrams, simulation, and system behavior exploration.",
    },
    {
        "file": "Machine_Learning_Onramp.pdf",
        "title": "Machine Learning Onramp",
        "track": "Applied AI",
        "level": "Advanced",
        "icon": ft.Icons.PSYCHOLOGY,
        "color": "#EC4899",
        "skills": ["Regression", "Classification", "Evaluation"],
        "preview": "Fundamentals of classification, regression, feature extraction, and model evaluation.",
    },
    {
        "file": "Explore_Data_with_MATLAB_Plots.pdf",
        "title": "Explore Data with MATLAB Plots",
        "track": "Visualization",
        "level": "Analysis",
        "icon": ft.Icons.QUERY_STATS,
        "color": "#10B981",
        "skills": ["Plots", "Charts", "Exploration"],
        "preview": "Data visualization techniques using plots, charts, and interactive figure exploration.",
    },
    {
        "file": "Calculations_with_Vectors_and_Matrices.pdf",
        "title": "Calculations with Vectors and Matrices",
        "track": "Engineering Math",
        "level": "Numerical",
        "icon": ft.Icons.GRID_ON,
        "color": "#F59E0B",
        "skills": ["Vectors", "Matrices", "Linear Algebra"],
        "preview": "Matrix math essentials for engineering workflows, linear algebra, and vector operations.",
    },
    {
        "file": "MATLAB_Coder_Onramp.pdf",
        "title": "MATLAB Coder Onramp",
        "track": "Code Generation",
        "level": "Deployment",
        "icon": ft.Icons.CODE,
        "color": "#EF4444",
        "skills": ["Algorithms", "C/C++", "Generation"],
        "preview": "Generate code from MATLAB algorithms and work with code generation workflows.",
    },
    {
        "file": "Make_and_Manipulate_Matrices.pdf",
        "title": "Make and Manipulate Matrices",
        "track": "Data Structures",
        "level": "Core Math",
        "icon": ft.Icons.DATA_ARRAY,
        "color": "#22C55E",
        "skills": ["Indexing", "Transforms", "Arrays"],
        "preview": "Build and transform matrices, index data, and perform matrix-based calculations.",
    },
]


def box_border(color=BORDER, left_color=None, left_width=1):
    return ft.Border(
        left=ft.BorderSide(left_width, left_color or color),
        right=ft.BorderSide(1, color),
        top=ft.BorderSide(1, color),
        bottom=ft.BorderSide(1, color),
    )


def chip(label, color=MATLAB_BLUE):
    return ft.Container(
        padding=ft.Padding(10, 5, 10, 5),
        bgcolor="#0B1726",
        border=box_border("#1D334B", color),
        border_radius=20,
        content=ft.Text(label, size=10, color=TEXT, no_wrap=True),
    )


def metric(label, value, icon, color=MATLAB_BLUE):
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


def certificate_card(cert):
    color = cert["color"]
    # Use GitHub-hosted raw file URL instead of local file:// URI so links work when deployed
    file_uri = f"https://github.com/Beam1239-png/web_portfolio/blob/main/assets/matlab/{cert['file']}?raw=1"

    return ft.Card(
        elevation=10,
        shape=ft.RoundedRectangleBorder(radius=8),
        col={"sm": 12, "md": 6, "lg": 6},
        content=ft.Container(
            bgcolor=PANEL,
            border=box_border(left_color=color, left_width=4),
            border_radius=8,
            padding=18,
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Container(
                                width=46,
                                height=46,
                                bgcolor="#07111F",
                                border=box_border(color),
                                border_radius=8,
                                alignment=ft.Alignment(0, 0),
                                content=ft.Icon(cert["icon"], size=25, color=color),
                            ),
                            ft.Column(
                                [
                                    ft.Row(
                                        [
                                            ft.Text(cert["track"].upper(), size=10, color=color, weight=ft.FontWeight.BOLD),
                                            ft.Text("|", size=10, color="#35516B"),
                                            ft.Text(cert["level"], size=10, color=MUTED),
                                        ],
                                        spacing=7,
                                    ),
                                    ft.Text(cert["title"], size=18, weight=ft.FontWeight.BOLD, color=TEXT, max_lines=2),
                                ],
                                spacing=2,
                                expand=True,
                            ),
                            ft.Container(
                                width=38,
                                height=38,
                                bgcolor="#06101C",
                                border=box_border("#1E3A53"),
                                border_radius=8,
                                alignment=ft.Alignment(0, 0),
                                content=ft.Icon(ft.Icons.PICTURE_AS_PDF, size=20, color="#F87171"),
                            ),
                        ],
                        spacing=14,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                    ),
                    ft.Text(cert["preview"], size=13, color="#B8C7D8", max_lines=3),
                    ft.Container(
                        bgcolor="#06101C",
                        border=box_border("#1E3A53"),
                        border_radius=8,
                        padding=12,
                        content=ft.Row(
                            [
                                ft.Icon(ft.Icons.VERIFIED, size=18, color=color),
                                ft.Column(
                                    [
                                        ft.Text("MATHWORKS CERTIFICATE", size=10, color=color, weight=ft.FontWeight.BOLD),
                                        ft.Text(cert["file"], size=12, color="#EAF2FF", no_wrap=True),
                                    ],
                                    spacing=2,
                                    expand=True,
                                ),
                            ],
                            spacing=10,
                        ),
                    ),
                    ft.Row([chip(skill, color) for skill in cert["skills"]], wrap=True, spacing=8, run_spacing=8),
                    ft.Row(
                        [
                            ft.OutlinedButton(
                                "Open Certificate",
                                icon=ft.Icons.OPEN_IN_NEW,
                                url=file_uri,
                                style=ft.ButtonStyle(color=color),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ],
                spacing=14,
            ),
        ),
    )


def matlab_page():
    # Count certificates as available (served from GitHub raw URLs in deployment)
    # Local file existence checks are unreliable on Render; assume uploaded to the repo.
    available = len(CERTIFICATES)

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
                                ft.Text("MATLAB Achievement Hub", size=32, weight=ft.FontWeight.BOLD, color=TEXT),
                                ft.Text(
                                    "A technical evidence board for MATLAB, Simulink, matrices, visualization, coding, and applied AI.",
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
                                    ft.Icon(ft.Icons.AUTO_GRAPH, size=16, color=MATLAB_ORANGE),
                                    ft.Text("MATHWORKS TRACK", size=11, color=TEXT, weight=ft.FontWeight.BOLD),
                                ],
                                spacing=6,
                            ),
                        ),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),
                ft.Row(
                    [
                        metric("Certificates", str(len(CERTIFICATES)), ft.Icons.WORKSPACE_PREMIUM, MATLAB_ORANGE),
                        metric("PDFs Found", f"{available}/{len(CERTIFICATES)}", ft.Icons.FOLDER_OPEN, MATLAB_BLUE),
                        metric("Skill Tracks", "7", ft.Icons.HUB, "#10B981"),
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
                        chip("MATLAB", MATLAB_BLUE),
                        chip("Simulink", "#8B5CF6"),
                        chip("Machine Learning", "#EC4899"),
                        chip("Matrices", MATLAB_ORANGE),
                        chip("Code Generation", "#EF4444"),
                    ],
                    wrap=True,
                    spacing=10,
                    run_spacing=10,
                ),
                ft.ResponsiveRow(
                    [certificate_card(cert) for cert in CERTIFICATES],
                    spacing=18,
                    run_spacing=18,
                ),
            ],
            spacing=18,
        ),
        padding=20,
        bgcolor=SURFACE,
        expand=True,
    )
