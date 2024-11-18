# REX/serialusm2m/__init__.py

import os
import glob
import importlib.util

current_dir = os.path.dirname(__file__)

module_files = glob.glob(os.path.join(current_dir, '*.py'))
module_names = [
    os.path.basename(f)
    for f in module_files
    if os.path.isfile(f) and not f.endswith('__init__.py')
]

__all__ = []

for filename in module_names:
    module_name = os.path.splitext(filename)[0]
    
    # Replace spaces and special characters with underscores
    module_alias = module_name
    for char in [' ', '#', '-', '.', '+', '&', '%', '$', '@', '!', '*']:
        module_alias = module_alias.replace(char, '_')
    
    # Ensure the alias starts with a letter or underscore
    if not module_alias[0].isalpha() and module_alias[0] != '_':
        module_alias = '_' + module_alias
    
    module_path = os.path.join(current_dir, filename)
    spec = importlib.util.spec_from_file_location(module_alias, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    globals()[module_alias] = module
    __all__.append(module_alias)
