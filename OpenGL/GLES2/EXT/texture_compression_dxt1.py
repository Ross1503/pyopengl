'''OpenGL extension EXT.texture_compression_dxt1

This module customises the behaviour of the 
OpenGL.raw.GLES2.EXT.texture_compression_dxt1 to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/texture_compression_dxt1.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper

import ctypes
from OpenGL.raw.GLES2 import _types
from OpenGL.raw.GLES2.EXT.texture_compression_dxt1 import *
from OpenGL.raw.GLES2.EXT.texture_compression_dxt1 import _EXTENSION_NAME

def glInitTextureCompressionDxt1EXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION