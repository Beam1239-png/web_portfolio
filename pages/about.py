import flet as ft


TEXT = "#E5EEF8"
MUTED = "#8DA2B8"
SURFACE = "#07111F"
PANEL = "#0D1B2A"
BORDER = "#20364D"
GREEN = "#48F838"
BLUE = "#38BDF8"
VIOLET = "#8B5CF6"
AMBER = "#F59E0B"
ROSE = "#EC4899"
RED = "#EF4444"


def about_page():
    skill_groups = [
        {
            "title": "Programming",
            "icon": ft.Icons.CODE,
            "color": BLUE,
            "items": ["Python", "JavaScript", "C++", "SQL", "Git"],
        },
        {
            "title": "Engineering",
            "icon": ft.Icons.ENGINEERING,
            "color": VIOLET,
            "items": ["MATLAB", "CAD Design", "Control Systems", "Simulink", "Circuit Analysis"],
        },
        {
            "title": "Web Systems",
            "icon": ft.Icons.PUBLIC,
            "color": ROSE,
            "items": ["React", "Node.js", "REST APIs", "Flet", "HTML/CSS"],
        },
        {
            "title": "Platforms",
            "icon": ft.Icons.SETTINGS,
            "color": AMBER,
            "items": ["Docker", "Linux", "AWS", "GitHub", "VS Code"],
        },
    ]

    capabilities = [
        {"label": "Engineering Thinking", "value": 92, "color": GREEN},
        {"label": "Software Build Skill", "value": 86, "color": BLUE},
        {"label": "Documentation Evidence", "value": 88, "color": AMBER},
        {"label": "Learning Velocity", "value": 94, "color": ROSE},
    ]

    milestones = [
        {
            "label": "Mechanical Engineering Student",
            "detail": "Using programming to strengthen analysis, modeling, and technical communication.",
            "icon": ft.Icons.SCHOOL,
            "color": GREEN,
        },
        {
            "label": "MATLAB Learning Track",
            "detail": "Completed 6+ MathWorks learning modules across MATLAB, Simulink, data, and code generation.",
            "icon": ft.Icons.FUNCTIONS,
            "color": AMBER,
        },
        {
            "label": "Project Contributor",
            "detail": "Built visible portfolio pages, repository evidence, navigation flows, and technical blog content.",
            "icon": ft.Icons.ACCOUNT_TREE,
            "color": BLUE,
        },
    ]

    def box_border(color=BORDER, left_color=None, left_width=1):
        return ft.Border(
            left=ft.BorderSide(left_width, left_color or color),
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

    def micro_chip(label, color):
        return ft.Container(
            padding=ft.Padding(9, 5, 9, 5),
            border_radius=6,
            bgcolor="#0F1E2D",
            border=border_all(color),
            content=ft.Text(label, size=10, color=TEXT, weight=ft.FontWeight.W_600),
        )

    def identity_stat(value, label, color):
        return ft.Container(
            expand=True,
            padding=12,
            border_radius=8,
            bgcolor=SURFACE,
            border=box_border(BORDER, color, 3),
            content=ft.Column(
                [
                    ft.Text(value, size=22, color=color, weight=ft.FontWeight.BOLD),
                    ft.Text(label.upper(), size=10, color=MUTED, weight=ft.FontWeight.BOLD),
                ],
                spacing=2,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
        )

    def capability_meter(item):
        return ft.Container(
            padding=12,
            border_radius=8,
            bgcolor=SURFACE,
            border=box_border("#1D334B", item["color"], 3),
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text(item["label"], size=12, color=TEXT, weight=ft.FontWeight.BOLD, expand=True),
                            ft.Text(f'{item["value"]}%', size=12, color=item["color"], weight=ft.FontWeight.BOLD),
                        ],
                        spacing=10,
                    ),
                    ft.Stack(
                        [
                            ft.Container(height=8, border_radius=4, bgcolor="#13283D"),
                            ft.Container(
                                width=max(40, item["value"] * 3),
                                height=8,
                                border_radius=4,
                                bgcolor=item["color"],
                            ),
                        ]
                    ),
                ],
                spacing=9,
            ),
        )

    def skill_cluster(group):
        return ft.Container(
            col={"sm": 12, "md": 6},
            padding=16,
            border_radius=8,
            bgcolor=PANEL,
            border=box_border(BORDER, group["color"], 3),
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Container(
                                width=40,
                                height=40,
                                border_radius=8,
                                bgcolor="#0F1E2D",
                                border=border_all(group["color"]),
                                alignment=ft.Alignment(0, 0),
                                content=ft.Icon(group["icon"], size=21, color=group["color"]),
                            ),
                            ft.Column(
                                [
                                    ft.Text(group["title"], size=15, color=TEXT, weight=ft.FontWeight.BOLD),
                                    ft.Text(f'{len(group["items"])} active tools', size=11, color=MUTED),
                                ],
                                spacing=1,
                                expand=True,
                            ),
                        ],
                        spacing=11,
                    ),
                    ft.Row(
                        [micro_chip(item, group["color"]) for item in group["items"]],
                        wrap=True,
                        spacing=8,
                        run_spacing=8,
                    ),
                ],
                spacing=13,
            ),
        )

    def milestone_row(index, item):
        return ft.Container(
            padding=14,
            border_radius=8,
            bgcolor=SURFACE,
            border=box_border(BORDER, item["color"], 3),
            content=ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text(f"0{index}", size=12, color=item["color"], weight=ft.FontWeight.BOLD),
                            ft.Container(width=2, height=44, bgcolor=item["color"], border_radius=1),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=8,
                    ),
                    ft.Container(
                        width=44,
                        height=44,
                        border_radius=8,
                        bgcolor="#0F1E2D",
                        border=border_all(item["color"]),
                        alignment=ft.Alignment(0, 0),
                        content=ft.Icon(item["icon"], size=22, color=item["color"]),
                    ),
                    ft.Column(
                        [
                            ft.Text(item["label"], size=14, color=TEXT, weight=ft.FontWeight.BOLD),
                            ft.Text(item["detail"], size=12, color=MUTED),
                        ],
                        spacing=4,
                        expand=True,
                    ),
                ],
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
        )

    portrait = ft.Container(
        col={"sm": 12, "lg": 4},
        padding=20,
        border_radius=8,
        bgcolor=PANEL,
        border=box_border(BORDER, GREEN, 4),
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(
                            width=58,
                            height=58,
                            border_radius=8,
                            bgcolor=SURFACE,
                            border=border_all(GREEN),
                            alignment=ft.Alignment(0, 0),
                            content=ft.Icon(ft.Icons.PERSON_PIN, size=32, color=GREEN),
                        ),
                        ft.Column(
                            [
                                ft.Text("Kambonde Lehabeam", size=20, color=TEXT, weight=ft.FontWeight.BOLD),
                                ft.Text("Mechanical Engineering Student", size=12, color=MUTED),
                            ],
                            spacing=2,
                            expand=True,
                        ),
                    ],
                    spacing=12,
                ),
                ft.Container(
                    padding=12,
                    border_radius=8,
                    bgcolor=SURFACE,
                    border=box_border("#1D334B", BLUE, 3),
                    content=ft.Text(
                        "I connect mechanical engineering fundamentals with software practice, using code to model, explain, document, and improve technical work.",
                        size=13,
                        color=TEXT,
                    ),
                ),
                ft.Row(
                    [
                        identity_stat("6+", "MATLAB courses", AMBER),
                        identity_stat("100+", "commit evidence", BLUE),
                    ],
                    spacing=10,
                ),
                ft.Row(
                    [
                        identity_stat("2026", "programming track", GREEN),
                        identity_stat("4", "skill domains", ROSE),
                    ],
                    spacing=10,
                ),
            ],
            spacing=14,
        ),
    )

    dossier = ft.Container(
        col={"sm": 12, "lg": 8},
        padding=22,
        border_radius=8,
        bgcolor="#081524",
        border=box_border(BORDER, BLUE, 4),
        content=ft.Column(
            [
                ft.Row(
                    [
                        micro_chip("ABOUT DOSSIER", GREEN),
                        micro_chip("ENGINEERING + SOFTWARE", BLUE),
                        micro_chip("EVIDENCE BASED", AMBER),
                    ],
                    wrap=True,
                    spacing=8,
                    run_spacing=8,
                ),
                ft.Text("Technical Profile", size=38, color=TEXT, weight=ft.FontWeight.BOLD),
                ft.Text(
                    "A compact view of the thinking, tools, and learning systems behind this portfolio.",
                    size=14,
                    color=MUTED,
                ),
                ft.Container(
                    padding=16,
                    border_radius=8,
                    bgcolor=PANEL,
                    border=box_border(BORDER, VIOLET, 3),
                    content=ft.Column(
                        [
                            ft.Text("Operating Style", size=16, color=TEXT, weight=ft.FontWeight.BOLD),
                            ft.Text(
                                "I approach projects like engineering systems: define the problem, build a working model, test the evidence, then explain the result clearly enough that someone else can inspect it.",
                                size=13,
                                color="#B8C7D8",
                            ),
                        ],
                        spacing=8,
                    ),
                ),
                ft.ResponsiveRow(
                    [
                        ft.Container(col={"sm": 12, "md": 6}, content=capability_meter(capabilities[0])),
                        ft.Container(col={"sm": 12, "md": 6}, content=capability_meter(capabilities[1])),
                        ft.Container(col={"sm": 12, "md": 6}, content=capability_meter(capabilities[2])),
                        ft.Container(col={"sm": 12, "md": 6}, content=capability_meter(capabilities[3])),
                    ],
                    spacing=10,
                    run_spacing=10,
                ),
            ],
            spacing=14,
        ),
    )

    skill_matrix = ft.Container(
        padding=18,
        border_radius=8,
        bgcolor=SURFACE,
        border=box_border(BORDER, AMBER, 4),
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Icon(ft.Icons.DATA_OBJECT, size=23, color=AMBER),
                        ft.Text("Capability Matrix", size=20, color=TEXT, weight=ft.FontWeight.BOLD),
                    ],
                    spacing=10,
                ),
                ft.ResponsiveRow([skill_cluster(group) for group in skill_groups], spacing=12, run_spacing=12),
            ],
            spacing=14,
        ),
    )

    timeline = ft.Container(
        padding=18,
        border_radius=8,
        bgcolor=PANEL,
        border=box_border(BORDER, ROSE, 4),
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Icon(ft.Icons.ROUTE, size=23, color=ROSE),
                        ft.Text("Learning Path", size=20, color=TEXT, weight=ft.FontWeight.BOLD),
                    ],
                    spacing=10,
                ),
                ft.Column(
                    [milestone_row(index + 1, item) for index, item in enumerate(milestones)],
                    spacing=10,
                ),
            ],
            spacing=14,
        ),
    )

    return ft.Container(
        padding=20,
        bgcolor="#0F172A",
        expand=True,
        content=ft.Column(
            [
                ft.ResponsiveRow([portrait, dossier], spacing=14, run_spacing=14),
                skill_matrix,
                timeline,
            ],
            spacing=16,
            expand=True,
        ),
    )
