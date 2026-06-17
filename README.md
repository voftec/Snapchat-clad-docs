# CLAD Documentation

> **Source:** https://developers.specs.com/docs/clad  
> **Archived:** 2026-06-17

This repository contains the complete documentation for **CLAD (Closed Loop Agentic Development)** - a suite of agents and skills which allow AI to create in Lens Studio, optimized for SPECS.

## What is CLAD?

- **Closed** means that CLAD allows AI to build autonomously. A single prompt from a developer is usually sufficient for the AI to deliver a working Lens that fulfills the request.
- **Loop** means that CLAD allows AI to work through the development phases of designing, building, and testing, with the capability to repeat these phases in a loop until tests pass.
- **Agentic** means that CLAD can break down complex tasks into smaller pieces that agents can specialize on.
- **Development** means that CLAD allows AI to work as your co-developer. From writing code to writing music, CLAD supports the full development experience.

> **Note:** CLAD is currently in **preview** for SPECS development.

## Repository Structure

```
.
├── README.md              # This file
└── CLAD_Documentation.md  # Complete CLAD documentation
```

## Documentation Contents

The main documentation (`CLAD_Documentation.md`) includes:

1. **CLAD Overview** - Introduction to the CLAD system
2. **How CLAD Works** - Detailed explanation of the development lifecycle
3. **Agents and Skills** - Information about available agents and skills
4. **Setup Guides**:
   - Setup Lens Studio
   - Claude Code Setup
   - Codex Setup
   - Cursor Setup
5. **Tools**:
   - JavaScript Debugger
   - Test Your Lens With LEAF
6. **Troubleshooting**:
   - Troubleshoot Lens Studio MCP
   - Troubleshoot Lens Studio Plugin
7. **Additional Guides**:
   - Convert a Project to SPECS
   - Refresh the Logger
   - Open Project in CLI

## Getting Started

1. Download [Lens Studio](https://ar.snap.com/download)
2. Follow the [Setup Lens Studio](#setup--setup-lens-studio) guide in the documentation
3. Setup your AI tool (Claude Code, Codex, or Cursor)
4. Start prompting AI, for example:
   - "Build a Periodic Table experience for SPECS"
   - "Add music and VFX to my Lens"
   - "Add a shader to make this sphere glow like lava"
   - "Add tests to my Lens"

## Images

All images from the original documentation are described inline in `CLAD_Documentation.md` at the exact positions they appear, using this format:

```
> 📸 IMAGE — <alt text>
> <what the image shows>
```

This allows AI agents to fully understand the visual context without downloading binary assets.

## Community

Connect with other developers to discuss, share what you're building, and learn more in the [r/Spectacles](https://www.reddit.com/r/Spectacles/) community on Reddit.

## License

Documentation archived from https://developers.specs.com/docs/clad for educational purposes.
