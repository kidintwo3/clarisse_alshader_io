# Clarisse AlShader IO
    Clarisse - Maya, Alshader import export util

#alshader_export.py
- Maya AlShader export script

#alshader_import.py
- Clarisse AlShader import script


  Inside Maya:
  ------------
    store_alstandard_mat_data(objA=['sphere1'], file_path='c:/test_mat.json')

  Inside Clarisse:
  ---------------
    read_mat_data(file_path='c:/test_mat.json', default_path="project://scene")
  
Supported
-----------
- File nodes: Only file paths are stored
