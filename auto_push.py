import os
import datetime
import subprocess

def auto_push(commit_msg="Auto commit"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_msg = f"{commit_msg} @ {timestamp}"

    commands = [
        'git add .',
        f'git commit -m "{full_msg}"',
        'git push origin main'
    ]

    for cmd in commands:
        print(f"Running: {cmd}")
        result = subprocess.run(cmd, shell=True)
        if result.returncode != 0:
            print(f"[ERROR] Failed: {cmd}")
            break
    else:
        print(f"[?] Pushed: {full_msg}")

if __name__ == "__main__":
    auto_push()
