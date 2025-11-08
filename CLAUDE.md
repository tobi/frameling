# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is the **frameling** configuration repository for managing system configurations on an Omarchy-based Linux system. Omarchy is a beautiful, modern & opinionated Linux distribution built on Arch Linux with Hyprland as the Wayland compositor.

**Key Concepts:**
- This repository is NOT the Omarchy source itself (located at `$HOME/.local/share/omarchy`)
- This is a personal configuration workspace where config files are staged, modified, and committed
- Configuration changes are made here via Claude Code, then committed with git
- Omarchy source: https://github.com/basecamp/omarchy

## System Architecture

### Configuration Layering

Hyprland and other tools use a hierarchical configuration system:

1. **Omarchy defaults** (`~/.local/share/omarchy/default/`) - Base system configs, DO NOT edit
2. **Theme configs** (`~/.config/omarchy/current/theme/`) - Current theme settings
3. **User overrides** (`~/.config/hypr/`, `~/.config/waybar/`, etc.) - Personal customizations

This repository mirrors the user override layer (`~/.config/`).

### File Organization

```
frameling/
├── hypr/              # Hyprland window manager config
│   ├── hyprland.conf  # Main entry, sources other files
│   ├── monitors.conf  # Display configuration
│   ├── input.conf     # Touchpad, keyboard settings
│   ├── bindings.conf  # Keybindings
│   ├── looknfeel.conf # Animations, decorations, shadows
│   ├── autostart.conf # Startup applications
│   ├── envs.conf      # Environment variables
│   ├── hypr*.conf     # hypridle, hyprlock, hyprsunset
│   ├── shaders/       # GLSL shaders for visual effects
│   └── AGENTS.md      # Development guidelines (reference this!)
├── waybar/            # Status bar configuration
│   ├── config.jsonc   # Waybar modules and layout
│   └── style.css      # Waybar styling
├── bin/               # Custom utilities (create as needed)
└── .claude/           # Claude Code configuration (skills, etc.)
```

## Common Development Tasks

### Testing Configuration Changes

**Hyprland:**
```bash
# Reload Hyprland config
hyprctl reload

# Check for config errors
hyprctl configerrors

# Get current effective config
hyprctl getoption all

# Refresh using Omarchy helper (recommended)
omarchy-refresh-hyprland
```

**Waybar:**
```bash
# Restart waybar
killall waybar && waybar &

# Refresh using Omarchy helper
omarchy-refresh-waybar
```

**Test shaders:**
```bash
hyprshade on <shader-name>
hyprshade off
ls ~/.config/hypr/shaders/  # List available shaders
```

### System Diagnostics

```bash
# Generate comprehensive system debug log (refreshes /tmp/omarchy-debug.log)
omarchy-debug

# Check Hyprland version and capabilities
hyprctl version

# Monitor information
hyprctl monitors

# Active window properties
hyprctl activewindow

# List all windows with classes (for window rules)
hyprctl clients
```

### Making Changes Workflow

1. **Make changes** to config files in this repository (hypr/, waybar/, etc.)
2. **Test changes** using `hyprctl reload` or `omarchy-refresh-*` commands
3. **Verify** with `hyprctl configerrors` or by testing functionality
4. **Commit changes** with git using a concise summary of the changes
5. **(Optional)** Run migrations if needed with `omarchy-migrate`

### Git Commit Workflow

After making configuration changes:

```bash
# Stage relevant files
git add hypr/monitors.conf hypr/looknfeel.conf  # Example

# Commit with summary
git commit -m "Update monitor layout and animation speeds"

# View recent commits
git log --oneline -10
```

**Commit message style:** Concise, imperative mood (e.g., "Add multi-monitor support", "Fix touchpad sensitivity", "Update keybindings for terminal")

## Omarchy CLI Tools

Omarchy provides extensive CLI tools prefixed with `omarchy-*`. Key tools:

**System Management:**
- `omarchy-debug` - Generate system diagnostics to `/tmp/omarchy-debug.log`
- `omarchy-migrate` - Run migration scripts after changes
- `omarchy-hook` - Hook system for custom event handling

**Configuration Refresh:**
- `omarchy-refresh-hyprland` - Reload Hyprland configuration
- `omarchy-refresh-waybar` - Restart waybar
- `omarchy-refresh-*` - Pattern for other tool refreshes

**Theme Management:**
- `omarchy-theme-set <theme>` - Switch system theme
- `omarchy-font-set <font>` - Change system font
- `omarchy-font-list` - List available fonts
- `omarchy-font-current` - Show current font

**Utilities:**
- `omarchy-cmd-screenshot` - Screenshot utility
- `omarchy-cmd-screenrecord` - Screen recording
- `omarchy-cmd-audio-switch` - Audio device switcher
- `omarchy-hyprland-workspace-toggle-gaps` - Toggle workspace gaps
- `omarchy-hyprland-window-pop` - Window management helper

All binaries are in `~/.local/share/omarchy/bin/`

## Hyprland Configuration Guidelines

**IMPORTANT:** Read `hypr/AGENTS.md` for detailed Hyprland development guidelines.

### Configuration Structure

Hyprland configs use modular sourcing:
- Main file sources defaults, then user overrides
- User configs in this repo override Omarchy defaults
- Use `$variable` syntax for reusable values (e.g., `$TERMINAL`, `$BROWSER`)

### Keybinding Patterns

Use `bindd` for descriptive bindings:
```conf
bindd = SUPER, Return, Terminal, exec, $TERMINAL
bindd = SUPER SHIFT, Q, Close Window, killactive
```

Group bindings by function (applications, utilities, media)

### Animation & Visual Effects

- **Speed:** 1-2 for fast/responsive, 3-5 for moderate, 6+ for slow
- **Curves:** `default` or `easeOutQuint` for smooth deceleration
- **Shadows:** Range 4-8, render power 3-5, use rgba with low opacity

See `hypr/AGENTS.md` for detailed animation configuration guidelines.

### GLSL Shaders

Location: `~/.config/hypr/shaders/`
- Use `#version 300 es` and `precision highp float;`
- Standard uniforms: `tex`, `time`, `v_texcoord`
- Include descriptive headers with usage instructions

## Local Tool Development

Create custom tools in `./bin/` directory:
- Follow `omarchy-*` naming pattern for consistency
- Make scripts executable (`chmod +x`)
- Use bash with `set -eEo pipefail` for error handling
- Source Omarchy helpers from `~/.local/share/omarchy/install/helpers/` if needed

## Code Style

Follow `.editorconfig` if present:
- 2-space indentation
- LF line endings
- Trim trailing whitespace

**Bash scripts:**
- Use `set -eEo pipefail` at the start
- Absolute paths: `$HOME/.local/share/omarchy` and `$OMARCHY_PATH`
- Error handling with user-friendly messages

## System Information

**Hardware:** Framework Laptop 13 (AMD Ryzen AI 300 Series)
- CPU: AMD Ryzen AI 7 350 w/ Radeon 860M
- Display: BOE 2256x1504 @ 201 DPI (13.5" 3:2 ratio)
- GPU: AMD Radeon 860M (amdgpu driver)

**Software:**
- OS: Arch Linux
- Kernel: 6.17.7-arch1-1
- Compositor: Hyprland 0.51.1
- Display: Wayland with Xwayland support

**Paths:**
- Omarchy installation: `$HOME/.local/share/omarchy`
- User configs: `$HOME/.config/hypr`, `$HOME/.config/waybar`, etc.
- Debug log: `/tmp/omarchy-debug.log` (refresh with `omarchy-debug`)

## Skills and Extensions

This repository uses Claude Code skills for specialized tasks:

- **hyprland** skill - Comprehensive Hyprland configuration assistance
- Future skills for waybar and other tools as needed

Skills are located in `.claude/skills/`

## Important Reminders

1. **Never edit Omarchy defaults directly** (`~/.local/share/omarchy/default/`)
2. **Always test before committing** - Use `hyprctl reload` and `hyprctl configerrors`
3. **Check debug log** for system issues: `/tmp/omarchy-debug.log`
4. **Reference AGENTS.md** in subdirectories (e.g., `hypr/AGENTS.md`) for component-specific guidelines
5. **Use Omarchy CLI tools** - They handle refresh/reload operations correctly
6. **Commit frequently** with clear, concise messages about configuration changes
