# --------------------------------------------------------------------------------
# Script Name: Drop to Floor Utility
# Description: This script contains a utility function to place selected objects
#              on the ground in Maya. It adjusts each selected object's position
#              so that its lowest point is aligned with the Y=0 plane, effectively
#              "dropping" it to the ground.
# Usage: The script is executed in Maya's Python environment. Ensure objects are
#        selected before running.
# Author: Kai Mallari
# Created: February 2024
# --------------------------------------------------------------------------------


import maya.cmds as mc


# Drops selected objects to the ground based on their bounding boxes
def drop2floor():
    """
    Drops the selected objects to the ground (Y=0) based on their bounding boxes.
    Iterates through all selected objects, calculates the lowest point on the Y-axis
    using the object's bounding box, and then adjusts the object's position so that
    this point aligns with Y=0.

    Operates on the current Maya selection.
    """
    selected_objects = mc.ls(selection=True)

    if selected_objects:
        for OBJECT in selected_objects:
            bbox = mc.exactWorldBoundingBox(OBJECT)
            object_position = mc.xform(OBJECT, query=True, translation=True)
            object_position[1] -= bbox[1]
            mc.xform(OBJECT, translation=object_position)
    else:
        print("No objects are selected.")


drop2floor()