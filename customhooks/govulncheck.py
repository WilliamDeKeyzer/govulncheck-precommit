from __future__ import annotations

import subprocess

def main() -> int:
    result = subprocess.run(['govulncheck', './...'], stdout=subprocess.PIPE, check=True, text=True)

    data = result.stdout
    result = result.returncode

    if result != 0:
        print("Vulnerabilities found!")
        print(data.decode('utf-8'))

    return result


if __name__ == '__main__':
    raise SystemExit(main())