# clarisse_alshader_io
Clarisse - Maya, Alshader import export util

[alshader_export] - Maya AlShader export script
[alshader_export] - Clarisse AlShader import script

[Usage]
  Inside Maya:
  ------------
    store_alstandard_mat_data(shader_nameA=['alSurface1'], file_path='c:/test_mat.json')

  Inside Clarisse:
  ---------------
    read_mat_data(file_path='c:/test_mat.json', default_path="project://scene")
  
[Supported]
  - File nodes: only file paths are stored
