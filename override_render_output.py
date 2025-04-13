import maya.cmds as cmds

def set_render_output_path():
    # Open a folder dialog
    target_path = cmds.fileDialog2(fileMode=3, caption="Select Render Output Folder")
    
    if target_path:
        # Format path and remove any default prefixes
        output_path = target_path[0].replace("\\", "/")

        # Use a relative-looking placeholder to suppress auto-folder addition
        # This ensures only the path you provide is used
        cmds.setAttr("defaultRenderGlobals.imageFilePrefix", output_path + "/<Layer>", type="string")
        
        # Prevent Maya from auto-appending scene/layer/camera
        cmds.setAttr("defaultRenderGlobals.outFormatControl", 0)
        cmds.setAttr("defaultRenderGlobals.putFrameBeforeExt", 1)  # Frame number before extension
        cmds.setAttr("defaultRenderGlobals.animation", 1)         # Enable frame animation
        cmds.setAttr("defaultRenderGlobals.periodInExt", 1)       # Add period before frame number

        print(f"Render output path set to: {output_path}")
    else:
        print("No folder selected.")

# Run the function
set_render_output_path()
