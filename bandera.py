"""Send one incident to Bandera's local model and print its response."""

from pathlib import Path
import sys

import ollama


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
    """Load the instruction and complete one incident-response exchange."""
    prompt_path = Path(__file__).resolve().parent / "prompts" / "investigation_copilot.md"
    try:
        instruction, version = load_instruction(prompt_path)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Bandera startup failed: {prompt_path}: {error}", file=sys.stderr)
        return 1

    print("Bandera started.")
    print(f"Model instruction loaded successfully: {prompt_path}")
    print(f"Prompt-Version: {version}")
    try:
        incident = input("Describe the incident: ").strip()
    except EOFError:
        print("Bandera input failed: no incident description received.", file=sys.stderr)
        return 1
    if not incident:
        print("Bandera input failed: incident description cannot be empty.", file=sys.stderr)
        return 1

    print("Bandera is investigating...", flush=True)
    response_started = False
    has_content = False
    try:
        response = ollama.chat(
            model="qwen3.5:27b",
            messages=[
                {"role": "system", "content": instruction},
                {"role": "user", "content": incident},
            ],
            stream=True,
        )
        for chunk in response:
            content = chunk.message.content
            if content:
                if not response_started:
                    print("\nBandera:", flush=True)
                    response_started = True
                print(content, end="", flush=True)
                has_content = has_content or bool(content.strip())
        if not has_content:
            raise ValueError("The model returned an empty response")
    except Exception as error:
        if response_started:
            print(flush=True)
        print(f"Bandera model call failed: {error}", file=sys.stderr)
        return 1

    print(flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
