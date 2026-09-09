# Blender Material Replacer

A small Blender add-on that replaces one material with another throughout the current Blender file.

It is useful when the same material is used on many objects and you want to swap all of those material assignments at once.

## What It Does

The add-on adds a **Material Replacer** panel to the 3D View sidebar.

You choose:

- Old Material
- New Material

Then press:

**Replace Material**

Every material slot using the old material is changed to use the new material.

## Installation

### Blender 4.5

1. Download `material_replacer.py`.
2. Open Blender.
3. Go to **Edit > Preferences**.
4. Select **Add-ons**.
5. Open the menu in the upper-right corner.
6. Choose **Install from Disk**.
7. Select `material_replacer.py`.
8. Enable **Material Replacer** if it is not already enabled.

## How To Use

1. Open the 3D View.
2. Press **N** to open the sidebar.
3. Open the **Material Replacer** tab.
4. Choose the material you want to replace in **Old Material**.
5. Choose the replacement material in **New Material**.
6. Click **Replace Material**.

The add-on will replace matching material assignments throughout the Blender file.

## Why I Made It

I wanted a quick way to replace a material used across many objects without having to edit each object individually.

This add-on is intentionally simple and focused on that one task.

## Compatibility

Designed for:

**Blender 4.5**

## Author

**BlenderMark**

Created as a free utility for the Blender community.<img width="245" height="177" alt="Replace" src="https://github.com/user-attachments/assets/f170c510-537b-419e-a4d0-cbf859fb5c12" />
