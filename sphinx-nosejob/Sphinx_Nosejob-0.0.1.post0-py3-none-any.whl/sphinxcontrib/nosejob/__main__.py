import click
import subprocess
from pathlib import Path

LANGUAGES = {
   "English"   :"en",
#    "Afrikaans" :"af",
}

@click.command()
@click.option("--project",  prompt = "The name of the project",      help = "The name of the project")
@click.option("--author",   prompt = "The name of the author",       help = "The name of the author")
@click.option("--release",  prompt = "The projects' release number", help = "The projects' release number", default = "0.0.0")
@click.option("--language", prompt = "The projects' release number", help = "The projects' release number", default="English",
    type=click.Choice(LANGUAGES.keys(), case_sensitive=False))
@click.argument("source",  # prompt = "The documentaion source folder",
    required=True, 
    type = click.Path(resolve_path=True,file_okay=False),
    default = Path("docs").resolve())
def main(source, project="Project", release="0.0.0", author="", language="English", verbose= True) :
    """Nosejob wrapper for the Sphix: Quickstart utility"""
    root = Path.cwd().resolve()
    path = Path("source")
    docs = Path(source)
    version = '.'.join(release.split('.')[:-1])
    process = subprocess.Popen(["sphinx-quickstart", "--no-batchfile", "--no-makefile", 
                   f"--project={project}", 
                   f"--author={author}", 
                   f"-v {version}", 
                   f"--release={release}", 
                   f"--language={LANGUAGES.get(language,'en')}",
                    "--master=index", 
                    "--dot=.", 
                    "--suffix=.rst", 
                    "--sep", 
                    "--ext-autodoc",
                    "--ext-doctest",
                    "--ext-intersphinx",
                    "--ext-todo",
                    "--ext-coverage",
                    "--ext-imgmath",
                    "--ext-mathjax",
                    "--ext-ifconfig",
                    "--ext-viewcode",
                    "--ext-githubpages",
                    "--extensions=sphinxcontrib.nosejob",
                    str(root)])
    process.communicate()
    source = path if path.is_absolute() else root/path
    target = docs if docs.is_absolute() else root/docs
    import time
    time.sleep(20)
    source.replace(target)
