"""Start Bandera and load its versioned investigation instruction."""

from pathlib import Path
import sys


def load_instruction(path: Path) -> tuple[str, str]:
    """Read the instruction and require one non-empty version entry."""
    instruction = path.read_text(encoding="utf-8")
    versions = [
        line.removeprefix("Prompt-Version:").strip()
        for line in instruction.splitlines()
        if line.startswith("Prompt-Version:")
    ]
    if len(versions) != 1 or not versions[0]:
        raise ValueError("Expected exactly one non-empty Prompt-Version entry")
    return instruction, versions[0]


def main() -> int:
    """Report successful startup only after loading a valid instruction."""
    prompt_path = Path(__file__).resolve().parent / "prompts" / "investigation_copilot.md"
    try:
        instruction, version = load_instruction(prompt_path)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Bandera startup failed: {prompt_path}: {error}", file=sys.stderr)
        return 1

    print("Bandera started.")
    print(f"Model instruction loaded successfully: {prompt_path}")
    print(f"Prompt-Version: {version}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
