import maya.cmds as cmds

import os
import json


def store_alstandard_mat_data(shader_nameA=None, file_path=None):
    """

    Store the Arnold AlStandard material attributes in a json file

    Example: store_alstandard_mat_data(shader_nameA=['alSurface1'], file_path='c:/test_mat.json')

    :param shader_nameA: array, string name of the shader to query from
    :param file_path: str, full output path
    :return:
    """

    if not shader_nameA:
        return

    if not file_path:
        return

    clarisse_arnold_pairs = {'diffuse_front_color': 'diffuseColor',
                             'diffuse_front_strength': 'diffuseStrength',
                             'diffuse_roughness': 'diffuseRoughness',
                             'diffuse_back_color': 'backlightColor',
                             'diffuse_back_strength': 'backlightStrength',

                             'mix': 'sssMix',
                             'subsurface_diffusion': 'sssMode',
                             'subsurface_density_scale': 'sssDensityScale',
                             'subsurface_color_1': 'sssRadiusColor',
                             'subsurface_distance_1': 'sssRadius',
                             'subsurface_weight_1': 'sssWeight1',
                             'subsurface_color_2': 'sssRadiusColor2',
                             'subsurface_distance_2': 'sssRadius2',
                             'subsurface_weight_2': 'sssWeight2',
                             'subsurface_color_3': 'sssRadiusColor3',
                             'subsurface_distance_3': 'sssRadius3',
                             'subsurface_weight_3': 'sssWeight3',

                             'diffuse_normal_mode': None,
                             'diffuse_normal_input': None,

                             'specular_color_1': 'specular1Color',
                             'specular_strength_1': 'specular1Strength',
                             'specular_roughness_1': 'specular1Roughness',
                             'specular_anisotropy_1': 'specular1Anisotropy',
                             'specular_anisotropy_rotation_1': 'specular1Rotation',
                             'specular_fresnel_mode_1': None,
                             'specular_index_of_refraction_1': 'specular1Ior',
                             'specular_fresnel_preset_1': None,
                             'specular_fresnel_reflectivity_1': 'specular1Reflectivity',
                             'specular_fresnel_edge_tint_1': 'specular1EdgeTint',
                             'specular_brdf_1': None,
                             'specular_exit_color_1': None,
                             'specular_normal_mode_1': None,
                             'specular_normal_input_1': None,

                             'specular_color_2': 'specular2Color',
                             'specular_strength_2': 'specular2Strength',
                             'specular_roughness_2': 'specular2Roughness',
                             'specular_anisotropy_2': 'specular2Anisotropy',
                             'specular_anisotropy_rotation_2': 'specular2Rotation',
                             'specular_fresnel_mode_2': None,
                             'specular_index_of_refraction_2': 'specular2Ior',
                             'specular_fresnel_preset_2': None,
                             'specular_fresnel_reflectivity_2': 'specular2Reflectivity',
                             'specular_fresnel_edge_tint_2': 'specular2EdgeTint',
                             'specular_brdf_2': None,
                             'specular_exit_color_2': None,
                             'specular_normal_mode_2': None,
                             'specular_normal_input_2': None,

                             'transmission_color': 'transmissionColor',
                             'transmission_strength': 'transmissionStrength',
                             'transmission_link_to_specular': 'transmissionLinkToSpecular1',
                             'transmission_linked_to': None,
                             'transmission_index_of_refraction': 'transmissionIor',
                             'transmission_roughness': 'transmissionRoughness',
                             'transmittance_color': None,
                             'transmittance_density': None,
                             'transmission_exit_color': None,
                             'transmission_normal_mode': None,
                             'transmission_normal_input': None,

                             'emission_color': 'emissionColor',
                             'emission_strength': 'emissionStrength'}

    shaderA = []

    for shader_name in shader_nameA:

        attributes = cmds.listAttr(shader_name, visible=True)

        atrA = {'name': shader_name, 'data': []}

        for i in attributes:

            value = cmds.getAttr(shader_name + '.' + str(i))

            if value:

                if isinstance(value, list):
                    value = value[0]

                # Check if plug has incoming file node connection
                conn_node = cmds.listConnections(shader_name + '.' + str(i), d=False, s=True)
                if conn_node:
                    if cmds.nodeType(conn_node, api=True) == 'kFileTexture':
                        tx_file_path = cmds.getAttr(conn_node[0] + '.fileTextureName')

                        # If it has a file path check if it's valid
                        if tx_file_path:
                            if os.path.exists(tx_file_path):
                                value = tx_file_path.replace('\\', '/')

                for clar_id, arnold_id in clarisse_arnold_pairs.iteritems():
                    if str(i) == arnold_id:
                        attr = {clar_id: value}
                        atrA['data'].append(attr)
                        break

        if atrA:
            shaderA.append(atrA)

    if shaderA:
        with open(file_path, 'w') as fp:
            json.dump(shaderA, fp, sort_keys=False, indent=4)

        print '[Info]Finished exporting material data...'


# Example script:
store_alstandard_mat_data(shader_nameA=['alSurface1'], file_path='c:/test_mat.json')