from datetime import datetime, timedelta
from pathlib import Path

import flet as ft


GITHUB_PROFILE_URL = "https://github.com/Pehovelo/UNAM-I3691CP-QuoteWise-development-team--QuoteWise"
GITHUB_USERNAME = "Beam1239-png"
GITHUB_REPO_OWNER = "Pehovelo"
GITHUB_REPO_NAME = "UNAM-I3691CP-QuoteWise-development-team--QuoteWise"

SURFACE = "#07111F"
PANEL = "#0D1B2A"
PANEL_ALT = "#10263A"
TEXT = "#E5EEF8"
MUTED = "#8DA2B8"
BORDER = "#20364D"
GREEN = "#48F838"
BLUE = "#38BDF8"
ORANGE = "#F59E0B"

_github_data_cache = None
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
FALLBACK_RECENT_COMMITS = [
    {
        "date": datetime(2026, 6, 8, 15, 28, 5),
        "message": "Update .firebaserc",
        "repo": GITHUB_REPO_NAME,
        "url": f"{GITHUB_PROFILE_URL}/commit/7a81959",
    },
    {
        "date": datetime(2026, 6, 8, 15, 27, 52),
        "message": "Fix formatting in .firebaserc",
        "repo": GITHUB_REPO_NAME,
        "url": f"{GITHUB_PROFILE_URL}/commit/551bdbe",
    },
    {
        "date": datetime(2026, 6, 8, 15, 13, 8),
        "message": "Update .firebaserc",
        "repo": GITHUB_REPO_NAME,
        "url": f"{GITHUB_PROFILE_URL}/commit/b4ca9f5",
    },
    {
        "date": datetime(2026, 6, 7, 13, 32, 27),
        "message": "Remove '.yefd/' from .gitignore",
        "repo": GITHUB_REPO_NAME,
        "url": f"{GITHUB_PROFILE_URL}/commit/4ac16b9",
    },
    {
        "date": datetime(2026, 6, 7, 13, 32, 4),
        "message": "Update .gitignore",
        "repo": GITHUB_REPO_NAME,
        "url": f"{GITHUB_PROFILE_URL}/commit/ef502ef",
    },
    {
        "date": datetime(2026, 6, 7, 10, 39, 41),
        "message": "Fix formatting in import statement for React",
        "repo": GITHUB_REPO_NAME,
        "url": f"{GITHUB_PROFILE_URL}/commit/2d976e8",
    },
    {
        "date": datetime(2026, 6, 7, 10, 39, 20),
        "message": "Fix formatting of import statement in App.js",
        "repo": GITHUB_REPO_NAME,
        "url": f"{GITHUB_PROFILE_URL}/commit/e1242ae",
    },
    {
        "date": datetime(2026, 6, 6, 12, 47, 12),
        "message": "Fix text attribute for automatic line ending normalization",
        "repo": GITHUB_REPO_NAME,
        "url": f"{GITHUB_PROFILE_URL}/commit/f843107",
    },
]


def _commit_dates_from_commits(commits):
    dates = []
    for commit in commits:
        date = commit.get("date")
        if hasattr(date, "date"):
            dates.append(date.date())
        elif date:
            dates.append(date)
    return dates


def box_border(color=BORDER, left_color=None, left_width=1):
    return ft.Border(
        left=ft.BorderSide(left_width, left_color or color),
        right=ft.BorderSide(1, color),
        top=ft.BorderSide(1, color),
        bottom=ft.BorderSide(1, color),
    )


def chip(label, color=BLUE):
    return ft.Container(
        padding=ft.Padding(10, 5, 10, 5),
        bgcolor="#0B1726",
        border=box_border("#1D334B", color),
        border_radius=20,
        content=ft.Text(label, size=10, color=TEXT, no_wrap=True),
    )


def metric(label, value, icon, color=BLUE):
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
                        ft.Text(str(value), size=18, weight=ft.FontWeight.BOLD, color=TEXT),
                        ft.Text(label.upper(), size=10, color=MUTED),
                    ],
                    spacing=0,
                ),
            ],
            spacing=10,
        ),
    )


def _load_github_data(commits_graph_path: Path):
    global _github_data_cache

    if _github_data_cache is not None:
        return _github_data_cache

    username = GITHUB_USERNAME.strip()
    if username.startswith("https://github.com/") or username.startswith("http://github.com/"):
        username = username.rstrip("/").split("/")[-1]
    elif "/" in username:
        username = username.rstrip("/").split("/")[-1]

    github_token = None
    try:
        import os
        github_token = os.environ.get("GITHUB_TOKEN")
    except Exception:
        github_token = None

    recent_commits = []
    dates = []
    if username:
        try:
            from utils.gh_api import (
                fetch_commit_dates_from_repo,
                fetch_recent_commits_from_repo,
            )

            if GITHUB_REPO_OWNER and GITHUB_REPO_NAME:
                dates = fetch_commit_dates_from_repo(
                    GITHUB_REPO_OWNER,
                    GITHUB_REPO_NAME,
                    username,
                    token=github_token,
                    days=90,
                )
                recent_commits = fetch_recent_commits_from_repo(
                    GITHUB_REPO_OWNER,
                    GITHUB_REPO_NAME,
                    username,
                    token=github_token,
                    days=90,
                    max_commits=8,
                )

        except Exception:
            recent_commits = []

    if not recent_commits:
        recent_commits = FALLBACK_RECENT_COMMITS
        dates = _commit_dates_from_commits(recent_commits)

    if dates:
        try:
            from utils.gh_stats import generate_commit_graph_from_dates

            generate_commit_graph_from_dates(dates, commits_graph_path, days=90)
        except Exception:
            pass

    _github_data_cache = recent_commits
    return recent_commits


def evidence_image(path, fallback_icon, title, caption):
    # Support both local Path objects and string URLs. If path is a Path and exists locally, use its
    # string path. Otherwise, if it's a string starting with http(s), use it directly. This avoids
    # file:// URIs and Windows-specific paths that break when deployed.
    src = None
    try:
        # If a Path is passed
        if hasattr(path, "exists") and path.exists():
            src = str(path)
        elif isinstance(path, str) and (path.startswith("http://") or path.startswith("https://")):
            src = path
    except Exception:
        src = None

    if src:
        return ft.Container(
            bgcolor="#06101C",
            border=box_border("#1E3A53"),
            border_radius=8,
            padding=10,
            content=ft.Image(src=src, fit=ft.BoxFit.CONTAIN),
        )

    return ft.Container(
        bgcolor="#06101C",
        border=box_border("#1E3A53"),
        border_radius=8,
        padding=18,
        content=ft.Row(
            [
                ft.Icon(fallback_icon, color=BLUE, size=28),
                ft.Column(
                    [
                        ft.Text(title, size=14, weight=ft.FontWeight.BOLD, color=TEXT),
                        ft.Text(caption, size=12, color=MUTED),
                    ],
                    spacing=4,
                    expand=True,
                ),
            ],
            spacing=12,
        ),
    )


def find_commit_screenshots(assets_base):
    screenshots_dir = assets_base.joinpath("Commit screenshot evidence")
    if not screenshots_dir.exists():
        return []

    # On local dev we can return Path objects; for deployment, convert to GitHub raw URLs
    files = sorted(
        [
            path
            for path in screenshots_dir.iterdir()
            if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
        ],
        key=lambda path: path.name.lower(),
    )

    # If the repo is published to GitHub, prefer serving images from the GitHub raw URL so Flet Web can load them.
    github_base = "https://github.com/Beam1239-png/web_portfolio/blob/main/assets/github/Commit%20screenshot%20evidence"
    web_urls = []
    for p in files:
        try:
            web_urls.append(f"{github_base}/{p.name}?raw=1")
        except Exception:
            web_urls.append(str(p))

    return web_urls


def evidence_gallery(paths):
    if not paths:
        return evidence_image(
            Path("missing-commit-evidence.png"),
            ft.Icons.IMAGE_SEARCH,
            "Commit image evidence",
            "Place commit screenshots in assets/github/Commit screenshot evidence to display them here.",
        )
    # `paths` can be a list of Path objects (local) or strings (URL). Use the value as the image src.
    return ft.ResponsiveRow(
        [
            ft.Container(
                col={"sm": 12, "md": 6},
                content=ft.Container(
                    bgcolor="#06101C",
                    border=box_border("#1E3A53"),
                    border_radius=8,
                    padding=10,
                    ink=True,
                    on_click=lambda e, image_path=path: show_screenshot_dialog(e, image_path),
                    content=ft.Column(
                        [
                            ft.Container(
                                height=190,
                                bgcolor="#030A12",
                                border_radius=6,
                                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                                content=ft.Image(src=(str(path) if not isinstance(path, str) else path), fit=ft.BoxFit.CONTAIN),
                            ),
                            ft.Row(
                                [
                                    ft.Icon(ft.Icons.IMAGE, size=16, color=BLUE),
                                    ft.Text((path.name if hasattr(path, 'name') else path.split('/')[-1]), size=11, color=MUTED, expand=True, no_wrap=True),
                                    ft.Icon(ft.Icons.ZOOM_IN, size=16, color=BLUE),
                                ],
                                spacing=6,
                            ),
                        ],
                        spacing=8,
                    ),
                ),
            )
            for path in paths
        ],
        spacing=12,
        run_spacing=12,
    )


def show_screenshot_dialog(e, image_path):
    # Determine a safe display name whether image_path is a Path or a URL string
    try:
        if isinstance(image_path, str):
            from urllib.parse import unquote, urlparse

            parsed = urlparse(image_path)
            display_name = unquote(parsed.path.split("/")[-1]) or image_path
        else:
            display_name = getattr(image_path, "name", str(image_path))
    except Exception:
        display_name = str(image_path)

    dlg = ft.AlertDialog(
        modal=True,
        title=ft.Row(
            [
                ft.Icon(ft.Icons.IMAGE_SEARCH, color=BLUE, size=22),
                ft.Text(display_name, color=TEXT, size=16, weight=ft.FontWeight.BOLD),
            ],
            spacing=8,
        ),
        content=ft.Container(
            width=900,
            height=560,
            bgcolor="#030A12",
            border=box_border("#1E3A53"),
            border_radius=8,
            padding=10,
            content=ft.Image(src=(str(image_path) if not isinstance(image_path, str) else image_path), fit=ft.BoxFit.CONTAIN),
        ),
        actions=[
            ft.TextButton(
                "Close",
                on_click=close_dialog,
            )
        ],
    )
    e.page.show_dialog(dlg)


def close_dialog(e):
    e.page.pop_dialog()


def commit_card(commit, index):
    message = commit.get("message", "No commit message")
    repo = commit.get("repo", GITHUB_REPO_NAME)
    date = commit.get("date")
    date_label = date.strftime("%d %b %Y") if hasattr(date, "strftime") else str(date or "Recent")
    color = [GREEN, BLUE, ORANGE, "#EC4899"][index % 4]

    return ft.Container(
        bgcolor=PANEL,
        border=box_border(left_color=color, left_width=4),
        border_radius=8,
        padding=14,
        content=ft.Row(
            [
                ft.Container(
                    width=38,
                    height=38,
                    bgcolor="#07111F",
                    border=box_border(color),
                    border_radius=8,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Icon(ft.Icons.COMMIT, size=21, color=color),
                ),
                ft.Column(
                    [
                        ft.Text(message, weight=ft.FontWeight.BOLD, size=14, color=TEXT, max_lines=2),
                        ft.Row(
                            [
                                ft.Text(repo, size=11, color=MUTED),
                                ft.Text("|", size=11, color="#35516B"),
                                ft.Text(date_label, size=11, color=MUTED),
                            ],
                            spacing=7,
                        ),
                    ],
                    expand=True,
                    spacing=4,
                ),
                ft.OutlinedButton(
                    "View",
                    icon=ft.Icons.OPEN_IN_NEW,
                    url=commit.get("url"),
                    style=ft.ButtonStyle(color=color),
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=12,
        ),
    )


def empty_commits_card():
    return ft.Container(
        bgcolor=PANEL,
        border=box_border(left_color=ORANGE, left_width=4),
        border_radius=8,
        padding=16,
        content=ft.Row(
            [
                ft.Icon(ft.Icons.WIFI_OFF, size=24, color=ORANGE),
                ft.Column(
                    [
                        ft.Text("Live commit feed unavailable", size=15, weight=ft.FontWeight.BOLD, color=TEXT),
                        ft.Text(
                            "GitHub API data could not be loaded right now. Local evidence remains available below.",
                            size=12,
                            color=MUTED,
                        ),
                    ],
                    spacing=4,
                    expand=True,
                ),
            ],
            spacing=12,
        ),
    )


def activity_signal(commits, days=14):
    end = datetime.now().date()
    start = end - timedelta(days=days - 1)
    day_list = [start + timedelta(days=index) for index in range(days)]
    counts = {day: 0 for day in day_list}

    for commit in commits:
        date = commit.get("date")
        commit_day = date.date() if hasattr(date, "date") else date
        if commit_day in counts:
            counts[commit_day] += 1

    max_count = max(counts.values()) if counts else 0
    active_days = sum(1 for count in counts.values() if count)
    total_commits = sum(counts.values())

    if not total_commits:
        return ft.Container(
            height=150,
            bgcolor="#06101C",
            border=box_border("#1E3A53"),
            border_radius=8,
            padding=18,
            content=ft.Row(
                [
                    ft.Icon(ft.Icons.BAR_CHART, color=ORANGE, size=28),
                    ft.Column(
                        [
                            ft.Text("Activity signal pending", size=14, weight=ft.FontWeight.BOLD, color=TEXT),
                            ft.Text("Commit dates will appear here when feed data is available.", size=12, color=MUTED),
                        ],
                        spacing=4,
                        expand=True,
                    ),
                ],
                spacing=12,
            ),
        )

    return ft.Container(
        bgcolor="#06101C",
        border=box_border("#1E3A53"),
        border_radius=8,
        padding=14,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(f"{total_commits} commits", size=13, weight=ft.FontWeight.BOLD, color=TEXT),
                        ft.Container(expand=True),
                        ft.Text(f"{active_days} active days", size=12, color=MUTED),
                    ],
                    spacing=8,
                ),
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Container(
                                    height=96,
                                    alignment=ft.Alignment(0, 1),
                                    content=ft.Container(
                                        height=10 + int((counts[day] / max_count) * 82) if counts[day] else 6,
                                        bgcolor=GREEN if counts[day] else "#20364D",
                                        border_radius=4,
                                    ),
                                ),
                                ft.Text(day.strftime("%d"), size=10, color=MUTED, text_align=ft.TextAlign.CENTER),
                            ],
                            expand=True,
                            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                            spacing=6,
                        )
                        for day in day_list
                    ],
                    spacing=5,
                ),
            ],
            spacing=12,
        ),
    )


def github_page():
    assets_base = Path(__file__).parent.parent.joinpath("assets", "github")
    commits_graph_path = assets_base.joinpath("commits_graph.png")
    # Serve PR image via GitHub raw URL so it loads in browsers when deployed
    pr1 = "https://github.com/Beam1239-png/web_portfolio/blob/main/assets/github/pr1.png?raw=1"
    commit_screenshots = find_commit_screenshots(assets_base)

    recent_commits = _load_github_data(commits_graph_path)
    commit_count = len(recent_commits)
    repo_short = GITHUB_REPO_NAME.replace("UNAM-I3691CP-", "")

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
                                ft.Text("GitHub Evidence", size=32, weight=ft.FontWeight.BOLD, color=TEXT),
                                ft.Text(
                                    "Repository activity, commit proof, pull request evidence, and contribution impact.",
                                    size=14,
                                    color=MUTED,
                                ),
                            ],
                            spacing=4,
                            expand=True,
                        ),
                        ft.OutlinedButton(
                            "View Repository",
                            icon=ft.Icons.OPEN_IN_NEW,
                            url=GITHUB_PROFILE_URL,
                            style=ft.ButtonStyle(color=GREEN),
                        ),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),
                ft.Row(
                    [
                        metric("Commit Images", len(commit_screenshots), ft.Icons.IMAGE, GREEN),
                        metric("Evidence Window", "90 days", ft.Icons.DATE_RANGE, BLUE),
                        metric("Feed Commits", commit_count, ft.Icons.COMMIT, ORANGE),
                    ],
                    spacing=12,
                ),
            ],
            spacing=18,
        ),
    )

    repo_panel = ft.Container(
        bgcolor=PANEL,
        border=box_border(left_color=GREEN, left_width=4),
        border_radius=8,
        padding=18,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Icon(ft.Icons.ACCOUNT_TREE, color=GREEN, size=24),
                        ft.Column(
                            [
                                ft.Text("Tracked Repository", size=16, color=TEXT, weight=ft.FontWeight.BOLD),
                                ft.Text(f"{GITHUB_REPO_OWNER}/{repo_short}", size=12, color=MUTED),
                            ],
                            spacing=3,
                            expand=True,
                        ),
                    ],
                    spacing=10,
                ),
                ft.Row(
                    [
                        chip(GITHUB_USERNAME, GREEN),
                        chip("Commits", BLUE),
                        chip("Pull Requests", ORANGE),
                        chip("Contribution Evidence", "#EC4899"),
                    ],
                    wrap=True,
                    spacing=8,
                    run_spacing=8,
                ),
            ],
            spacing=14,
        ),
    )

    graph_panel = ft.Container(
        bgcolor=PANEL,
        border=box_border(),
        border_radius=8,
        padding=18,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Icon(ft.Icons.INSIGHTS, color=BLUE, size=24),
                        ft.Column(
                            [
                                ft.Text("Commit Activity Signal", size=16, color=TEXT, weight=ft.FontWeight.BOLD),
                                ft.Text(f"Recent commit rhythm for {GITHUB_USERNAME}.", size=12, color=MUTED),
                            ],
                            spacing=3,
                            expand=True,
                        ),
                    ],
                    spacing=10,
                ),
                activity_signal(recent_commits),
            ],
            spacing=14,
        ),
    )

    commits_section = ft.Container(
        bgcolor="#081827",
        border=box_border(),
        border_radius=8,
        padding=18,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text("Recent Commit Feed", size=18, color=TEXT, weight=ft.FontWeight.BOLD),
                                ft.Text(f"Latest authored commits from {GITHUB_USERNAME} in the tracked repository.", size=12, color=MUTED),
                            ],
                            spacing=3,
                            expand=True,
                        ),
                        chip("BEAM COMMITS" if recent_commits else "READY", GREEN if recent_commits else ORANGE),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),
                *([commit_card(commit, index) for index, commit in enumerate(recent_commits)] or [empty_commits_card()]),
            ],
            spacing=12,
        ),
    )

    proof_grid = ft.ResponsiveRow(
        [
            ft.Container(
                col={"sm": 12, "md": 6},
                content=ft.Container(
                    bgcolor=PANEL,
                    border=box_border(left_color=BLUE, left_width=4),
                    border_radius=8,
                    padding=18,
                    content=ft.Column(
                        [
                            ft.Text("Commit Screenshot Evidence", size=16, color=TEXT, weight=ft.FontWeight.BOLD),
                            ft.Text(
                                "Uploaded from assets/github/Commit screenshot evidence.",
                                size=12,
                                color=MUTED,
                            ),
                            evidence_gallery(commit_screenshots),
                        ],
                        spacing=12,
                    ),
                ),
            ),
            ft.Container(
                col={"sm": 12, "md": 6},
                content=ft.Container(
                    bgcolor=PANEL,
                    border=box_border(left_color=ORANGE, left_width=4),
                    border_radius=8,
                    padding=18,
                    content=ft.Column(
                        [
                            ft.Text("Pull Request Evidence", size=16, color=TEXT, weight=ft.FontWeight.BOLD),
                            evidence_image(pr1, ft.Icons.CALL_MERGE, "Pull request proof", "PR screenshots can be added to assets/github/pr1.png."),
                        ],
                        spacing=12,
                    ),
                ),
            ),
        ],
        spacing=18,
        run_spacing=18,
    )

    impact_card = ft.Container(
        bgcolor=PANEL_ALT,
        border=box_border(left_color="#EC4899", left_width=4),
        border_radius=8,
        padding=18,
        content=ft.Row(
            [
                ft.Icon(ft.Icons.ROCKET_LAUNCH, color="#EC4899", size=26),
                ft.Column(
                    [
                        ft.Text("Impact Summary", size=16, color=TEXT, weight=ft.FontWeight.BOLD),
                        ft.Text(
                            "Contributions strengthened navigation, user experience, repository traceability, and visible project delivery evidence.",
                            size=13,
                            color="#B8C7D8",
                        ),
                    ],
                    spacing=4,
                    expand=True,
                ),
            ],
            spacing=12,
        ),
    )

    return ft.Container(
        content=ft.Column(
            [
                header,
                ft.Row([repo_panel, graph_panel], spacing=18),
                commits_section,
                proof_grid,
                impact_card,
            ],
            spacing=18,
        ),
        padding=20,
        bgcolor=SURFACE,
        expand=True,
    )
