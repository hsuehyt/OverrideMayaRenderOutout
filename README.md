# OverrideMayaRenderOutput

A simple Python script for Autodesk Maya to quickly set the render output directory via a folder dialog without permanently changing project structures or paths, when just wanting to ignore the project path temporarily and view the rendering results outside the project directory. The alternative way of doing this manually is to paste the target path into "Render Settings/File Output/File name prefix:" and make sure it ends in "/"

## Features
- Opens a folder selection dialog in Maya.
- Automatically sets the selected path as the render output.
- Ensures the path uses forward slashes (`/`) for compatibility.
- Updates the `defaultRenderGlobals.imageFilePrefix` with the specified output path.
- Sets `outFormatControl` to `0` to allow custom file prefix usage.

## Installation
1. Clone or download this repository.
2. Copy the script into your Maya scripts directory or source it directly in Maya.

## Usage
1. In Maya, open the Script Editor.
2. Load and execute the script.
3. Call the function:
   ```python
   set_render_output_path()
   ```
4. A folder dialog will appear. Select your desired output directory.
5. The script will automatically apply the selected folder as the render output path.

## Important Notes
- The chosen path will be set in **Render Settings > File Output > File name prefix**.
- Make sure the path ends with a forward slash (`/`).
- Example manual method (without this script):
  1. Open **Render Settings**.
  2. Go to **File Output** tab.
  3. In **File name prefix**, paste the target path (make sure it ends with `/`).

## Repository
GitHub: [OverrideMayaRenderOutput](https://github.com/hsuehyt/OverrideMayaRenderOutout)

## License
This project is open-source under the MIT License.

---

If you find this tool helpful, feel free to star the repo or contribute!
