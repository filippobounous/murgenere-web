#!/usr/bin/env python3
"""Setup script for murgenere-web.

Creates a virtual environment, installs dependencies,
and clones the private Streamlit repository used for
`my.murgenere.com`.
"""

import subprocess
from pathlib import Path


def run(cmd):
    print("Running:", " ".join(cmd))
    subprocess.check_call(cmd)


def main():
    root = Path(__file__).parent
    venv = root / '.venv'

    if not venv.exists():
        run(['python3', '-m', 'venv', str(venv)])

    python = venv / 'bin' / 'python'
    run([str(python), '-m', 'pip', 'install', '--upgrade', 'pip'])
    run([str(python), '-m', 'pip', 'install', '-r', 'requirements.txt'])

    personal_repo = root / 'personal'
    if not personal_repo.exists():
        run(['git', 'clone', 'https://github.com/filippobounous/personal.git', str(personal_repo)])
    else:
        run(['git', '-C', str(personal_repo), 'pull'])

    print('\nSetup complete.')
    print(f'Activate the virtual environment with: source {venv}/bin/activate')
    print('Run the Flask server with: python -m app.main')
    print('Launch the Streamlit app with: streamlit run app.py (inside ./personal)')


if __name__ == '__main__':
    main()

