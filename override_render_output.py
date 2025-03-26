import maya.cmds as cmds
import maya.mel as mel

def set_render_output_path():
    # Open a folder dialog
    target_path = cmds.fileDialog2(fileMode=3, caption="Select Render Output Folder")
    
    if target_path:
        # Add placeholders for scene and render layer organization
        output_path = target_path[0].replace("\\", "/") + "/"
        
        # Set the output path override
        cmds.setAttr("defaultRenderGlobals.imageFilePrefix", output_path, type="string")
        cmds.setAttr("defaultRenderGlobals.outFormatControl", 0)
        
        print(f"Render output path set to: {output_path}")
    else:
        print("No folder selected.")

# Call the function to use it
set_render_output_path()
