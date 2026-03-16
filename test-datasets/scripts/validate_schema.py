#!/usr/bin/env python3
"""Validate generated datasets against upstream convention JSON schemas.

Downloads the latest schema.json from each convention repo and validates
every zarr.json that declares that convention via zarr_conventions.

Usage:
    python validate_schema.py           # validate all
    python validate_schema.py --verbose # show per-file details

Requires: jsonschema
Exit code 0 = all pass, 1 = failures.
"""

import json
import sys
import urllib.request
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("SKIP: jsonschema not installed (pip install jsonschema)")
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
VERBOSE = "--verbose" in sys.argv

# Convention UUID -> schema URL (from upstream repos)
# Uses main branch: v1 tags don't exist yet on these repos.
SCHEMA_URLS = {
    "f17cb550-5864-4468-aeb7-f3180cfb622f": (
        "proj:",
        "https://raw.githubusercontent.com/zarr-conventions/geo-proj/main/schema.json",
    ),
    "689b58e2-cf7b-45e0-9fff-9cfc0883d6b4": (
        "spatial:",
        "https://raw.githubusercontent.com/zarr-conventions/spatial/main/schema.json",
    ),
    "d35379db-88df-4056-af3a-620245f8e347": (
        "multiscales",
        "https://raw.githubusercontent.com/zarr-conventions/multiscales/main/schema.json",
    ),
}


def fetch_schema(url):
    """Download and parse a JSON schema."""
    with urllib.request.urlopen(url) as resp:
        return json.loads(resp.read())


def log(msg):
    if VERBOSE:
        print(f"    {msg}")


def main():
    # Fetch schemas
    schemas = {}
    print("Fetching convention schemas...")
    for uuid, (name, url) in SCHEMA_URLS.items():
        try:
            schemas[uuid] = fetch_schema(url)
            print(f"  {name} OK")
        except Exception as e:
            print(f"  {name} FAILED: {e}")
            sys.exit(1)

    passed = 0
    failed = 0
    errors = []

    # Validate valid datasets
    for zarr_json in sorted(ROOT.rglob("valid/**/*.zarr/**/zarr.json")):
        meta = json.loads(zarr_json.read_text())
        attrs = meta.get("attributes", {})
        conventions = attrs.get("zarr_conventions", [])
        if not conventions:
            continue

        rel = zarr_json.relative_to(ROOT)
        for conv in conventions:
            uuid = conv.get("uuid")
            if uuid not in schemas:
                continue
            conv_name = conv.get("name", uuid)
            schema = schemas[uuid]
            try:
                jsonschema.validate(meta, schema)
                log(f"PASS {rel} [{conv_name}]")
                passed += 1
            except jsonschema.ValidationError as e:
                msg = f"{rel} [{conv_name}]: {e.message}"
                errors.append(msg)
                failed += 1

    # Validate invalid datasets (should fail schema validation)
    invalid_checked = 0
    invalid_rejected = 0
    invalid_escaped = []
    for zarr_json in sorted(ROOT.rglob("invalid/**/*.zarr/**/zarr.json")):
        meta = json.loads(zarr_json.read_text())
        attrs = meta.get("attributes", {})
        conventions = attrs.get("zarr_conventions", [])
        if not conventions:
            continue

        rel = zarr_json.relative_to(ROOT)
        for conv in conventions:
            uuid = conv.get("uuid")
            if uuid not in schemas:
                continue
            conv_name = conv.get("name", uuid)
            schema = schemas[uuid]
            invalid_checked += 1
            try:
                jsonschema.validate(meta, schema)
                msg = f"{rel} [{conv_name}]: schema did not reject"
                invalid_escaped.append(msg)
                print(f"  FAIL {msg}")
            except jsonschema.ValidationError:
                log(f"PASS {rel} [{conv_name}]: correctly rejected")
                invalid_rejected += 1

    print(f"\nValid: {passed} passed, {failed} failed")
    print(
        f"Invalid: {invalid_rejected} correctly rejected out of {invalid_checked} checked"
    )

    if errors:
        print("\nErrors:")
        for e in errors:
            print(f"  - {e}")

    if invalid_escaped:
        print("\nInvalid datasets that escaped validation:")
        for e in invalid_escaped:
            print(f"  - {e}")

    sys.exit(1 if (failed or invalid_escaped) else 0)


if __name__ == "__main__":
    main()
