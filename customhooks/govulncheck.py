from __future__ import annotations

import subprocess

def main() -> int:
    result = subprocess.run(['govulncheck', './...'], stdout=subprocess.PIPE, check=True)

    data = result.stdout
    result = result.returncode

    print("ExitCode : ", result)
    print("Output.  : ", data.decode('utf-8'))

    return result


if __name__ == '__main__':
    raise SystemExit(main())