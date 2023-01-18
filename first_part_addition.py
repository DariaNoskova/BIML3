import NemAll_Python_Geometry as geometry
import g_val as g_val
import Lab3BeamDasha


def fp_1(self, build_ele):
    interface = Lab3BeamDasha.interface(self, build_ele)
    polyline = geometry.Polygon3D()
    polyline += geometry.Point3D(interface[3],
                                 interface[2], interface[1] - interface[11])
    polyline += geometry.Point3D(interface[3],
                                 interface[2] - interface[0] -
                                 (interface[2] - interface[0]
                                     * 2 - interface[5]) / 2,
                                 interface[1])
    polyline += geometry.Point3D(interface[3],
                                 interface[2] - interface[0] - (
        interface[2] - interface[0] * 2 - interface[5]) / 2 - interface[5],
        interface[1])
    polyline += geometry.Point3D(interface[3],
                                 0, interface[1] - interface[11])
    polyline += geometry.Point3D(interface[3],
                                 interface[2], interface[1] - interface[11])

    poly_path = geometry.Polyline3D()
    poly_path += geometry.Point3D(interface[3],
                                  interface[2], interface[1] - interface[11])
    poly_path += geometry.Point3D(interface[6] - interface[3],
                                  interface[2], interface[1] - interface[11])
    _, sh = geometry.CreatePolyhedron(polyline, poly_path)

    return sh


def fp_2(self, build_ele):
    interface = Lab3BeamDasha.interface(self, build_ele)
    polyline = geometry.Polygon3D()
    polyline += geometry.Point3D(interface[3],
                                 interface[2] - interface[0], interface[1])
    polyline += geometry.Point3D(interface[3] + interface[4], interface[2] - interface[0] - (
        interface[2] - interface[0] * 2 - interface[5]) / 2, interface[1])
    polyline += geometry.Point3D(interface[3] + interface[4] + (interface[2] - interface[0] * 2 - interface[5]) / 2,
                                 interface[2] - (interface[2] - interface[0] * 2 - interface[5]) / 2, interface[1] - interface[11])
    polyline += geometry.Point3D(interface[3] + (interface[2] - interface[0]
                                 * 2 - interface[5]) / 2, interface[2], interface[1] - interface[11])
    polyline += geometry.Point3D(interface[3],
                                 interface[2] - interface[0], interface[1])

    poly_path = geometry.Polyline3D()
    poly_path += geometry.Point3D(interface[3],
                                  interface[2] - interface[0], interface[1])
    poly_path += geometry.Point3D(interface[3] - 10,
                                  interface[2] - interface[0] - 10, interface[1] - 10)

    _, sh = geometry.CreatePolyhedron(polyline, poly_path)

    return sh


def fp_3(self, build_ele):
    interface = Lab3BeamDasha.interface(self, build_ele)
    polyline = geometry.Polygon3D()
    polyline += geometry.Point3D(0, interface[2], interface[1] - interface[11])
    polyline += geometry.Point3D(0, interface[2] - interface[0], interface[1])
    polyline += geometry.Point3D(0, interface[0], interface[1])
    polyline += geometry.Point3D(0, 0, interface[1] - interface[11])
    polyline += geometry.Point3D(0, interface[2], interface[1] - interface[11])

    poly_path = geometry.Polyline3D()
    poly_path += geometry.Point3D(0,
                                  interface[2], interface[1] - interface[11])
    poly_path += geometry.Point3D(interface[3],
                                  interface[2], interface[1] - interface[11])

    _, sh = geometry.CreatePolyhedron(polyline, poly_path)

    return sh


def fp_4(self, build_ele):
    interface = Lab3BeamDasha.interface(self, build_ele)
    polyline = geometry.Polygon3D()
    polyline += geometry.Point3D(interface[3],
                                 interface[2] - interface[0], interface[1])
    polyline += geometry.Point3D(interface[3],
                                 interface[2], interface[1] - interface[11])
    polyline += geometry.Point3D(interface[3] + (interface[2] - interface[0]
                                 * 2 - interface[5]) / 2, interface[2], interface[1] - interface[11])
    polyline += geometry.Point3D(interface[3],
                                 interface[2] - interface[0], interface[1])

    poly_path = geometry.Polyline3D()
    poly_path += geometry.Point3D(interface[3],
                                  interface[2] - interface[0], interface[1])
    poly_path += geometry.Point3D(interface[3],
                                  interface[2] - interface[0] - 10, interface[1])

    _, sh = geometry.CreatePolyhedron(polyline, poly_path)

    return sh


def fp_2_2(self, build_ele):
    interface = Lab3BeamDasha.interface(self, build_ele)
    polyline = geometry.Polygon3D()
    polyline += geometry.Point3D(interface[3], interface[0], interface[1])
    polyline += geometry.Point3D(interface[3] + interface[4], interface[0] + (
        interface[2] - interface[0] * 2 - interface[5]) / 2, interface[1])
    polyline += geometry.Point3D(interface[3] + interface[4] + (interface[2] - interface[0] * 2 - interface[5]) / 2,
                                 (interface[2] - interface[0] * 2 - interface[5]) / 2, interface[1] - interface[11])
    polyline += geometry.Point3D(interface[3] + (
        interface[2] - interface[0] * 2 - interface[5]) / 2, 0, interface[1] - interface[11])
    polyline += geometry.Point3D(interface[3], interface[0], interface[1])

    poly_path = geometry.Polyline3D()
    poly_path += geometry.Point3D(interface[3], interface[0], interface[1])
    poly_path += geometry.Point3D(interface[3] -
                                  10, interface[0] + 10, interface[1] - 10)

    _, sh = geometry.CreatePolyhedron(polyline, poly_path)

    return sh


def fp_3_2(self, build_ele):
    interface = Lab3BeamDasha.interface(self, build_ele)
    polyline = geometry.Polygon3D()
    polyline += geometry.Point3D(interface[6] - interface[3],
                                 interface[2], interface[1] - interface[11])
    polyline += geometry.Point3D(interface[6] - interface[3],
                                 interface[2] - interface[0], interface[1])
    polyline += geometry.Point3D(interface[6] -
                                 interface[3], interface[0], interface[1])
    polyline += geometry.Point3D(interface[6] -
                                 interface[3], 0, interface[1] - interface[11])
    polyline += geometry.Point3D(interface[6] - interface[3],
                                 interface[2], interface[1] - interface[11])

    poly_path = geometry.Polyline3D()
    poly_path += geometry.Point3D(interface[6] - interface[3],
                                  interface[2], interface[1] - interface[11])
    poly_path += geometry.Point3D(interface[6],
                                  interface[2], interface[1] - interface[11])

    _, sh = geometry.CreatePolyhedron(polyline, poly_path)

    return sh


def fp_4_2(self, build_ele):
    interface = Lab3BeamDasha.interface(self, build_ele)
    polyline = geometry.Polygon3D()
    polyline += geometry.Point3D(interface[3], interface[0], interface[1])
    polyline += geometry.Point3D(interface[3], 0, interface[1] - interface[11])
    polyline += geometry.Point3D(interface[3] + (
        interface[2] - interface[0] * 2 - interface[5]) / 2, 0, interface[1] - interface[11])
    polyline += geometry.Point3D(interface[3], interface[0], interface[1])

    poly_path = geometry.Polyline3D()
    poly_path += geometry.Point3D(interface[3], interface[0], interface[1])
    poly_path += geometry.Point3D(interface[3],
                                  interface[0] + 10, interface[1])

    _, sh = geometry.CreatePolyhedron(polyline, poly_path)

    return sh


def fp_2_3(self, build_ele):
    interface = Lab3BeamDasha.interface(self, build_ele)
    polyline = geometry.Polygon3D()
    polyline += geometry.Point3D(interface[6] - interface[3],
                                 interface[2] - interface[0], interface[1])
    polyline += geometry.Point3D(interface[6] - interface[3] - interface[4], interface[2] - interface[0] - (
        interface[2] - interface[0] * 2 - interface[5]) / 2, interface[1])
    polyline += geometry.Point3D(interface[6] - interface[3] - interface[4] - (interface[2] - interface[0] * 2 - interface[5]) / 2,
                                 interface[2] - (interface[2] - interface[0] * 2 - interface[5]) / 2, interface[1] - interface[11])
    polyline += geometry.Point3D(interface[6] - interface[3] - (
        interface[2] - interface[0] * 2 - interface[5]) / 2, interface[2], interface[1] - interface[11])
    polyline += geometry.Point3D(interface[6] - interface[3],
                                 interface[2] - interface[0], interface[1])

    poly_path = geometry.Polyline3D()
    poly_path += geometry.Point3D(interface[6] - interface[3],
                                  interface[2] - interface[0], interface[1])
    poly_path += geometry.Point3D(interface[6] - interface[3] +
                                  10, interface[2] - interface[0] - 10, interface[1] + 10)

    _, sh = geometry.CreatePolyhedron(polyline, poly_path)

    return sh


def fp_3_3(self, build_ele):
    interface = Lab3BeamDasha.interface(self, build_ele)
    polyline = geometry.Polygon3D()
    polyline += geometry.Point3D(interface[6] - interface[3],
                                 interface[2] - interface[0], interface[1])
    polyline += geometry.Point3D(interface[6] - interface[3],
                                 interface[2], interface[1] - interface[11])
    polyline += geometry.Point3D(interface[6] - interface[3] - (
        interface[2] - interface[0] * 2 - interface[5]) / 2, interface[2], interface[1] - interface[11])
    polyline += geometry.Point3D(interface[6] - interface[3],
                                 interface[2] - interface[0], interface[1])

    poly_path = geometry.Polyline3D()
    poly_path += geometry.Point3D(interface[6] - interface[3],
                                  interface[2] - interface[0], interface[1])
    poly_path += geometry.Point3D(interface[6] - interface[3],
                                  interface[2] - interface[0] - 10, interface[1])

    _, sh = geometry.CreatePolyhedron(polyline, poly_path)

    return sh


def fp_2_4(self, build_ele):
    interface = Lab3BeamDasha.interface(self, build_ele)
    polyline = geometry.Polygon3D()
    polyline += geometry.Point3D(interface[6] -
                                 interface[3], interface[0], interface[1])
    polyline += geometry.Point3D(interface[6] - interface[3] - interface[4], interface[0] + (
        interface[2] - interface[0] * 2 - interface[5]) / 2, interface[1])
    polyline += geometry.Point3D(interface[6] - interface[3] - interface[4] - (interface[2] - interface[0] *
                                 2 - interface[5]) / 2, (interface[2] - interface[0] * 2 - interface[5]) / 2, interface[1] - interface[11])
    polyline += geometry.Point3D(interface[6] - interface[3] - (
        interface[2] - interface[0] * 2 - interface[5]) / 2, 0, interface[1] - interface[11])
    polyline += geometry.Point3D(interface[6] -
                                 interface[3], interface[0], interface[1])

    poly_path = geometry.Polyline3D()
    poly_path += geometry.Point3D(interface[6] -
                                  interface[3], interface[0], interface[1])
    poly_path += geometry.Point3D(interface[6] - interface[3] -
                                  10, interface[0] + 10, interface[1] - 10)

    _, sh = geometry.CreatePolyhedron(polyline, poly_path)

    return sh


def fp_3_4(self, build_ele):
    interface = Lab3BeamDasha.interface(self, build_ele)
    polyline = geometry.Polygon3D()
    polyline += geometry.Point3D(interface[6] -
                                 interface[3], interface[0], interface[1])
    polyline += geometry.Point3D(interface[6] -
                                 interface[3], 0, interface[1] - interface[11])
    polyline += geometry.Point3D(interface[6] - interface[3] - (
        interface[2] - interface[0] * 2 - interface[5]) / 2, 0, interface[1] - interface[11])
    polyline += geometry.Point3D(interface[6] -
                                 interface[3], interface[0], interface[1])

    poly_path = geometry.Polyline3D()
    poly_path += geometry.Point3D(interface[6] -
                                  interface[3], interface[0], interface[1])
    poly_path += geometry.Point3D(interface[6] -
                                  interface[3], interface[0] + 10, interface[1])

    _, sh = geometry.CreatePolyhedron(polyline, poly_path)

    return sh


def fp_5(self, build_ele):
    interface = Lab3BeamDasha.interface(self, build_ele)
    polyline = geometry.Polygon3D()
    polyline += geometry.Point3D(0, 20, 0)
    polyline += geometry.Point3D(0, interface[2] - 20, 0)
    polyline += geometry.Point3D(0, interface[2], 20)
    polyline += geometry.Point3D(0, interface[2], interface[1] - interface[11])
    polyline += geometry.Point3D(0, 0, interface[1] - interface[11])
    polyline += geometry.Point3D(0, 0, 20)
    polyline += geometry.Point3D(0, 20, 0)

    if not g_val.is_valid(polyline):
        return

    poly_path = geometry.Polyline3D()
    poly_path += geometry.Point3D(0, 20, 0)
    poly_path += geometry.Point3D(interface[6], 20, 0)

    _, sh = geometry.CreatePolyhedron(polyline, poly_path)

    return sh
