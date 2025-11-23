# Hyprland Configuration Agents Guide

## Build/Test Commands
- **Reload config**: `hyprctl reload`
- **Check config**: `hyprctl configerrors`
- **Test shader**: `hyprshade on <shader-name>`
- **List shaders**: `ls ~/.config/hypr/shaders/`
- **Check version**: `hyprctl version` (to verify available commands)
- **Get active config**: `hyprctl getoption all` (to see current effective settings)

## Code Style Guidelines

### Configuration Structure
- Use modular config files (monitors.conf, input.conf, bindings.conf, etc.)
- Source defaults first, then override with personal configs
- Use `$variable` syntax for reusable commands/paths

### Naming Conventions
- Variables: `$TERMINAL`, `$BROWSER` (UPPER_SNAKE_CASE)
- Bindings: `bindd = MODIFIER, KEY, Description, exec, command`
- Comments: Use `#` for single-line, `# Section` for organization

### GLSL Shaders
- Version: `#version 300 es`
- Include descriptive header with usage instructions
- Use `precision highp float;`
- Standard uniforms: `tex`, `time`, `v_texcoord`

### Keybinding Patterns
- Use `bindd` for descriptive bindings
- Group by function (applications, utilities, media)
- Use `omarchy-launch-*` helpers for consistent app launching

## Animation & Visual Effects Guidelines

### Animation Configuration
- **Speed**: Use 1-2 for fast, responsive animations; 3-5 for moderate; 6+ for slow
- **Curves**: `default` for standard, `easeOutQuint` for smooth deceleration
- **Focus effects**: Use `fadeSwitch` animation for visible focus transitions
- **Workspace switching**: `workspaceSwitch` with speed 1-2 for snappy transitions

### Shadow Configuration
- **Range**: 4-8 for subtle shadows (4 = small, 8 = large)
- **Render power**: 3-5 (3 = subtle, 5 = prominent)
- **Color**: Use rgba with low opacity (0.25 = 25% opacity)
- **Syntax**: `col.shadow = rgba(0, 0, 0, 0.25)`

### Common Animation Types
- `fadeSwitch`: Window focus changes
- `workspaceSwitch`: Workspace navigation
- `windowOpen`: New window creation
- `windowClose`: Window destruction
- `border`: Window border animations

## Information Sources

### Primary Sources (Check First)
1. **Current effective config**: `hyprctl getoption all` - shows what's actually loaded
2. **Hyprland Wiki**: https://wiki.hyprland.org/ - comprehensive documentation
3. **Config files in this repo**: Check existing patterns before adding new ones

### Debugging Information
- **Version compatibility**: `hyprctl version` to check available commands
- **Live monitoring**: `hyprctl monitors` for current display setup
- **Active windows**: `hyprctl activewindow` for current window properties
- **Active workspace**: `hyprctl activeworkspace` for workspace info

### File Structure Understanding
- **[hyprland.conf](./hyprland.conf)**: Main entry point, sources other files
- **[looknfeel.conf](./looknfeel.conf)**: Animations, decorations, shadows, visual effects
- **[bindings.conf](./bindings.conf)**: Keybindings and application launchers
- **[input.conf](./input.conf)**: Touchpad, keyboard, and input device settings
- **[monitors.conf](./monitors.conf)**: Display configuration and workspace layout