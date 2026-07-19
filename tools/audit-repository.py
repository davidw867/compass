from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

STANDARD = ROOT / "tools" / "repository-standard.json"

with open(STANDARD, "r", encoding="utf8") as f:
    spec = json.load(f)

critical = []
warnings = []

def check_directory(base, name):
    path = base / name
    if not path.exists():
        critical.append(f"Missing directory: {path}")

def check_file(base, name):
    path = base / name
    if not path.exists():
        critical.append(f"Missing file: {path}")

print("=" * 60)
print("Compass One Repository Compliance Audit")
print("Repository Standard:", spec["version"])
print("=" * 60)

#
# Root Directories
#

for folder in spec["requiredRootDirectories"]:
    check_directory(ROOT, folder)

#
# Root Files
#

for file in spec["requiredRootFiles"]:
    check_file(ROOT, file)

#
# Agents
#

agent_root = ROOT / "agents"

for folder in spec["requiredAgentDirectories"]:

    path = agent_root / folder

    if not path.exists():
        critical.append(f"Missing agent: {folder}")
    else:

        readme = path / "README.md"

        if not readme.exists():
            warnings.append(f"Missing README: {readme}")

#
# Connectors
#

connector_root = ROOT / "connectors"

for folder in spec["requiredConnectorDirectories"]:

    path = connector_root / folder

    if not path.exists():
        critical.append(f"Missing connector: {folder}")
    else:

        readme = path / "README.md"

        if not readme.exists():
            warnings.append(f"Missing README: {readme}")

#
# Providers
#

provider_root = ROOT / "providers"

for folder in spec["requiredProviderDirectories"]:

    path = provider_root / folder

    if not path.exists():
        critical.append(f"Missing provider: {folder}")
    else:

        readme = path / "README.md"

        if not readme.exists():
            warnings.append(f"Missing README: {readme}")

#
# Projects
#

src_root = ROOT / "src"

for project in spec["requiredProjects"]:

    path = src_root / project

    if not path.exists():
        critical.append(f"Missing project: {project}")
    else:

        readme = path / "README.md"

        if not readme.exists():
            warnings.append(f"Missing README: {readme}")

#
# Tests
#

tests_root = ROOT / "tests"

for folder in spec["requiredTestDirectories"]:

    path = tests_root / folder

    if not path.exists():
        critical.append(f"Missing test directory: {folder}")
    else:

        readme = path / "README.md"

        if not readme.exists():
            warnings.append(f"Missing README: {readme}")

#
# Report
#

print()

if critical:

    print("CRITICAL")

    for item in critical:
        print("  ", item)

else:
    print("No critical issues found.")

print()

if warnings:

    print("WARNINGS")

    for item in warnings:
        print("  ", item)

else:
    print("No warnings found.")

print()

if critical:
    print("FAILED")
    sys.exit(1)

print("PASSED")
sys.exit(0)
