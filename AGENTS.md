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
## Comments earn their maintenance cost

A comment ships only if it passes all three gates. Fail any: delete or rewrite.
Borderline: delete — borderline means the information is reconstructible, which
is what makes deletion cheap.

**Loss.** Three years from now, would losing this cost a maintainer real time
rediscovering intent, an invariant, a constraint, or a failure mode the code and
tests do not already make obvious?

**Elite.** Would SQLite, Redis, the Go standard library, or CPython write this
comment, at this length? Those projects state the constraint and stop. They do
not argue with an imagined objector.

**Upkeep.** Will it stay true without maintenance? A comment that hand-syncs a
value the code owns — a count, an offset, a line reference, a duplicated
constant — is false the first time that value moves.

### Ceiling

One or two lines. A comment reaching four is either carrying several facts, in
which case split it, or arguing, in which case cut it to the fact.

Rationale, alternatives weighed, and the story of how the code got here belong
in the commit message: timestamped, attached to the exact diff, and free to
maintain.

A comment often holds both a constraint and the deliberation that found it. Keep
the constraint, cut the deliberation. "Runs at most once per second" survives;
"this is the right trade for now" does not.

### Keep

- Why over how: upstream quirks, protocol and compatibility constraints,
  performance tradeoffs still part of the contract.
- Invariants, preconditions, ordering, lifetime, and concurrency requirements
  that types and tests cannot express.
- Code that looks wrong but is not, so a later cleanup does not reintroduce the
  bug.
- A high-level sketch of an algorithm whose local operations do not reveal the
  whole.

### Delete

- Narration of the next lines; code translated into English.
- Restated names, types, defaults, or control flow.
- Values duplicated from the code and hand-synced.
- Justification, hedging, or apology for a choice.
- Speculation about future requirements.
- History version control already holds, including commented-out code.
- Ticket and issue numbers. They say nothing to a reader without tracker access,
  and they rot when the tracker moves. Unfinished work goes in the tracker, not
  the source.
- Transient observations — "currently", "for now", "the latest release" —
  that go stale with no nearby edit.

### The upkeep gate in practice

It reaches values that track our own code. It does not reach frozen external
facts.

Bad (Delete):

```python
# There are 321 tests to complete for servers.
```

Good (Keep):

```python
# CPython < 3.11 has no ExceptionGroup, so this branch stays.
```

### Documentation exception

Doctests, minimal usage examples, and param, return, and raises lines on public
API are exempt from the loss gate — they serve the caller, not the maintainer.
They are exempt from nothing else. Ceiling: a good man page entry.

NumPy-style `Parameters`, `Returns`, and `Attributes` sections and executable
doctests fall under this exception — autodoc ships every field whether or not
you describe it, and a doctest that runs is also a test. Rustdoc `///` comments
and `# Examples` doctests fall under this exception — a rustdoc example is
compiled and run.

