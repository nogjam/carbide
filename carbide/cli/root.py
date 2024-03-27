"""Defines the CLI."""

from importlib.metadata import version
import subprocess
from typing import Any

import click

from ..config import REPO_ROOT_DIR
from ..local import LocalData
from .gen_description_from_script import gen_description_from_script


def print_version(ctx: click.Context, param: click.Parameter, value: Any) -> None:
    # Adapted from the Click documentation:
    # https://click.palletsprojects.com/en/8.1.x/options/#callbacks-and-eager-options
    if not value or ctx.resilient_parsing:
        return
    pkg_name: str = __name__.split(".", maxsplit=1)[0]
    click.echo(f"{pkg_name} {version(pkg_name)}")
    ctx.exit()


# Have Pyright calm down re. backslash sequences in the logo string.
# pyright: reportInvalidStringEscapeSequence=none


@click.group
@click.option(
    "--version",
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,
    help="Show the version and exit.",
)
@click.option("--python/--shell", default=False)
@click.pass_context
def cli_root(ctx: click.Context, python: bool):
    """\b
                  _    _    _
      __ __ _ _ _| |__(_)__| |___
     / _/ _` | '_| '_ \ / _` / -_)
     \__\__,_|_| |_.__/_\__,_\___|

    A collection of tools for increasing developer productivity.
    """
    ctx.ensure_object(dict)

    ctx.obj["PYTHON_IMPL"] = python


@cli_root.group("cp")
def copy_group():
    """Copy operations."""
    ...


@cli_root.group("register")
def register_group():
    """For registering local entities with carbide."""
    ...


@copy_group.command(
    "files-with-name", help=gen_description_from_script("copy_all_files_with_name.sh")
)
@click.argument("name")
@click.argument("source", type=click.Path(exists=True, file_okay=False))
@click.argument("dest", type=click.Path(file_okay=False))
@click.pass_context
def copy_all_files_with_name_command(
    ctx: click.Context, name: str, source: str, dest: str
):
    if ctx.obj["PYTHON_IMPL"]:
        from scripts.copy_all_files_with_name import copy_all_files_with_name

        for message in copy_all_files_with_name(name, source, dest):
            click.echo(message)
    else:
        # TODO: Handle subprocess.run() calls with a function in the same
        # module as gen_description_from_script().
        subprocess.run(
            [
                REPO_ROOT_DIR / "scripts" / "copy_all_files_with_name.sh",
                name,
                source,
                dest,
            ],
            capture_output=True,
        )


@register_group.command("git-repo", help="Register a git repo for quick access.")
@click.argument("path", type=click.Path(exists=True, file_okay=False))
def register_git_repo_command(path: str):
    LocalData.register_git_repo(path)
    click.echo(f"Directory is: {path}")
