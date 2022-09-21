from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 720
height = 720

blackmirror = Material(diffuse = (0.2, 0.2, 0.2), spec = 64, matType = REFLECTIVE)
redmirror = Material(diffuse = (0.9, 0.2, 0.2), spec = 64, matType = REFLECTIVE)

opaquepurple = Material(diffuse = (0.62, 0.12, 0.94), spec = 64, matType = OPAQUE)
opaquegreen = Material(diffuse = (0.2, 0.2, 0.9), spec = 64, matType = OPAQUE)

whiteglass = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 1.8, matType = TRANSPARENT)
yellowglass = Material(diffuse = (0.9, 0.9, 0.2), spec = 64, ior = 1.8, matType = TRANSPARENT)

rtx = Raytracer(width, height)

rtx.envMap = Texture("envmap1.bmp")

rtx.lights.append( AmbientLight(intensity = 0.1 ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1), intensity = 0.8 ))
#rtx.lights.append( PointLight(point = (0,0,0)))

rtx.scene.append( Sphere(V3(0,0,-10), 1, blackmirror)  )

rtx.scene.append( Sphere(V3(3,0,-10), 1, opaquegreen)  )
rtx.scene.append( Sphere(V3(0,3,-10), 1, opaquepurple)  )

rtx.scene.append( Sphere(V3(-3,0,-10),1, redmirror)  )
rtx.scene.append( Sphere(V3(-2,-3,-10), 1, whiteglass)  )
rtx.scene.append( Sphere(V3(2,-3,-10), 1, yellowglass)  )


rtx.glRender()

rtx.glFinish("output.bmp")