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