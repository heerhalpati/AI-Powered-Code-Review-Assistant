import subprocess

def analyze_python_code(code):
    with open("temp_code.py", "w") as f:
        f.write(code)

    result = subprocess.run(
        ["pylint", "temp_code.py", "--disable=C0114,C0116"],
        capture_output=True, text=True
    )

    return result.stdout
