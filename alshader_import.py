import ix

import os
import json
import ntpath


def read_mat_data(file_path=None, default_path="project://scene"):
    """

    Reads the material data from the json file

    Example: read_mat_data(file_path='c:/test_mat.json')

    :param file_path: str, full path to the json file
    :param default_path: str, context path where the materials and texture nodes will be created
    :return:
    """

    if not file_path:
        return

    if not os.path.exists(file_path):
        return

    # Open the json file and read the data
    with open(file_path, 'r') as fp:
        dataA = json.load(fp)

    if not dataA:
        return

    for shader in dataA:
        if shader:
            shader_name = shader['name']

            # Create Physical Material
            if shader_name:
                standard_mat = ix.cmds.CreateObject(str(shader_name) + '_mat', "MaterialPhysicalStandard", "Global",
                                                    default_path)

            # Get the attributes
            if standard_mat:
                attributes_data = shader.get('data')

                if attributes_data:
                    for i in attributes_data:
                        if i:

                            if isinstance(i, dict):
                                for clar_id, val in i.iteritems():

                                    print val

                                    if isinstance(val, list) and len(val) == 3:
                                        ix.cmds.SetValues([standard_mat.get_full_name() + "." + str(clar_id)],
                                                          [str(val[0]), str(val[1]), str(val[2])])

                                    # Everything that is a string is considered as a file path
                                    elif isinstance(val, basestring):
                                        texture_node = ix.cmds.CreateObject(str(ntpath.basename(val)) + "_tx",
                                                                            "TextureStreamedMapFile", "Global",
                                                                            default_path)

                                        if texture_node:
                                            ix.cmds.SetValues([texture_node.get_full_name() + ".filename[0]"],
                                                              [str(val)])

                                            ix.cmds.SetTexture([standard_mat.get_full_name() + "." + str(clar_id)],
                                                               texture_node.get_full_name())

                                    else:
                                        # Set the attribute
                                        ix.cmds.SetValues([standard_mat.get_full_name() + "." + str(clar_id)],
                                                          [str(val)])


read_mat_data(file_path='c:/test_mat.json', default_path="project://scene")