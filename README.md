# OverrideMayaRenderOutput

A simple Python script for Autodesk Maya to quickly set the render output directory via a folder outside the project directory. The alternative way of doing this manually is to paste the target path into "Render Settings/File Output/File name prefix:". Make sure it ends in "/".

## Features
- Opens a folder selection dialog in Maya.
- Automatically sets the selected path as the render output.
- Ensures the path uses forward slashes (`/`) for compatibility.
- Updates the `defaultRenderGlobals.imageFilePrefix` with the specified output path.
- Sets `outFormatControl` to `0` to allow custom file prefix usage.

## Usage
1. Copy the code file `override_render_output.py` from this repository.
2. Paste the script into your Maya Scripts Editor.
3. Execute the script.
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
