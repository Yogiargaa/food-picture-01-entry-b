import os
import shutil


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(script_dir, "entry.png"),
        os.path.join(os.getcwd(), "entry.png"),
    ]
    src = next((p for p in candidates if os.path.exists(p)), candidates[0])
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
