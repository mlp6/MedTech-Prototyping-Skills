from pathlib import Path
import subprocess

p = Path('.')
texfiles = list(p.glob('**/*.tex'))

for f in texfiles:
	subprocess.run(["latexmk", "-pdf", "-cd", f])
