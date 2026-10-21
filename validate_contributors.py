
import json
import re
import sys
from pathlib import Path

# Paths relative to this script
BASE_DIR = Path(__file__).resolve().parent
CONTRIBUTORS_DIR = BASE_DIR / "contributors"

REQUIRED_FIELDS = ["name", "country", "role", "github"]
OPTIONAL_FIELDS = ["linkedin", "highlight"]

GITHUB_PATTERN = re.compile(
    r"^https://github\.com/([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,37}[a-zA-Z0-9])?)\/?$"
)


def validate_contributor(file_path):
    """Validate a contributor JSON file."""
    errors = []

    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, UnicodeError) as error:
        return [f"Invalid JSON: {error}"]
    except OSError as error:
        return [f"Cannot read file: {error}"]

    if not isinstance(data, dict):
        return ["Contributor data must be a JSON object"]

    # Check required fields
    for field in REQUIRED_FIELDS:
        value = data.get(field)

        if not isinstance(value, str) or not value.strip():
            errors.append(
                f"Missing or empty required field: {field}"
            )

    # Validate optional fields if provided
    for field in OPTIONAL_FIELDS:
        if field in data and (
            not isinstance(data[field], str)
            or not data[field].strip()
        ):
            errors.append(
                f"Optional field '{field}' must be a non-empty string"
            )

    # Validate GitHub URL
    github = data.get("github")

    if isinstance(github, str) and github.strip():
        match = GITHUB_PATTERN.fullmatch(github.strip())

        if not match:
            errors.append("Invalid GitHub profile URL")
        else:
            username = match.group(1)

            # Check whether filename matches GitHub username
            if file_path.stem.lower() != username.lower():
                errors.append(
                    f"Filename must match GitHub username: "
                    f"{username}.json"
                )

    return errors


def main():
    if not CONTRIBUTORS_DIR.is_dir():
        print("ERROR: contributors folder not found")
        return 1

    json_files = sorted(CONTRIBUTORS_DIR.glob("*.json"))

    if not json_files:
        print("ERROR: No contributor JSON files found")
        return 1

    total_errors = 0

    print(f"Validating {len(json_files)} contributor files...\n")

    for file_path in json_files:
        errors = validate_contributor(file_path)

        if errors:
            print(f"FAIL: {file_path.name}")

            for error in errors:
                print(f"  - {error}")

            total_errors += len(errors)
        else:
            print(f"PASS: {file_path.name}")

    print("\nValidation Summary")
    print("------------------")
    print(f"Total files: {len(json_files)}")
    print(f"Total errors: {total_errors}")

    if total_errors:
        print("Validation failed.")
        return 1

    print("All contributor files passed validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
