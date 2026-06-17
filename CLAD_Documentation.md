# CLAD — Complete Documentation

> **Source:** https://developers.specs.com/docs/clad  
> **Archived:** 2026-06-17

---

## How to read image/GIF descriptions in this document

Every image and animated GIF from the original documentation is represented inline at the exact position it appears on the page, using this format:

```
> 📸 IMAGE — <alt text>
> <what the image shows>
```

```
> 🎞️ GIF (animated) — <alt text>
> <what the animation shows, including the before/after states and what action is demonstrated>
```

All original image asset URLs are also preserved so they can be fetched directly.

---

## Table of Contents

1. [CLAD Overview](#1-clad-overview)
2. [How CLAD Works](#2-how-clad-works)
3. [Agents and Skills](#3-agents-and-skills)
4. [Setup — Setup Lens Studio](#4-setup--setup-lens-studio)
5. [Setup AI — Claude Code Setup](#5-setup-ai--claude-code-setup)
6. [Setup AI — Codex Setup](#6-setup-ai--codex-setup)
7. [Setup AI — Cursor Setup](#7-setup-ai--cursor-setup)
8. [Tools — JavaScript Debugger](#8-tools--javascript-debugger)
9. [Tools — Test Your Lens With LEAF](#9-tools--test-your-lens-with-leaf)
10. [Troubleshooting — Troubleshoot Lens Studio MCP](#10-troubleshooting--troubleshoot-lens-studio-mcp)
11. [Troubleshooting — Troubleshoot Lens Studio Plugin](#11-troubleshooting--troubleshoot-lens-studio-plugin)
12. [Additional Guides — Convert a Project to SPECS](#12-additional-guides--convert-a-project-to-specs)
13. [Additional Guides — Refresh the Logger](#13-additional-guides--refresh-the-logger)
14. [Additional Guides — Open Project in CLI](#14-additional-guides--open-project-in-cli)

---

## 1. CLAD Overview

> **URL:** https://developers.specs.com/docs/clad

# CLAD

Closed loop agentic development (CLAD) is a suite of agents and skills which allow AI to create in Lens Studio, optimized for SPECS.

- **Closed** means that CLAD allows AI to build autonomously. A single prompt from a developer is usually sufficient for the AI to deliver a working Lens that fulfills the request.
- **Loop** means that CLAD allows AI to work through the development phases of designing, building, and testing, with the capability to repeat these phases in a loop until tests pass.
- **Agentic** means that CLAD can break down complex tasks into smaller pieces that agents can specialize on. Lens Studio includes a broad set of tools and skills which AI uses to work effectively on both new and existing projects. CLAD focuses an AI's context to the current task but with the capability to progressively disclose additional information as necessary.
- **Development** means that CLAD allows AI to work as your co-developer. From writing code to writing music, CLAD supports the full development experience.

> **Note:** CLAD is currently in **preview** for SPECS development.

> 📸 IMAGE — **CLAD overview diagram** (`circuit-flow.webp`)  
> A flow diagram showing CLAD as a closed loop. It depicts the circular relationship between the AI agent, Lens Studio (via MCP), and the SPECS platform. Arrows show the flow: the developer gives a prompt → AI agents invoke skills → Lens Studio MCP tools execute changes in the editor → the preview/device provides feedback → the loop repeats. The diagram emphasizes that the loop is self-contained and autonomous.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/overview/circuit-flow.webp_

> 📸 IMAGE — **CLAD workflow diagram** (`stack-flow.webp`)  
> A horizontal pipeline diagram showing the four phases of the CLAD workflow stacked left to right: **Design & Prototype** → **Test & Optimize** → **Publish** → **Post-Production**. Each phase is represented as a labeled block. This gives a high-level at-a-glance view of the entire development lifecycle that CLAD covers.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/overview/stack-flow.webp_

### Key Points

- CLAD can be used with your favorite AI tools (Claude Code, Codex, Cursor, etc.).
- CLAD can be extended with your own tools and skills.
- CLAD can be used to create new projects or iterate on existing ones.
- CLAD is optimized for the SPECS platform.
- CLAD can "one-shot" lenses (to build a working result after just a single prompt), but it can also build alongside you as a co-developer.

### How it works

CLAD connects your AI to [Lens Studio](https://ar.snap.com/download), a fully-featured IDE for creating interactive experiences. Lens Studio provides an MCP server which supports the connection and provides a host of tools for the AI to use the editor. In addition to those MCP tools, CLAD includes an additional [suite of agents and skills](https://github.com/lens-studio-devs/ls-extensions/) that enable your AI to build a complete SPECS experience: from prototype to distribution.

> **Note:** For more information on how CLAD works, see [How CLAD Works](#2-how-clad-works).

### Get Started

1. Download [Lens Studio](https://ar.snap.com/download).
2. [Setup Lens Studio](#4-setup--setup-lens-studio) — create a SPECS project for CLAD.
3. Setup AI — connect [Claude Code](#5-setup-ai--claude-code-setup), [Codex](#6-setup-ai--codex-setup), or [Cursor](#7-setup-ai--cursor-setup).
4. Prompt AI, for example:
   - "Build a Periodic Table experience for SPECS"
   - "Add music and VFX to my Lens"
   - "Add a shader to make this sphere glow like lava"
   - "Add tests to my Lens"

> **Note:** You can apply to the [SPECS Developer Program](https://developers.specs.com) to learn more.

> **Note:** Built something cool with CLAD? Sign up for [CLAD Device Access](https://developers.specs.com/clad-access) to get queued for office hours and try it on a physical device.

### Community

Connect with other developers to discuss, share what you're building, and learn more in the [r/Spectacles](https://www.reddit.com/r/Spectacles/) community on Reddit.

---

## 2. How CLAD Works

> **URL:** https://developers.specs.com/docs/clad/overview-section/how-clad-works

# How CLAD Works

Exceptional experiences begin with prototyping and development, but the journey continues well beyond that. Once built, you need to test, optimize, publish, and learn from how people use your Lens.

CLAD (Closed Loop Agentic Development) automates and supports your entire experience development lifecycle, empowering you to move faster with AI as your co-developer.

> 📸 IMAGE — **CLAD lifecycle overview** (`pipeline.webp`)  
> A wide horizontal pipeline diagram showing the full CLAD development lifecycle in sequential stages: **Design & Prototype** → **Test** → **Optimize** → **Publish** → **Post-Production**. Each stage is a labeled box connected by arrows. The diagram communicates that CLAD is not just for initial building — it covers the entire journey from first idea to live product analytics.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-clad-works/pipeline.webp_

### Design & Prototype

> 📸 IMAGE — **Design and prototype loop** (`builder-flow.webp`)  
> A looping sub-flow diagram zooming into the Design & Prototype phase. It shows an inner loop between three steps: **Describe** (developer gives a natural-language prompt) → **Build** (AI generates scene objects, scripts, assets) → **Preview** (result appears live in Lens Studio preview panel). An arrow loops back from Preview to Describe, showing the iterative nature of this phase.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-clad-works/builder-flow.webp_

In this phase, CLAD will build out a starting point for your experience: building out the Lens scene, generating assets, writing scripts, and more.

> 📸 IMAGE — **Scene setup example** (`image10.png`)  
> A screenshot of Lens Studio with a SPECS scene being built. The Scene Hierarchy panel on the left shows objects being added (camera, world tracking, UI elements). The viewport in the center shows a 3D preview of the scene with the SPECS environment. This demonstrates the starting state of a fresh SPECS project with the necessary base objects already in place.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-clad-works/image10.png_

You can ask CLAD to quickly set up a scene by describing — in any level of detail — what you're looking for.

**Example prompt:** "create a bunch of planets to represent the solar system."

> 🎞️ GIF (animated) — **Solar system example** (`image15-cropped.gif`)  
> An animated GIF showing CLAD autonomously building a solar system Lens in Lens Studio. The animation shows: the AI adding sphere objects for planets one by one into the scene hierarchy, applying materials/textures to each planet (sun is yellow/orange, Earth is blue-green, etc.), then adding orbital animation scripts so the planets begin rotating around the sun in the preview panel. The preview panel updates in real time as each step completes.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-clad-works/image15-cropped.gif_

Though CLAD can build full experiences from scratch, it can also refine an existing project.

**Example prompt:** "add scripts or shaders to make the experience more engaging."

> 🎞️ GIF (animated) — **Engagement refinements** (`image14.gif`)  
> An animated GIF showing CLAD iterating on an existing Lens to add engagement features. The animation shows the AI analyzing the existing scene, then adding a shader to the sun to give it a glow/emission effect, adding particle trails to orbiting planets, and adding a tap interaction so that tapping a planet displays an info panel. Each change is visible in the live preview panel as it is applied.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-clad-works/image14.gif_

CLAD understands SPECS-specific capabilities. In this example, it's leveraging SPECS UI Kit and displays information from AI endpoints.

### Testing, Migration & Optimization

As the experience is being built, CLAD can simulate camera movement to see various perspectives, test interactions live in the preview, and iterate until behavior matches your intent.

> 📸 IMAGE — **Preview interaction during build** (`verify-flow.webp`)  
> A diagram showing the verify/preview feedback loop. It shows the AI writing code → the code compiling → the preview panel updating → the AI reading the preview output (screenshot + logs) → the AI deciding whether to accept or iterate. This flow diagram makes clear that CLAD does not just write code blindly — it checks its own output at each step.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-clad-works/verify-flow.webp_

> **Note:** Since AI will be building your Lens live in Lens Studio, you can watch along as it interacts with your Preview panel.

CLAD can also use LEAF (Lens Evaluation & Automation Framework), which allows AI to write its own scenario and integration tests for your Lens.

> **Tip:** Because these unit tests are written as scripts, you can run them as you continue to develop your Lens without relying on AI every time.

> 📸 IMAGE — **LEAF testing workflow** (`image13.png`)  
> A screenshot showing the LEAF panel open inside Lens Studio. The panel lists named test scenarios (e.g., "tap_button", "resize_object") with Run buttons next to each. The Logger panel at the bottom shows test output with PASSED/FAILED status messages. This demonstrates the LEAF UI that developers use to run automated tests directly in the editor.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-clad-works/image13.png_

> 📸 IMAGE — **Generated LEAF scenarios** (`image7.png`)  
> A screenshot of a TypeScript file open in VS Code / Lens Studio, showing CLAD-generated LEAF scenario code. The code shows a class extending `Scenario` with an `async run()` method that uses `DefaultLeafInteractor` to trigger buttons and asserts on resulting UI state. This demonstrates the actual test code CLAD writes automatically.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-clad-works/image7.png_

> 🎞️ GIF (animated) — **Automated LEAF test run** (`image3.gif`)  
> An animated GIF showing a LEAF test executing in the Lens Studio preview panel. The animation shows: the preview panel resets to a clean state → simulated hand/interaction inputs appear in the preview (visualized as cursor/hand indicators) → the interaction triggers a UI button → a result panel animates into view → the Logger at the bottom shows "PASSED" in green. This demonstrates the full automated test cycle with no human interaction required.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-clad-works/image3.gif_

CLAD can generate tests and run them automatically as it builds the Lens.

For example, if you are making a note-taking experience, AI will double-check that the code it wrote actually did what it intended.

You have access to what CLAD creates so that you can reuse and modify it.

For example, in the case of LEAF, you can run the generated scenarios through the LEAF panel directly.

In the testing phase, you can even simulate hand movements and gestures to ensure your interactions work as expected.

For example, here CLAD created a scenario in LEAF to test the two-hand pinch-and-drag to resize an object.

In addition to testing, CLAD will also help you optimize your Lens by looking at your existing assets, profiling performance, and applying targeted fixes.

Agentic optimization is a time-intensive, human-like process that systematically improves project performance while preserving visual parity.

> 📸 IMAGE — **Performance attribution chart** (`image4.png`)  
> A bar chart generated by CLAD's performance profiling agent. The chart shows frame time attribution broken down by system category (e.g., "Rendering", "Scripts", "Physics", "VFX") measured in milliseconds per frame (ms/frame). The tallest bar identifies the dominant performance bottleneck. This helps the developer (and the AI) understand where to focus optimization efforts.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-clad-works/image4.png_

> 📸 IMAGE — **Before and after optimization** (`image9.png`)  
> A side-by-side comparison screenshot. The left panel shows the Lens preview **before** optimization with a visible frame rate counter showing a lower FPS value. The right panel shows the same Lens **after** CLAD applied performance fixes, with a higher FPS. The visual appearance of the Lens is identical in both panels, demonstrating that optimization was achieved without visual regression.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-clad-works/image9.png_

If you have existing projects, CLAD can also bring them into SPECS. For example, it can migrate your existing Lens onto SPECS APIs and improve runtime performance.

> 📸 IMAGE — **Migration and FPS improvement** (`image5.png`)  
> A screenshot showing a Lens migration result. Lens Studio is open with a complex Lens that was originally built for Spectacles (2024). The UI shows a before/after FPS comparison, with the migrated version running at a noticeably higher frame rate on the SPECS 27 platform. The migration log in the output panel lists the deprecated APIs that were automatically updated.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-clad-works/image5.png_

> 🎞️ GIF (animated) — **Sand simulation on SPECS** (`image6.gif`)  
> An animated GIF showing a visually complex "Sand Simulation" Lens running on a SPECS device. The animation shows thousands of individual sand particles flowing and interacting with each other in real time, demonstrating high-performance native C++ code (SpecsNDK) running efficiently on the SPECS hardware. The sand responds to gravity and accumulates realistically.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-clad-works/image6.gif_

A complex Lens originally designed for Spectacles, brought to SPECS and running at a higher FPS on device after being optimized.

"A Sand Simulation simulating thousands of grains" running efficiently in C++, built and brought into SPECS through SpecsNDK using CLAD, running on device.

### Publishing

> 📸 IMAGE — **Publishing workflow** (`publish-flow.webp`)  
> A step-by-step diagram of the SPECS publishing process. It shows five labeled phases flowing left to right: **Validate** (check project settings, platform target) → **Build** (compile and package the Lens) → **Review** (pre-submission checklist) → **Submit** (upload to SPECS platform) → **Live** (Lens is discoverable in the SPECS community). Each step corresponds to a phase of the `/specs-publish` skill.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-clad-works/publish-flow.webp_

When you're ready, you can ask CLAD to publish your Lens for discovery in the SPECS community.

> **Note:** You will need a SPECS account to publish. Apply to the [SPECS Developer Program](https://developers.specs.com) to learn more. If you've built something cool with CLAD, you can also sign up to the [CLAD Device Access](https://developers.specs.com/clad-access) there to get queued for office hours and try it on a physical device.

### Post-Production

Once your Lens has been published, you can use CLAD to help you get insights on how it's being used, as well as opportunities to iterate.

> **Tip:** Learn what CLAD provides in each part of the process on [Agents and Skills](#3-agents-and-skills).

> **Tip:** CLAD can also write Editor code, allowing you to customize Lens Studio with plugins for a more tailored development workflow.

### SPECS Experience Builder

SPECS Experience Builder is an agent inside of the CLAD tool suite. The experience builder provides a structure for planning and building an entire interactive SPECS AR experience in one shot.

You can invoke SPECS Experience Builder by appending "Make ____ for SPECS".

> 📸 IMAGE — **Experience builder flow** (`image2.png`)  
> A screenshot of Cursor (the AI tool) executing the SPECS Experience Builder agent. The chat panel shows the AI systematically working through phases: planning the scene structure, generating 3D assets, writing TypeScript scripts, assembling the scene hierarchy, and running verification. The Lens Studio window is visible in the background, updating in real time as the AI works. This is a "one-shot" build in progress.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-clad-works/image2.png_

**Example prompt:** "Create a SPECS note taking lens"

> 📸 IMAGE — **Note-taking Lens example** (`image12.png`)  
> A screenshot of the finished note-taking Lens running in the Lens Studio SPECS preview. The Lens shows a floating world-space UI panel (using SPECS UI Kit) with a text input field (AR keyboard), a list of saved notes, and action buttons. The UI demonstrates voice recognition integration (microphone button) and persistent data storage. The scene is fully assembled and functional.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-clad-works/image12.png_

> 🎞️ GIF (animated) — **Chemistry education Lens** (`image16.gif`)  
> An animated GIF showing a chemistry education Lens built autonomously with CLAD. The animation shows a 3D periodic table in AR space — the user taps an element, and an info panel animates in showing the element's atomic structure (3D electron shell diagram), name, symbol, atomic number, and key properties. The UI uses SPECS UI Kit with a unique dark-themed design. The tap interaction, panel animation, and 3D model display all work seamlessly.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-clad-works/image16.gif_

An example chemistry education Lens made autonomously with CLAD, then iterated with humans in the loop. Notice that while the Lens uses the same SPECS UI Kit, it still has its unique flavor and design.

---

## 3. Agents and Skills

> **URL:** https://developers.specs.com/docs/clad/overview-section/agents-and-skills

# Agents and Skills

CLAD comes with many agents and skills that make it possible for an AI to build in a closed-loop, agentic development flow. Below we discuss some of the key agents and skills that make this possible.

> **Note:** The AI will usually pick up the right skills and agents automatically as it works — you don't have to name them. This page is provided so you can drive them explicitly when you'd like more control over a specific step.

> **Note:** This page has no images. All content is text-based skill and agent reference documentation.

### Example Workflow

There are many ways CLAD can empower your workflow — from helping you build autonomously, to helping you craft specific parts of your Lens.

#### Automatic end-to-end loop using SPECS Experience Builder

You can trigger the entire closed-loop agentic development end to end on its own by invoking the `specs-experience-builder` agent. This agent will plan and build an entire interactive SPECS AR experience on its own: it generates meshes, sound, music, UI, and icons, writes the scripts, and assembles the scene. After it builds, the loop verifies the result in the live preview and offers next steps — LEAF tests, optimization, publishing — and more!

```
build me an interactive solar system for SPECS
```

#### Do it yourself

If you're working on an existing project, or you only want to use certain parts of CLAD, you can trigger each part of CLAD individually. For example, you might trigger some of the following skills, agents, and more when creating a solar-system Lens for SPECS:

- `/scene-construction` — lay out the sun and planets orbiting it.
- `/lens-api` — make the planets orbit around the sun.
- `/build-mesh` — generate custom models (a rocket, an asteroid) to fly around the solar system.
- `/shader-graph` — make the sun glow realistically.
- `/specs-build-ui`, `/icon-selector`, `/font-selector` — on planet tap, show a panel with information about the planet.
- `/build-music` + `/build-sfx` — add an ambient soundtrack and tap sounds.
- `/verify-preview` — after each change, confirm that tapping a planet shows its info panel (read-only, during development).
- `live-lens-tester` (agent) — when you're ready to lock it in, it writes a re-runnable LEAF test for that tap-to-reveal interaction so future changes can't silently break it.

> **Tip:** `/lens-studio-field-notes` contains tips and tricks that help an AI agent succeed. Loading it early in your session gives the AI the context it needs to handle Lens Studio projects. (The router loads it for you automatically; you rarely invoke it by hand.)

> **Note:** Running the above is an illustrative workflow where you are driving the progress, working with AI, and using CLAD skills and agents to execute some tasks. SPECS Experience Builder will get into significantly more detail in order to achieve a one-shot.

### Specialist Agents

In addition to the overall SPECS Experience Builder agent, CLAD comes with specialists you might use while building your Lens. The three most valuable to know about:

- `script-author` — writes the TypeScript behavior code (and compile-checks it); doesn't touch the scene layout.
- `editor-api-specialist` — handles heavy, multi-step project edits, keeping the noise out of the main conversation.
- `specs-project-migrator` — upgrades an older Spectacles (2024) project to SPECS 27, separating auto-fixes from manual follow-ups.

The remaining specialists are spawned automatically by an orchestrator as part of the relevant step in the loop, and are called out in those sections below.

> **Tip:** Agents are useful because they can spawn within another context — so you keep your main context smaller and more compact!

### The Loop

Below we list some of the skills that the SPECS Experience Builder goes through when building a Lens end to end.

#### Getting Started & Setup

- `/lens-studio-router` — the front door for any LS task; checks readiness, picks the platform, routes to the right workflow.
- `/specs-project-init` — validate a SPECS project (camera, world tracking, required packages, preview device).
- `/ensure-package-installed` — verify a package is installed; install it (and its dependencies) from the Asset Library if missing.

> **Tip:** Before generating a fresh scene, `/reset-preview-environment` gives you a clean preview to build on — it recenters the camera, disables stray objects left over from a previous build, and captures a log baseline so you only read new output. It's safe and idempotent: it does not delete your scripts or assets and leaves the permanent environment (lighting, skybox, tracking) in place.

> **Note:** A few skills shell out to external tools (Node.js, ffmpeg, Blender) — each is called out inline on the skill that needs it. `/specs-project-init` probes for the optional ones and warns you when something a workflow needs is missing.

#### Design & Prototype Loop

- `/scene-construction` — the hub for adding and arranging objects (read → presets → apply → save).
- `/camera-and-rendering` — set up cameras, on-screen 2D content, and debug invisible objects.
- `/materials` — color, shininess, and textures via presets. The default "make it look like X."
- `/shader-graph` — custom surface looks no preset can do (glow, animated, procedural).
- `/vfx-graph` — particle effects: smoke, sparks, trails, magic.
- `/physics` — gravity, collisions, joints, draggable/throwable props; objects colliding with face/hand/world.
- `/build-mesh` — generate a finished 3D model from a text description (optionally animated). It picks from four peer backends per asset, by what the asset needs:
  - **SPECS text-to-3D** — the default for static props. Snap's hosted text-to-3D API (authenticated through your signed-in session, no API key); best texture fidelity, any style, and supports image→3D. Static only and asynchronous (create → poll → download, minutes per job).
  - **FAST3D** — faster static AI props, synchronous, no local dependencies; lower fidelity than SPECS. Used only when you explicitly ask for fast/draft meshes.
  - **Code-authored / procedural MeshBuilder** — build geometry from TypeScript at runtime (lathe, extrude, tube, skinned meshes); best for anything that must move, articulate, or be generated parametrically. Hands off to `/mesh-builder-scripting` and yields a TypeScript artifact instead of a GLB; zero pipeline latency, but a low realism ceiling (no canvas textures).
  - **Blender voxel** — a blocky voxel look, and the only backend that produces a rigged GLB (skinned skeleton). Needs Blender installed.
  - Requires Node.js for asset processing; the AI backends (SPECS, FAST3D) need Lens Studio sign-in with API access; the voxel / rigged-GLB backend needs Blender (optional — static AI meshes don't).
- `/mesh-builder-scripting` — build or reshape geometry from code at runtime (vs. the pre-made models of `/build-mesh`).
- `/lens-package-toolkit` — install, unpack, inspect, and author reusable Lens Studio packages.
- `/update-lens-packages` — update libraries (SIK, UI Kit, Sync Kit) to their latest versions (or a pinned version when you ask for one).

##### Scripting & Editor Automation

- `/lens-api` — writing TypeScript that runs inside a live Lens (events, taps, screen-to-world, runtime objects).
- `/editor-api` — code that automates the Lens Studio editor for bulk edits (a different runtime — never mix the two).
- `/lens-studio-field-notes` — the shared "house rules" loaded automatically by the router (mostly behind the scenes).

##### UI & Typography

- `/specs-build-ui` — world-space UI panels for SPECS (HUDs, menus, sliders, switches, text inputs).
- `/font-selector` — search fonts by mood or name and apply to text.
- `/icon-selector` — find and import the right Material icon for a button or panel.

> **Tip:** `/specs-build-ui` consumes icons and fonts — it doesn't generate them. Run `/icon-selector` and `/font-selector` first; the UI skill then reads the icons on disk and the font path you pass in. (The orchestrator enforces this order: icons and fonts before UI.)

##### Hand Interaction & Input

- `/specs-interaction-recipes` — the playbook for hand actions: pinch, hover, grab, swipe, throw, custom gestures.
- `/specs-keyboard` — show an AR keyboard for text input (text, URL, numpad, phone).
- `/specs-asr` — real-time speech-to-text (40+ languages); great for dictation and voice → AI chat.

> **Tip:** `/specs-build-ui` and `/specs-interaction-recipes` cover two different layers. UI panels, buttons, and dialogs (anything flat the user reads or taps) belong to `/specs-build-ui` — a UIKit Button already handles its own tap. Hand gestures on 3D objects (grab a planet, throw a ball) belong to `/specs-interaction-recipes`. They connect through an event bus: the UI module emits events your main script subscribes to. Don't hand-roll a button with a collider — that's the anti-pattern the builder guards against.

##### Audio

- `/build-music` — compose original music: melodies, beats, jingles. Offline, license-clean.
  - Requires Node.js; uses ffmpeg (if present) to verify the track isn't silent — without ffmpeg it still renders, just skips that check.
- `/build-sfx` — generate sound effects: clicks, impacts, whooshes, ambient textures, 8-bit.
  - Requires Node.js.
- `/specs-audio` — how sound plays on-device: power-saving vs. low-latency, Snap recording, mic input.

##### SPECS Platform Capabilities

- `/specs-ai-remote-service` — connect to AI services via the Remote Service Gateway (RSG). It fronts several providers, picked by what you're building:
  - **Gemini** — text / multimodal chat. For image generation use the Imagen endpoint.
  - **OpenAI** — chat completions and Realtime voice.
  - **Snap3D** — AI image / 3D generation.
  - Key split: chat-completions + ASR (hold-to-talk; simpler wiring, just mic + RSG) vs Gemini Live / OpenAI Realtime (full live voice — needs the websocket + dynamic-audio hierarchy).
- `/specs-camera` — access camera frames for computer vision, AR overlays, and ML/AI.
- `/specs-depth` — per-pixel depth for correct-distance placement and occlusion.
- `/specs-world-query` — ray-cast to find real surfaces (floor, table, wall) and drop objects on them.
- `/specs-location` — GPS, heading, and Snap Places for outdoor and map-based AR.
- `/specs-custom-locations` — anchor content to one scanned real-world place.
- `/specs-snap-cloud` — cloud backend (Supabase) for saved data, leaderboards, uploads, edge functions.
- `/specs-sync-kit` — shared multiplayer / colocated experiences synced across people.
- `/specs-internet` — HTTP requests and downloading remote media (images, video, audio, glTF).
- `/specs-websocket` — persistent two-way connections for live feeds and streaming.
- `/specs-spatial-image` — turn a 2D photo into a viewable 3D depth image.
- `/specs-ndk` — add a native C++ module for advanced, high-performance code (engineers only).
  - Requires CMake, Python 3, and a C++ toolchain. Also needs the Google Cloud SDK only as a fallback — if downloading the SpecsNDK toolchain returns a 401/403 it installs gcloud and runs `gcloud auth login` to authorize; the default download is anonymous and needs no gcloud.

> **Agent:** After a multiplayer build with `/specs-sync-kit`, the `specs-sync-kit-validator` agent runs a read-only structural check for the common setup mistakes (leftover sample content, wrong start mode, misplaced game content, missing camera tracking) and reports concrete fixes.

#### Testing, Migration & Optimization Loop

##### Debugging

- `/lens-debug` — start here for bugs. Describe the symptom; it routes you to the right specialist.
- `/specs-debug` — add-on layer for SPECS-only bugs (SIK, AI gateway, sync, tracking, world-space UI).
- `/lens-log-analysis` — how to read the logs correctly (a clean compile ≠ the Lens actually ran).
- `/lens-js-debugger` — interactive debugger: breakpoints, step, inspect live values.
- `/preview-inspection` — query the live scene: find objects, read transforms, capture a render.
- `/specs-preview-interaction` — drive the preview with simulated hand actions (pinch, drag, tap) to test behavior, no glasses needed. The action-driving sibling of `/preview-inspection`.
- `/verify-preview` — confirm an edit produced the behavior you expected. Read-only; use after each change.

> **Tip:** `/verify-preview` runs inline in the main agent, with full code context — it recompiles, captures the running preview, can drive an interaction and check the logs, then judges the result against what the code should do. It keeps the main context lean by being a tight, focused pass (and can offload bulk screenshots to an ad-hoc helper under context pressure).

##### Testing with LEAF

LEAF lets you instrument your Lens for testing. You can create repeatable scenarios that run to make sure the pieces of your Lens continue to work. CLAD can create and run LEAF scenarios automatically!

- `/specs-leaf-install-packages` — install the LEAF framework before writing or running tests.
- `/specs-leaf-write-scenarios` — author and attach automated test scenarios for a Lens.
- `/specs-leaf-run-in-preview` — run those scenarios in the preview panel; the fastest iteration loop.

To learn more about LEAF, including how to install it and write scenarios yourself, see [Test Your Lens With LEAF](#9-tools--test-your-lens-with-leaf).

> **Tip — `/verify-preview` vs. LEAF:** While building, use `/verify-preview` for quick "did my last edit work?" checks — it writes nothing and is the right tool most of the time. When the experience is far enough along that you want protection against regressions, use the `live-lens-tester` agent (or the LEAF skills directly) to write a persistent, re-runnable test suite. Rule of thumb: building → `/verify-preview`; locking in → LEAF.

##### Optimizing

- `/specs-capture-perf-trace` — record a `.pftrace` from one or more preview panels.
- `/perfetto-trace-analysis` — analyze a trace to find frame drops and jank, with honest confidence levels.
- `/specs-lens-perf-attribution` — pin down which system eats frame time (ms/frame) and produce a plan.
- `/specs-lens-perf-optimize` — apply the recommended fixes one at a time, verifying and committing each.
- `/specs-optimize-lens-mesh` — cut draw calls by merging same-material meshes and decimating geometry.

> **Agents:** `/specs-lens-perf-optimize` drives two worker agents in a loop — `perf-attribution-runner` measures where frame time goes (ms/frame per system), and `perf-fix-applicator` applies one undoable fix at a time with before/after capture. Both are spawned automatically; you just invoke the skill.

##### Migration

- `/specs-27-migration` — migrate an older Lens to the SPECS 27 APIs (updates deprecated features).

#### Publishing

- `/specs-publish` — take a SPECS Lens to "submitted for review" in five guided phases.

---

## 4. Setup — Setup Lens Studio

> **URL:** https://developers.specs.com/docs/clad/setup/setup-lens-studio

# Setup Lens Studio

> **Note:** Lens Studio version **5.22** or later is required. [Download Lens Studio](https://ar.snap.com/download).

Here's how to create a new SPECS project for CLAD to work inside:

1. Open Lens Studio.
2. On the Lens Studio home page, select **SPECS**.

> 📸 IMAGE — **Select SPECS on the Lens Studio home page** (`image1.png`)  
> A screenshot of the Lens Studio home screen / project creation page. The screen shows a grid of platform options including "SPECS", "Spectacles", "Camera", etc. The "SPECS" option is highlighted/selected, indicated by a colored border or checkmark. This is the very first step when creating a new project — choosing the SPECS platform target.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/setup-lens-studio/image1.png_

3. Select **Base Template**.

> 📸 IMAGE — **Select the Base Template** (`image3.png`)  
> A screenshot showing the template selection screen after choosing SPECS. A list or grid of project templates is displayed. The "Base Template" option is highlighted — it is the minimal starting project, providing only the essential SPECS camera setup and world tracking. Other templates may also be visible (e.g., "Hand Tracking", "World Mesh") but Base Template is the recommended starting point for CLAD.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/setup-lens-studio/image3.png_

4. Save the project to your machine by selecting **File > Save As** from the toolbar.

> 📸 IMAGE — **Save the project with File > Save As** (`image2.png`)  
> A screenshot of Lens Studio with the File menu open, showing "Save As" highlighted. A system file-picker dialog may also be visible. This step is critical — CLAD's AI tools need the project to be saved to disk because the `mcp.json` file (which enables MCP server auto-discovery) is only created once the project has a file path on disk.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/setup-lens-studio/image2.png_

Your project is now set up to target SPECS. Next, connect an AI coding tool to Lens Studio. We have guides for [Claude Code](#5-setup-ai--claude-code-setup), [Codex](#6-setup-ai--codex-setup), and [Cursor](#7-setup-ai--cursor-setup).

> **Tip:** If your AI does not have a guide, try providing the contents of one of the guides to your agent.

---

## 5. Setup AI — Claude Code Setup

> **URL:** https://developers.specs.com/docs/clad/setup/setup-ai/claude-code-setup

# Claude Code Setup

Use this guide to connect Claude Code to Lens Studio, install the CLAD Lens Studio plugin, and start building a SPECS Lens.

### Before You Start

Before you start, make sure:

1. A Lens Studio project prepared for SPECS is open in the Lens Studio editor — [Setup Lens Studio](#4-setup--setup-lens-studio).
2. A terminal is open in the Lens Studio project folder — [Open Project in CLI](#14-additional-guides--open-project-in-cli).

> **Note:** The order of these setup steps matter. Lens Studio must be opened first so that it can create an MCP for the terminal to auto-connect to.

### Install Claude Code

Please review Claude Code's documentation on how to install Claude Code to CLI: https://claude.com/product/claude-code

**macOS (using Bash/Zsh)**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows (using PowerShell)**

```powershell
irm https://claude.ai/install.ps1 | iex
```

### Start Claude Code

> **Note:** Use **Claude Code** in the CLI for this guide, not **Claude for Mac**. You may use Claude for Mac after you complete the steps in this guide.

The doc shows a side-by-side visual comparison of the two interfaces:

> 📸 IMAGE — **Claude Code prompt with only `>`** (`claude-prompt.webp`) — *left side of comparison*  
> A screenshot of a terminal window running Claude Code CLI. The prompt shows only a single `>` character with no path prefix — this is the Claude Code interactive prompt, ready to accept slash commands like `/plugin` and `/mcp`. The background is a dark terminal. This visual helps users distinguish Claude Code's prompt from a regular terminal prompt.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/setup-ai/claude-prompt.webp_

> 📸 IMAGE — **Claude for Mac application window** (`claude-for-mac.jpg`) — *right side of comparison*  
> A screenshot of the Claude for Mac desktop application. It shows the standard Claude chat UI with a message input box at the bottom, conversation history in the center, and the Claude logo/branding. This is the GUI Mac app — **not** the CLI tool. The image is shown to contrast with Claude Code so users don't confuse the two.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/setup-ai/claude-for-mac.jpg_

> **Note:** It's important to call Claude in your Lens Studio's project folder. The project folder contains an `mcp.json` which tells Claude that Lens Studio provides an MCP server for it to connect to. This MCP server is per Lens Studio window. It is possible for you to open multiple Lens Studio Windows and open Claude in each project folder and have them operate on each individually.

From your Lens Studio project folder, start Claude Code in CLI:

```
claude
```

> 📸 IMAGE — **Claude Code trust folder prompt** (`image1.webp`)  
> A screenshot of Claude Code displaying a "Do you trust this folder?" security prompt in the terminal. The message warns that the project folder contains an `mcp.json` configuration file. Two options are shown: "Yes, I trust this folder" and "No". The "Yes, I trust this folder" option should be selected to allow Claude Code to load the Lens Studio MCP server configuration.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/setup-ai/image1.webp_

> 📸 IMAGE — **Approve the Lens Studio MCP server** (`image2.webp`)  
> A screenshot of Claude Code displaying a prompt asking whether to approve the Lens Studio MCP server. The message reads something like "This project has configured an MCP server: lens-studio. Would you like to use it?" with an option "Use this and all future MCP servers in this project". This should be selected to establish the MCP connection to Lens Studio.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/setup-ai/image2.webp_

### Install the plugin marketplace

The following commands are for Claude Code, not terminal. To verify you are typing into Claude Code, ensure that the line you are typing does not come after a path.

The doc shows another side-by-side comparison:

> 📸 IMAGE — **Claude Code prompt (left) vs Terminal prompt (right)** (`claude-prompt.webp` + `terminal.webp`)  
> Two side-by-side screenshots. Left: Claude Code shows only `>`. Right: a regular terminal shows a full path prefix like `C:\Users\diego\Documents\MyProject >` before the cursor. This comparison teaches users to verify they are in Claude Code (not a terminal) before running slash commands.  
> _Asset URL (Claude Code side): https://developers.specs.com/docs-static/static/clad/setup-ai/claude-prompt.webp_  
> _Asset URL (Terminal side): https://developers.specs.com/docs-static/static/clad/setup-ai/terminal.webp_

For the most up-to-date installation steps, please refer to the ls-extensions repository readme: https://github.com/lens-studio-devs/ls-extensions

> 📸 IMAGE — **ls-extensions readme install steps** (`image4.webp`)  
> A screenshot of the GitHub repository page for `lens-studio-devs/ls-extensions`, showing the README.md content. The README displays the installation commands for different AI tools (Claude Code, Codex, Cursor). The relevant section for Claude Code is visible, showing the `/plugin marketplace add` command. This is referenced so users can always find the most up-to-date commands directly from the source.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/setup-ai/image4.webp_

In Claude Code, add the ls-extensions plugin marketplace:

```
/plugin marketplace add git@github.com:lens-studio-devs/ls-extensions.git
```

### Install the CLAD plugin

```
/plugin install ls-clad@ls-extensions
```

### Verify Plugin Installation

```
/plugin
```

> 📸 IMAGE — **CLAD plugin shown in the Installed tab** (`image6.webp`)  
> A screenshot of the Claude Code plugin menu, open to the "Installed" tab. The list shows "Lens Studio CLAD" (ls-clad) as an installed plugin with a checkmark or enabled indicator. Other plugins may also be listed. This confirms the CLAD plugin was successfully installed and is active in Claude Code.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/setup-ai/image6.webp_

### Verify MCP Connection

```
/mcp
```

> 📸 IMAGE — **Lens Studio MCP server connected** (`image7.webp`)  
> A screenshot of the Claude Code `/mcp` command output. It shows a list of connected MCP servers with "lens-studio" listed and showing a green connected status indicator (or "connected" text). The server entry may show the number of available tools (e.g., "42 tools"). This confirms the AI can communicate with Lens Studio.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/setup-ai/image7.webp_

### Enable Auto Mode

To avoid approving many individual permissions:

- Press Shift + Tab until you see the auto mode option.
- Press Enter to confirm auto mode.

> 📸 IMAGE — **Enabling auto mode in Claude Code** (`image8.webp`)  
> A screenshot of the Claude Code interface showing the mode selector at the bottom of the terminal. The options cycle through different approval modes. "Auto" mode is highlighted/selected — in this mode, Claude Code executes all tool calls (including MCP calls to Lens Studio) without asking for individual approval each time. This is necessary for CLAD to operate autonomously during a long build session.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/setup-ai/image8.webp_

### Start Building!

Ask Claude Code to build a SPECS Lens. Example prompt:

```
Can you please build me a periodic table SPECS Lens showing the atomic structure of various elements?
```

### Await Completion

Let Claude Code work. A full Lens build can take 30+ minutes.

---

## 6. Setup AI — Codex Setup

> **URL:** https://developers.specs.com/docs/clad/setup/setup-ai/codex-setup

# Codex Setup

Use this guide to connect Codex to Lens Studio, install the CLAD Lens Studio plugin, and start building a SPECS Lens.

### Before You Start

Before you start, make sure:

1. A Lens Studio project prepared for SPECS is open in the Lens Studio editor — [Setup Lens Studio](#4-setup--setup-lens-studio).
2. A terminal is open in the Lens Studio project folder — [Open Project in CLI](#14-additional-guides--open-project-in-cli).

> **Note:** The order of these setup steps matter. Lens Studio must be opened first so that it can create an MCP for the terminal to auto-connect to.

### Install Codex

Please review Codex documentation on how to install Codex CLI: https://chatgpt.com/codex/

```
codex --version
```

**Windows (PowerShell)**

```powershell
irm https://chatgpt.com/codex/install.ps1 | iex
```

### Start Codex

```
codex
```

> 📸 IMAGE — **Codex trust folder prompt** (`image5.webp`)  
> A screenshot of Codex CLI displaying a security/trust prompt when launched in the project folder. It asks the user to confirm they trust the current directory before proceeding. The option "Yes, continue" should be selected. This is equivalent to Claude Code's trust folder prompt.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/codex-setup/image5.webp_

### Install the plugin marketplace

The doc shows a side-by-side comparison:

> 📸 IMAGE — **Terminal prompt (left) vs Codex prompt (right)** (`terminal.webp` + `codex-prompt.webp`)  
> Two side-by-side screenshots. Left: a regular terminal showing a full path prefix like `C:\Users\diego\Documents\MyProject >`. Right: Codex's interactive prompt showing only a single `>` character. This helps users verify they are in Codex (not a terminal) before running plugin commands.  
> _Asset URL (Terminal side): https://developers.specs.com/docs-static/static/clad/codex-setup/terminal.webp_  
> _Asset URL (Codex side): https://developers.specs.com/docs-static/static/clad/codex-setup/codex-prompt.webp_

> 📸 IMAGE — **ls-extensions readme install steps** (`image7.webp`)  
> A screenshot of the `lens-studio-devs/ls-extensions` GitHub README showing the installation instructions for Codex. The Codex-specific command (`codex plugin marketplace add git@github.com:lens-studio-devs/ls-extensions.git`) is visible.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/codex-setup/image7.webp_

In Codex, add the ls-extensions plugin marketplace:

```
codex plugin marketplace add git@github.com:lens-studio-devs/ls-extensions.git
```

Alternatively, add the marketplace through the Codex UI:

1. In Codex, enter `/plugins`.

> 📸 IMAGE — **Open the Codex plugins menu** (`image4.webp`)  
> A screenshot of the Codex interactive UI after entering `/plugins`. A menu panel appears showing tabs or sections for "Installed", "Marketplace", and "Add Marketplace". The UI is overlaid on top of the terminal. This shows where to navigate to add a new marketplace source.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/codex-setup/image4.webp_

2. Navigate to the Add Marketplace section, then select "Add marketplace".

> 📸 IMAGE — **Add marketplace in Codex** (`image1.webp`)  
> A screenshot of the Codex plugins UI on the "Add Marketplace" screen. There is an input field for entering a marketplace URL, and an "Add marketplace" button. The UI is waiting for the user to enter the `git@github.com:lens-studio-devs/ls-extensions.git` URL.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/codex-setup/image1.webp_

3. Enter the Marketplace URL:

```
git@github.com:lens-studio-devs/ls-extensions.git
```

> 📸 IMAGE — **Enter the Lens Studio extensions marketplace URL** (`image2.webp`)  
> A screenshot of the Codex plugin marketplace URL input field with the `git@github.com:lens-studio-devs/ls-extensions.git` URL already typed in. A confirm/submit button is visible. This shows the completed state before adding the marketplace.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/codex-setup/image2.webp_

### Install the CLAD plugin

> 📸 IMAGE — **ls-extensions marketplace in Codex** (`image10.webp`)  
> A screenshot of the Codex plugins UI showing the `[ls-extensions]` marketplace section after it has been added. The marketplace lists available plugins, with "ls-clad" (Lens Studio CLAD) shown as an installable plugin. An option "Press Enter to install or view plugin details" is visible next to it.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/codex-setup/image10.webp_

> 📸 IMAGE — **Install ls-clad in Codex** (`image6.webp`)  
> A screenshot of the Codex plugin detail screen for ls-clad. The plugin name "Lens Studio CLAD", a brief description, and an "Install this plugin now" button are shown. This is the confirmation screen just before the plugin gets installed.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/codex-setup/image6.webp_

### Verify Plugin Installation

```
/plugins
```

> 📸 IMAGE — **CLAD plugin shown in the Installed tab** (`image3.webp`)  
> A screenshot of the Codex `/plugins` menu on the Installed tab. "ls-clad" (Lens Studio CLAD) is listed as an installed plugin with a checkmark indicating it is active.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/codex-setup/image3.webp_

### Verify MCP Connection

```
/mcp
```

> 📸 IMAGE — **Connected MCP servers in Codex** (`image9.webp`)  
> A screenshot of the Codex `/mcp` command output showing the list of connected MCP servers. "lens-studio" appears in the list with a connected status. This confirms Codex can communicate with Lens Studio via MCP.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/codex-setup/image9.webp_

### Enable Auto-Approval Mode

```
codex config set approval_policy "on-request" && codex config set approvals_reviewer "auto_review"
```

### Start Building!

```
Using SPECS experience builder, can you please build me a periodic table SPECS Lens showing the atomic structure of various elements?
```

> **Note:** Codex performs best when you use the phrase "Using SPECS experience builder" in your prompt.

### Await Completion

Let Codex work. A full Lens build can take 30+ minutes.

---

## 7. Setup AI — Cursor Setup

> **URL:** https://developers.specs.com/docs/clad/setup/setup-ai/cursor-setup

# Cursor Setup

Use this guide to connect Cursor to Lens Studio, install the CLAD Lens Studio plugin, and start building a SPECS Lens.

### Before You Start

1. A Lens Studio project prepared for SPECS is open in the Lens Studio editor — [Setup Lens Studio](#4-setup--setup-lens-studio).
2. A terminal is open in the Lens Studio project folder — [Open Project in CLI](#14-additional-guides--open-project-in-cli).

### Install Cursor

https://cursor.com/home

```
cursor --version
```

### Start Cursor

```
cursor
```

### Install the plugin marketplace

> 📸 IMAGE — **ls-extensions readme install steps** (`image1.webp`)  
> A screenshot of the `lens-studio-devs/ls-extensions` GitHub README showing the Cursor-specific installation instructions. The section visible shows the `git clone` command and the `cp` / `Copy-Item` commands for placing the plugin into Cursor's plugin directory.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/cursor-setup/image1.webp_

Clone the ls-extensions marketplace repository locally:

```
git clone git@github.com:lens-studio-devs/ls-extensions.git
```

### Install the CLAD plugin

**macOS / Linux:**

```bash
mkdir -p ~/.cursor/plugins/local
cp -R ls-extensions/plugins/ls-clad ~/.cursor/plugins/local/ls-clad
```

**Windows (PowerShell):**

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.cursor\plugins\local" | Out-Null
Copy-Item -Recurse -Force ls-extensions\plugins\ls-clad "$env:USERPROFILE\.cursor\plugins\local\ls-clad"
```

### Confirm Plugin Installation

1. In Cursor, select **Cursor > Settings > Cursor Settings**.

> 📸 IMAGE — **Open Cursor Settings** (`image2.webp`)  
> A screenshot of Cursor's application menu bar open on macOS or Windows, with the path **Cursor > Settings > Cursor Settings** highlighted. This shows the exact navigation path to reach Cursor's settings panel where plugins and MCP servers are managed.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/cursor-setup/image2.webp_

2. Select **Plugins** in the vertical menu to confirm **Ls Clad** shows up.

> 📸 IMAGE — **Ls Clad plugin in Cursor** (`image5.webp`)  
> A screenshot of the Cursor Settings panel open on the "Plugins" section. A list of installed plugins is shown, and "Ls Clad" appears in the list with an enabled toggle/checkmark. This confirms the CLAD plugin was correctly copied to Cursor's plugin directory and is recognized by the editor.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/cursor-setup/image5.webp_

### Verify MCP Connection

1. In Cursor, select **Cursor > Settings > Cursor Settings**.

> 📸 IMAGE — **Open Cursor Settings** (`image2.webp` — repeated)  
> Same screenshot as above showing the Cursor Settings navigation path.

2. Select the toggle beside **lens-studio** to enable the MCP.

> 📸 IMAGE — **Enable the lens-studio MCP server** (`image4.webp`)  
> A screenshot of the Cursor Settings panel on the MCP or AI Tools section. A list of available MCP servers is shown, and "lens-studio" appears in the list with a toggle switch. The toggle is being set to the ON/enabled position. Once enabled, Cursor can use Lens Studio's MCP tools in its agent mode.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/cursor-setup/image4.webp_

### Enable Run Everything

1. In Cursor, select **Cursor > Settings > Cursor Settings**.
2. In the **Agents** section, set **Run Mode** to **Run Everything**.

> 📸 IMAGE — **Run Mode set to Run Everything** (`image3.webp`)  
> A screenshot of the Cursor Settings panel in the "Agents" section. A "Run Mode" dropdown selector is visible and is set to "Run Everything". This setting allows Cursor's agent to execute all tool calls (including Lens Studio MCP calls) without requesting approval for each individual action, enabling CLAD to work autonomously.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/cursor-setup/image3.webp_

### Start Building!

```
Can you please build me a periodic table SPECS Lens showing the atomic structure of various elements?
```

### Await Completion

Let Cursor work. A full Lens build can take 30+ minutes.

---

## 8. Tools — JavaScript Debugger

> **URL:** https://developers.specs.com/docs/clad/tools/javascript-debugger

# JavaScript Debugger

Attach an external JavaScript debugger to pause and inspect your Lens script in Lens Studio and on SPECS.

> **Tip:** In addition to using the debugger with your code editor, you can have CLAD drive the debugger for you with the `/lens-js-debugger` skill — or just by asking the AI to "use the debugger". See [Agents and Skills](#3-agents-and-skills) for the full set.

### Compatibility

Supported targets: SPECS device, Lens Studio preview panels (SPECS 27, No Simulation, Horizontal).  
Supported debug clients: VS Code, Cursor, and other VS Code forks.

### Usage

1. Open the same project in Lens Studio and VS Code.
2. Navigate to the **Run and Debug** tab in VS Code.

> 📸 IMAGE — **Run and Debug tab in VS Code** (`image1.webp`)  
> A screenshot showing a very small icon — the VS Code activity bar on the left side with the "Run and Debug" icon (a play button with a bug symbol) highlighted. This is the tab that needs to be opened to access the debug launch configurations for attaching to a running Lens.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/javascript-debugger/image1.webp_

3. Press **Attach to running Lens (Lens Studio)**.

> 📸 IMAGE — **Attach to running Lens launch configuration** (`image2.webp`)  
> A screenshot of VS Code's Run and Debug panel showing the launch configuration dropdown. The option "Attach to running Lens (Lens Studio)" is selected/visible in the dropdown. A green play button is next to it. This is the specific launch config that was auto-generated by the Lens Studio JS debug integration.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/javascript-debugger/image2.webp_

4. Select the target to attach from the list.

> 📸 IMAGE — **Selecting a debug target from the list** (`image3.webp`)  
> A screenshot of VS Code showing a Quick Pick dropdown listing the available debug targets. Each entry represents a running Lens Studio preview panel or SPECS device. Entries might be labeled "SPECS 27 Preview" or "Device: SPECS". The user clicks one to attach the debugger to that specific target.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/javascript-debugger/image3.webp_

5. Enjoy a proper debugging experience — pause on breakpoints, explore the call stack, watch variables, and more.

> 📸 IMAGE — **Debug controls for the attached Lens** (`image4.webp`)  
> A screenshot of VS Code with the JavaScript debugger attached to a running Lens. The debug toolbar at the top shows the standard controls: Continue (F5), Step Over (F10), Step Into (F11), Step Out (Shift+F11), Restart, Stop. The Variables panel on the left shows the current scope with inspectable JavaScript variables from the Lens script. A breakpoint is hit and the current line is highlighted in the TypeScript source file.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/javascript-debugger/image4.webp_

### SPECS-specific Considerations

> 📸 IMAGE — **Send to SPECS for Debugging option** (`image5.webp`)  
> A screenshot of Lens Studio showing a dropdown or context menu with the option "Send to SPECS for Debugging" highlighted. This is distinct from the regular "Send to SPECS" button. The regular send flow compiles to optimized bytecode (no debug info). The "for Debugging" option keeps the JavaScript source and debug symbols intact so VS Code can attach and show breakpoints.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/javascript-debugger/image5.webp_

- **Important:** You must use the **Send to SPECS for Debugging** option (not the regular Send to SPECS).
- The normal **Send to SPECS** flow sends optimized bytecode instead of JS, with no debug info available.
- It is not currently possible to reload a Lens on SPECS while keeping the debug session alive.
- Only one Lens Studio instance at a time is supported.

---

## 9. Tools — Test Your Lens With LEAF

> **URL:** https://developers.specs.com/docs/clad/tools/test-your-lens-with-leaf

# Test Your Lens With LEAF

> **Note:** This page has no images. All content is code samples and text documentation.

LEAF is an automated testing framework for SPECS Lenses. It lets you define repeatable test scenarios, simulate user interactions such as hand input, gestures, and ray-based targeting, and catch bugs in your Lens's workflows. The result is less manual testing and more reliable releases.

> **The easiest way to use LEAF is through CLAD**, which automates the process of installing, authoring, and running scenarios for your Lens:
> - **`/specs-leaf-install-packages`**: installs the LEAF framework.
> - **`/specs-leaf-write-scenarios`**: authors test scenarios for your Lens.
> - **`/specs-leaf-run-in-preview`**: runs the scenarios.

### Understand the Building Blocks

| Concept | What it is |
|---|---|
| Scenario | A scenario is essentially a test. Specifically, it is a class extending `Scenario` with an async `run()` method containing interactions and assertions. |
| Scenario index | A registry that maps a scenario ID to its file and optional parameters, allowing the framework to discover and run scenarios by ID. |
| Interactor | A simulated input source that drives your Lens. |
| Assertions | `expect(...)` checks inside `run()`. A failed assertion, or any thrown error, fails the scenario. |

#### Available interactors

1. **`DefaultLeafInteractor`** simulates generic input through a SIK interactor and can trigger, drag, and hover any SIK interactable. It is the simplest interactor.
2. **`LeafHandInteractor`** simulates hand input with individually accessible hands for the left and right side. In addition, this interactor provides access to the `Hand`, which can perform various gestures as well through `hand.makeGesture(gesture)`. Supported gestures are fist, pinch, palm, backhand, and relaxed.
3. **`IkBodyInteractor`** simulates full-body inverse kinematics and can be used for the most realistic interactions.

If the available interactors don't cover all your interaction needs, you can always create your own custom interactor as well.

### Before You Start

1. Your Lens Studio project targets SPECS.
2. Your Lens uses Spectacles Interaction Kit (SIK) interactables for the interactions you want to test.
3. The Lens Studio project is open in the Lens Studio editor.

### Install LEAF

1. In Lens Studio, open the Asset Library.
2. Search for **Leaf** and import it into your project.
3. Confirm that `Leaf.lspkg` appears in your Asset Browser.

> **Tip:** with CLAD, run `/specs-leaf-install-packages` instead.

### Write a Scenario

```typescript
import { Scenario } from "Leaf.lspkg/Scenarios/scenario/Scenario";
import { DefaultLeafInteractor } from "Leaf.lspkg/Interactors/interactor/DefaultLeafInteractor";
import { findInteractableByName } from "Leaf.lspkg/Interactors/InteractableUtils";
import { findSceneObjectByName } from "Leaf.lspkg/Utils/common/Utils";
import { expect } from "Leaf.lspkg/Utils/common/Expect";

@component
export class TapButtonScenario extends Scenario {
  async run(): Promise<void> {
    const interactor = new DefaultLeafInteractor();
    const button = findInteractableByName("PrimaryButton");
    expect(button).toBeTruthy();
    await interactor.trigger(button);
    const label = findSceneObjectByName("StatusLabel").getComponent("Text").text;
    expect(label).toBe("Pressed");
  }
}
```

#### Core interactions

| Method | What it simulates |
|---|---|
| `trigger(target)` | Targets and triggers an interactable. |
| `drag(target, dragVector, dragDurationMs)` | Triggers an interactable, then drags it along a specified vector for a given duration (in milliseconds). |
| `hover(target, hoverDurationMs?)` | Targets and hovers over an interactable for a given duration (in milliseconds, optional and defaults to 200ms). |

#### Assertions and utilities

```typescript
const label = findSceneObjectByName("StatusLabel").getComponent("Text").text;
expect(label).toBe("Pressed");
```

`expect()` supports: `toBe`, `toEqual`, `toBeCloseTo`, `toBeGreaterThan`, `toBeLessThan`, `toBeTruthy`, `toBeFalsy`, `toBeNull`, and `.not` to invert any of them.

Utilities include: `findSceneObjectByName`, `findInteractableByName`, `findInScene`, `nextFrame()`, `sleep(ms)`.

### Register Your Scenarios

```typescript
import { scenariosIndex } from "Leaf.lspkg/Scenarios/decorator/ScenarioIndexDecorator";
import { ScenarioMetadata } from "Leaf.lspkg/Scenarios/scenario/ScenarioMetadata";
import { TapButtonScenario } from "./TapButtonScenario";

@component
export class LeafIndex extends BaseScriptComponent {
  @scenariosIndex
  static scenariosIndex: ScenarioMetadata[] = [
    {
      id: "tap_button",
      typename: TapButtonScenario.getTypeName(),
    },
  ];
}
```

### Run Scenarios in the Preview

1. In Lens Studio, open the LEAF panel.
2. Reset the Preview to ensure that the Lens starts from a clean state.
3. Select a scenario from the list and run it.
4. Watch the preview — simulated interactions play out against your Lens.

> **Tip:** with CLAD, run `/specs-leaf-run-in-preview`.

### Read the Results

- PASSED = scenario completed `run()` without throwing.
- FAILED = scenario threw (failed `expect`, missing interactable, or timeout), shown with the error in the Logger.

### Quick Checklist

- `Leaf.lspkg` is in your Asset Browser.
- Your scenario class extends `Scenario`, and every async call inside `run()` is awaited.
- The scenario is registered in a `@scenariosIndex` index attached to the scene.
- The scenario appears in the LEAF panel and runs in the preview.
- The Logger shows PASSED, and shows FAILED when you intentionally break an assertion.

### Important Considerations

- Always `await` async calls inside `run()`. Un-awaited failures are silently swallowed.
- If an interactable is not found, the interactor throws and the scenario fails. Prefer stable SceneObject names.
- `trigger` waits for trigger events to fire; `drag` runs for the full duration. Use `nextFrame()` or `sleep(ms)` when your Lens needs time to react.
- LEAF simulates SIK interactors only. Raw touch events or custom gesture code need custom Interactors.
- Building → `/verify-preview`; locking in → LEAF.

---

## 10. Troubleshooting — Troubleshoot Lens Studio MCP

> **URL:** https://developers.specs.com/docs/clad/troubleshooting/troubleshoot-lens-studio-mcp

# Troubleshoot Lens Studio MCP

Detailed walkthroughs: [Claude Code Setup](#5-setup-ai--claude-code-setup), [Codex Setup](#6-setup-ai--codex-setup), [Cursor Setup](#7-setup-ai--cursor-setup).

### Verify Setup

Verify that Lens Studio is open and the project has been properly configured — [Setup Lens Studio](#4-setup--setup-lens-studio) and [Convert a Project to SPECS](#12-additional-guides--convert-a-project-to-specs).

### Verify MCP Server

In Lens Studio, select **AI Assistant > AI Model Context Protocol (MCP) > Configure Server**.

> 📸 IMAGE — **Open Lens Studio MCP configuration** (`image51.webp`)  
> A screenshot of Lens Studio with the "AI Assistant" menu open in the top menu bar. The submenu shows "AI Model Context Protocol (MCP)" expanded, and "Configure Server" is highlighted. This shows the exact navigation path to access the MCP server configuration popup inside Lens Studio.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-to-guides/troubleshoot-lens-studio-mcp/image51.webp_

The server popup should indicate the server is running. If not, select **Start Server**.

> 📸 IMAGE — **Copy MCP configuration** (`image72.webp`)  
> A screenshot of the Lens Studio MCP configuration popup dialog. The dialog shows the MCP server status (e.g., "Running" with a green indicator), server address/port information, a "Start Server" button (grayed out since it's running), and a "Copy MCP Config" button. The Copy MCP Config button copies the full JSON configuration to the clipboard so it can be pasted into an AI tool's config.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-to-guides/troubleshoot-lens-studio-mcp/image72.webp_

Example prompt after copying config:

```
Connect to Lens Studio MCP using the following configuration details: [Pasted MCP Config]
```

### Verify Lens Studio Plugins

Open preferences: **Lens Studio > Preferences > Plugins > Installed Plugins**.

> 📸 IMAGE — **Installed Plugins preferences** (`image55.webp`)  
> A screenshot of the Lens Studio Preferences window, open on the "Plugins" tab. A list of installed plugins is shown. The three required plugins — AiAssistantV2, Agents-Docs, and Core-ChatTools — should be visible in this list. Any plugin that is missing or disabled would be identified here.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-to-guides/troubleshoot-lens-studio-mcp/image55.webp_

Verify these plugins are present and enabled:

- **AiAssistantV2**
- **Agents-Docs**
- **Core-ChatTools**

> 📸 IMAGE — **AiAssistantV2, Agents-Docs, and Core-ChatTools enabled** (`image86.webp`)  
> A screenshot of the Lens Studio Installed Plugins list with all three required plugins visible and their toggle switches in the enabled/ON position: AiAssistantV2 (enables the AI assistant and MCP server), Agents-Docs (provides agent documentation tools), and Core-ChatTools (provides the core set of chat/AI tools including "Execute Editor Code"). Each plugin has a green/enabled indicator.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-to-guides/troubleshoot-lens-studio-mcp/image86.webp_

If any plugins are missing, reinstall from the Asset Library.

> **Tip:** One way to check that your AI harness has access to the complete suite of tools is by asking if it has access to the "Lens Studio Execute Editor Code tool".

---

## 11. Troubleshooting — Troubleshoot Lens Studio Plugin

> **URL:** https://developers.specs.com/docs/clad/troubleshooting/troubleshoot-lens-studio-plugin

# Troubleshoot Lens Studio Plugin

For the latest instructions, see the readme in [ls-extensions](https://github.com/lens-studio-devs/ls-extensions/#installation).

> 📸 IMAGE — **ls-extensions installation readme** (`image25.webp`)  
> A screenshot of the `lens-studio-devs/ls-extensions` GitHub repository README page, showing the "Installation" section. The README displays step-by-step installation instructions for each supported AI tool (Claude Code, Codex, Cursor), with the relevant commands for adding the plugin marketplace and installing the ls-clad plugin. This is the canonical, always-up-to-date source for installation instructions.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-to-guides/troubleshoot-lens-studio-plugin/image25.webp_

Detailed walkthroughs: [Claude Code Setup](#5-setup-ai--claude-code-setup), [Codex Setup](#6-setup-ai--codex-setup), [Cursor Setup](#7-setup-ai--cursor-setup).

- Some AI tools may not recognize plugins until the AI tool has been reloaded. Try closing and reopening the tool.
- Some AI tools may install a plugin but not enable it by default. Check your AI tool's documentation for how to enable the plugin.

---

## 12. Additional Guides — Convert a Project to SPECS

> **URL:** https://developers.specs.com/docs/clad/additional-guides/setup-specs-project

# Convert a Project to SPECS

CLAD is optimized for the SPECS platform. You can convert an existing project to target the SPECS platform, or create a SPECS project from scratch — see [Setup Lens Studio](#4-setup--setup-lens-studio).

> **Tip:** You can ask CLAD to set up your project to target SPECS for you.

### Converting a Project to SPECS

1. Convert **Target Platform** to **SPECS**.

> 📸 IMAGE — **Convert target platform to SPECS** (`image68.webp`)  
> A screenshot of Lens Studio's Project Settings panel showing the "Target Platform" dropdown selector. The dropdown is open or set to "SPECS". Other platform options (e.g., "Spectacles", "Camera") may be visible. This is the primary setting that tells Lens Studio to build for the SPECS hardware platform.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-to-guides/setup-specs-project/image68.webp_

2. Select project settings: **File > Project Settings**.
3. Confirm that the platform of your Preview panel(s) is set to **SPECS 27**.

> 📸 IMAGE — **Preview panel set to SPECS 27** (`image46.webp`)  
> A screenshot of Lens Studio with the Preview panel visible. The Preview panel's platform selector (a dropdown in the panel's toolbar) is set to "SPECS 27". This ensures the preview simulates the correct SPECS hardware environment rather than a phone or older Spectacles.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-to-guides/setup-specs-project/image46.webp_

4. Install the packages **SPECS UI Kit** and **Spectacles Interaction Kit** from the Asset Library.

> 📸 IMAGE — **Install SPECS UI Kit and Spectacles Interaction Kit** (`image40.webp`)  
> A screenshot of the Lens Studio Asset Library search interface with "SPECS UI Kit" searched. The result shows the SPECS UI Kit package with an "Import" or "Add to Project" button. The Asset Browser panel on the right may show the package appearing under "Packages" after installation. SpectaclesInteractionKit is shown as a dependency that gets auto-installed.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-to-guides/setup-specs-project/image40.webp_

5. For any Camera objects, add a **Device Tracking** component and set **Tracking Mode** to **World**.

> 📸 IMAGE — **Add Device Tracking to cameras** (`image82.webp`)  
> A screenshot of Lens Studio with a Camera object selected in the Scene Hierarchy. The Inspector panel on the right shows the camera's components. An "Add Component" button is visible, or the "Device Tracking" component is being added. This step enables world-space AR tracking for the camera.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-to-guides/setup-specs-project/image82.webp_

> 📸 IMAGE — **Device Tracking set to World** (`image43.webp`)  
> A screenshot of the Inspector panel for a Camera object, showing the Device Tracking component. The "Tracking Mode" property dropdown is set to "World". This configures the camera to track real-world surfaces and positions, enabling the AR experience to be anchored in the physical environment.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-to-guides/setup-specs-project/image43.webp_

6. For any camera objects, set the **Far** value to a large value like `100,000`.

> 📸 IMAGE — **Increase camera Far clip** (`image9.webp`)  
> A screenshot of the Inspector panel for a Camera component in Lens Studio. The "Far" clipping plane input field is visible and has been set to a large value (e.g., 100000). This setting prevents objects at real-world distances from being clipped out of the view frustum.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-to-guides/setup-specs-project/image9.webp_

7. Expand **SpectaclesInteractionKit** and drag **Prefabs/SpectaclesInteractionKit** into the scene.

> 📸 IMAGE — **Add Spectacles Interaction Kit prefab to the scene** (`image22.webp`)  
> A screenshot showing the Asset Browser panel with SpectaclesInteractionKit expanded, revealing the Prefabs folder. The "SpectaclesInteractionKit" prefab is selected or being dragged into the Scene Hierarchy or viewport. Adding this prefab provides the hand tracking and interaction system needed for SPECS experiences.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-to-guides/setup-specs-project/image22.webp_

> 📸 IMAGE — **Scene with SIK hands after setup** (`image90.webp`)  
> A screenshot of the Lens Studio viewport showing the result of adding the SpectaclesInteractionKit prefab. Two virtual hand models (left and right) appear in the 3D preview — these represent the simulated hand tracking that the SIK system provides. A compilation error may be visible in the Logger, which is resolved by refreshing the Logger (see the Refresh Logger guide).  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-to-guides/setup-specs-project/image90.webp_

The above steps outline the minimum changes necessary to port a project to the SPECS platform.

---

## 13. Additional Guides — Refresh the Logger

> **URL:** https://developers.specs.com/docs/clad/additional-guides/refresh-logger

# Refresh the Logger

Lens Studio logs errors as they are observed, but only some of those errors are compilation errors that prevent your Lens from running. To refresh your Logger to focus on compilation errors:

1. Clear your logger using the **Clear** button.

> 📸 IMAGE — **Clear the Logger** (`image56.webp`)  
> A screenshot of the Lens Studio Logger panel. The panel shows a list of log messages (errors, warnings, info). The "Clear" button (usually a trash can icon or "Clear" text button) at the top of the Logger panel is highlighted. Clicking this clears all accumulated log messages so only new ones from the next compile will appear.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-to-guides/refresh-logger/image56.webp_

2. Open the **TypeScript Status** window: **Window > Utilities > TypeScript Status**.

> 📸 IMAGE — **Open TypeScript Status** (`image54.webp`)  
> A screenshot of Lens Studio with the "Window" menu open in the top menu bar. The submenu shows "Utilities" expanded, with "TypeScript Status" highlighted. This is the navigation path to open the TypeScript Status panel, which shows the real compilation state of all TypeScript files in the project.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-to-guides/refresh-logger/image54.webp_

3. In the **TypeScript Status** window, check whether compilation succeeded.

> 📸 IMAGE — **Successful TypeScript compilation** (`image18.webp`)  
> A screenshot of the TypeScript Status panel in Lens Studio showing a successful compilation state. A green circle or green checkmark icon is displayed prominently, indicating that all TypeScript files compiled without errors. The panel may also show the number of files compiled and the compilation time.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-to-guides/refresh-logger/image18.webp_

> 📸 IMAGE — **Compilation errors in TypeScript Status** (`image3.webp`)  
> A screenshot of the TypeScript Status panel showing a failed compilation state. A red triangle warning icon (⚠️) is displayed, along with a count of compilation errors. A button labeled "Show errors in Logger" or similar is visible — clicking it will populate the Logger with only the TypeScript compilation errors, filtering out noise from runtime errors.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-to-guides/refresh-logger/image3.webp_

---

## 14. Additional Guides — Open Project in CLI

> **URL:** https://developers.specs.com/docs/clad/additional-guides/open-project-in-cli

# Open Your Project in CLI

Open your Lens Studio project folder in a command line interface (CLI) before starting Claude Code, Codex, Cursor, or other AI tools.

### macOS

1. Press **Command + Spacebar** to open Spotlight Search.
2. Type **Terminal** and press **Return** to open it.

> 📸 IMAGE — **Open Terminal on macOS** (`image19.webp`)  
> A screenshot of macOS Spotlight Search with "Terminal" typed into the search bar. The Terminal application appears as the top result. The Return key should be pressed to open it. This is the first step for macOS users who need to open a terminal window.  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-to-guides/open-project-in-cli/image19.webp_

3. Run `cd` with the path to your project folder.

```bash
cd ~/Documents/MyProject
```

> 📸 IMAGE — **Change directory to the project folder** (`image11.webp`)  
> A screenshot of the macOS Terminal showing a `cd` command being typed or already executed, changing the working directory to the Lens Studio project folder. The terminal prompt updates to show the project folder path at the beginning of the line, confirming the directory change was successful. This is the required state before launching any AI tool (Claude Code, Codex, Cursor).  
> _Asset URL: https://developers.specs.com/docs-static/static/clad/how-to-guides/open-project-in-cli/image11.webp_

### Windows

On Windows, use **PowerShell**, not Command Prompt (CMD).

1. Press **Win + R** to open the **Run** dialog.
2. Type `powershell` and press **Enter**.
3. Run `cd` with the path to your project folder.

```powershell
cd ~\Documents\MyProject
```

---

*End of CLAD Documentation — https://developers.specs.com/docs/clad*
