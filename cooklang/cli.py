import logging
from pathlib import Path

import typer

from .chowdown import migrate_cook_to_chowdown
from .nyum import migrate_cook_to_nyum, migrate_nyum_to_cook

app = typer.Typer()


@app.command()
def to_nyum(cook_dir: Path, output_dir: Path):
    """Convert to nyum-style markdown"""
    migrate_cook_to_nyum(cook_dir, output_dir)


@app.command()
def to_chowdown(cook_dir: Path, output_dir: Path):
    """Convert to chowdown-style markdown"""
    migrate_cook_to_chowdown(cook_dir, output_dir)


@app.command()
def from_nyum(nyum_dir: Path, output_dir: Path):
    """Convert from nyum-style markdown"""
    migrate_nyum_to_cook(nyum_dir, output_dir)
