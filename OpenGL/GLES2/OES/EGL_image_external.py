'''OpenGL extension OES.EGL_image_external

This module customises the behaviour of the 
OpenGL.raw.GLES2.OES.EGL_image_external to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/EGL_image_external.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper

import ctypes
from OpenGL.raw.GLES2 import _types
from OpenGL.raw.GLES2.OES.EGL_image_external import *
from OpenGL.raw.GLES2.OES.EGL_image_external import _EXTENSION_NAME

def glInitEglImageExternalOES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION