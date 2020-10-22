import argparse as ap
import subprocess

if __name__ == '__main__':
    p = ap.ArgumentParser(description="Unix wizard commands")
    command = ''
    new_command = 'sudo apt-get install {}'

    p.add_argument(
        '--docker',
        action='store_true',
        help='install docker')

    args = p.parse_args()
    if args.docker:
        command += new_command.format('docker')

    subprocess.call(command, shell=True)
