# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Rust-Python hybrid project using PyO3 and Maturin to create Python bindings for Rust code. The Rust library is compiled as a Python extension module named `learning_rust`.

## Architecture

- **Rust Library**: Located in `src/lib.rs`, defines the Rust functions exposed to Python
- **Python Module**: The compiled module is named `learning_rust` (defined in Cargo.toml)
- **PyO3**: Used for Rust-Python interop with stable ABI targeting Python 3.9+
- **Build System**: Maturin handles building and packaging the Rust extension

## Development Commands

### Building the Extension
```bash
# Install maturin (if not already installed)
uv pip install maturin

# Build and install the module in development mode
maturin develop

# Build a wheel
maturin build
```

### Running Tests
```bash
# Run Rust tests
cargo test

# Run Python tests (after building with maturin develop)
python -m pytest tests/
```

### Common Development Tasks
```bash
# Check Rust code
cargo check
cargo clippy

# Format Rust code
cargo fmt

# Clean build artifacts
cargo clean
```

## Key Files

- `src/lib.rs`: Main Rust library code with PyO3 bindings
- `Cargo.toml`: Rust project configuration, defines the cdylib crate type for Python extension
- `pyproject.toml`: Python project configuration, specifies maturin as the build backend
- `tests/`: Python tests for the extension module

## Classes with fields

**Classes with fields** — `NamedTuple`, dataclasses — document every field in
an `Attributes` section:

```python
class BuildInfo(NamedTuple):
    """What the extension module reports about its own build.

    Attributes
    ----------
    version : str
        Version the Rust crate was compiled at.
    profile : str
        Cargo profile used, ``debug`` or ``release``.
    """
```

A type says how a field is shaped, not what it holds. Describing each one
keeps that meaning next to the code, and anything that renders the class —
autodoc, a REPL, an editor tooltip — has a description to show instead of a
bare name.

## Documentation Standards

### Code Blocks

Code blocks are paste-and-run units: pasting one block runs exactly one
intended action. Doctests and other executed examples are exempt — the test
suite runs them, nobody pastes them.

- **One command per block.** Multiple steps may share a block only when
  explicitly chained with `&&`, `;`, or `\` continuations — the chain is
  then one logical command.
- **Explanations go in prose above the block**, never as `#` comments inside it.
- **Command menus are per-command blocks with prose lead-ins**, not tables.
- **Shell commands use the `console` tag with a `$ ` prefix.** This separates
  interactive commands from scripts and enables prompt-aware copy.
- **Split long commands with `\`** — one flag or flag+value pair per indented
  continuation line, positional arguments last.

Good:

Show the last ten commits as a graph:

```console
$ git log \
    --max-count=10 \
    --graph \
    --oneline
```

Bad:

```console
# Show the last ten commits as a graph
$ git log --max-count=10 --graph --oneline
```
