import NemAll_Python_Geometry as geometry
import g_val as g_val
import Lab3BeamDasha

def tp_1(self, build_ele):
    interface = Lab3BeamDasha.interface(self, build_ele)
    polyline = geometry.Polygon3D()
    polyline += geometry.Point3D(interface[3], interface[2] - interface[0] - (
        interface[2] - interface[0] * 2 - interface[5]) / 2, interface[1] + interface[7])
    polyline += geometry.Point3D(interface[3], interface[8] - (
        interface[8] - interface[2]) / 2, interface[1] + interface[7] + interface[9])
    polyline += geometry.Point3D(interface[3], -(
        interface[8] - interface[2]) / 2, interface[1] + interface[7] + interface[9])
    polyline += geometry.Point3D(interface[3], interface[0] + (
        interface[2] - interface[0] * 2 - interface[5]) / 2, interface[1] + interface[7])
    polyline += geometry.Point3D(interface[3], interface[2] - interface[0] - (
        interface[2] - interface[0] * 2 - interface[5]) / 2, interface[1] + interface[7])
    poly_path = geometry.Polyline3D()
    poly_path += geometry.Point3D(interface[3], interface[2] - interface[0] - (
        interface[2] - interface[0] * 2 - interface[5]) / 2, interface[1] + interface[7])
    poly_path += geometry.Point3D(interface[6] - interface[3], interface[2] - interface[0] - (
        interface[2] - interface[0] * 2 - interface[5]) / 2, interface[1] + interface[7])

    _, sh = geometry.CreatePolyhedron(polyline, poly_path)

    return sh


def tp_3(self, build_ele):
    interface = Lab3BeamDasha.interface(self, build_ele)
    polyline = geometry.Polygon3D()
    polyline += geometry.Point3D(interface[6] - interface[3],
                                 interface[2] - interface[0], interface[1] + interface[7])
    polyline += geometry.Point3D(interface[6] - interface[3] - interface[4], interface[2] - interface[0] - (
        interface[2] - interface[0] * 2 - interface[5]) / 2, interface[1] + interface[7])
    polyline += geometry.Point3D(interface[6] - interface[3] - interface[4] - (interface[2] - interface[0] * 2 - interface[5]) / 2, interface[2] - (
        interface[2] - interface[0] * 2 - interface[5]) / 2 + (interface[8] - interface[2]) / 2, interface[1] + interface[7] + interface[9])
    polyline += geometry.Point3D(interface[6] - interface[3] - (interface[2] - interface[0] * 2 - interface[5]) / 2,
                                 interface[2] + (interface[8] - interface[2]) / 2, interface[1] + interface[7] + interface[9])
    polyline += geometry.Point3D(interface[6] - interface[3],
                                 interface[2] - interface[0], interface[1] + interface[7])

    poly_path = geometry.Polyline3D()
    poly_path += geometry.Point3D(interface[6] - interface[3],
                                  interface[2] - interface[0], interface[1] + interface[7])
    poly_path += geometry.Point3D(interface[6] - interface[3] + 10,
                                  interface[2] - interface[0] - 10, interface[1] + interface[7] + 10)

    _, sh = geometry.CreatePolyhedron(polyline, poly_path)

    return sh


def tp_2(self, build_ele, plus=0):
    interface = Lab3BeamDasha.interface(self, build_ele)
    polyline = geometry.Polygon3D()
    polyline += geometry.Point3D(plus,
                                 interface[0], interface[1] + interface[7])
    polyline += geometry.Point3D(plus,
                                 interface[2] - interface[0], interface[1] + interface[7])
    polyline += geometry.Point3D(plus, interface[2] + (
        interface[8] - interface[2]) / 2, interface[1] + interface[7] + interface[9])
    polyline += geometry.Point3D(plus, -(
        interface[8] - interface[2]) / 2, interface[1] + interface[7] + interface[9])
    polyline += geometry.Point3D(plus,
                                 interface[0], interface[1] + interface[7])

    poly_path = geometry.Polyline3D()
    poly_path += geometry.Point3D(plus,
                                  interface[0], interface[1] + interface[7])
    poly_path += geometry.Point3D(plus +
                                  interface[3], interface[0], interface[1] + interface[7])

    _, sh = geometry.CreatePolyhedron(polyline, poly_path)

    return sh


def tp_4(self, build_ele, minus_1=0, minus_2=0, digit=-10):
    interface = Lab3BeamDasha.interface(self, build_ele)
    polyline = geometry.Polygon3D()
    polyline += geometry.Point3D(interface[6] - interface[3], interface[2] -
                                 interface[0] - minus_1, interface[1] + interface[7])
    polyline += geometry.Point3D(interface[6] - interface[3], interface[8] - (
        interface[8] - interface[2]) / 2 - minus_2, interface[1] + interface[7] + interface[9])
    polyline += geometry.Point3D(interface[6] - interface[3] - (interface[2] - interface[0] * 2 - interface[5]) / 2, interface[2] + (
        interface[8] - interface[2]) / 2 - minus_2, interface[1] + interface[7] + interface[9])
    polyline += geometry.Point3D(interface[6] - interface[3], interface[2] -
                                 interface[0] - minus_1, interface[1] + interface[7])

    poly_path = geometry.Polyline3D()
    poly_path += geometry.Point3D(interface[6] - interface[3],
                                  interface[2] - interface[0] - minus_1, interface[1] + interface[7])
    poly_path += geometry.Point3D(interface[6] - interface[3], interface[2] -
                                  interface[0] + digit - minus_1, interface[1] + interface[7])
    _, sh = geometry.CreatePolyhedron(polyline, poly_path)

    return sh


def tp_2_2(self, build_ele):
    interface = Lab3BeamDasha.interface(self, build_ele)
    polyline = geometry.Polygon3D()
    polyline += geometry.Point3D(interface[6] - interface[3],
                                 interface[0], interface[1] + interface[7])
    polyline += geometry.Point3D(interface[6] - interface[3] - interface[4], interface[0] + (
        interface[2] - interface[0] * 2 - interface[5]) / 2, interface[1] + interface[7])
    polyline += geometry.Point3D(interface[6] - interface[3] - interface[4] - (interface[2] - interface[0] * 2 - interface[5]) / 2, (
        interface[2] - interface[0] * 2 - interface[5]) / 2 - (interface[8] - interface[2]) / 2, interface[1] + interface[7] + interface[9])
    polyline += geometry.Point3D(interface[6] - interface[3] - (interface[2] - interface[0] * 2 - interface[5]) / 2, -(
        interface[8] - interface[2]) / 2, interface[1] + interface[7] + interface[9])
    polyline += geometry.Point3D(interface[6] - interface[3],
                                 interface[0], interface[1] + interface[7])

    poly_path = geometry.Polyline3D()
    poly_path += geometry.Point3D(interface[6] - interface[3],
                                  interface[0], interface[1] + interface[7])
    poly_path += geometry.Point3D(interface[6] - interface[3] +
                                  10, interface[0] + 10, interface[1] + interface[7] + 10)

    _, sh = geometry.CreatePolyhedron(polyline, poly_path)

    return sh


def tp_2_3(self, build_ele):
    interface = Lab3BeamDasha.interface(self, build_ele)
    polyline = geometry.Polygon3D()
    polyline += geometry.Point3D(interface[3], interface[2] -
                                 interface[0], interface[1] + interface[7])
    polyline += geometry.Point3D(interface[3] + interface[4], interface[2] - interface[0] - (
        interface[2] - interface[0] * 2 - interface[5]) / 2, interface[1] + interface[7])
    polyline += geometry.Point3D(interface[3] + interface[4] + (interface[2] - interface[0] * 2 - interface[5]) / 2, interface[2] - (
        interface[2] - interface[0] * 2 - interface[5]) / 2 + (interface[8] - interface[2]) / 2, interface[1] + interface[7] + interface[9])
    polyline += geometry.Point3D(interface[3] + (interface[2] - interface[0] * 2 - interface[5]) / 2, interface[2] + (
        interface[8] - interface[2]) / 2, interface[1] + interface[7] + interface[9])
    polyline += geometry.Point3D(interface[3], interface[2] -
                                 interface[0], interface[1] + interface[7])

    poly_path = geometry.Polyline3D()
    poly_path += geometry.Point3D(
        interface[3], interface[2] - interface[0], interface[1] + interface[7])
    poly_path += geometry.Point3D(interface[3] - 10, interface[2] -
                                  interface[0] - 10, interface[1] + interface[7] - 10)

    _, sh = geometry.CreatePolyhedron(polyline, poly_path)

    return sh


def tp_4_2(self, build_ele, minus_1=0, minus_2=0, digit=-10):
    interface = Lab3BeamDasha.interface(self, build_ele)
    polyline = geometry.Polygon3D()
    polyline += geometry.Point3D(interface[3], interface[2] -
                                 interface[0] - minus_1, interface[1] + interface[7])
    polyline += geometry.Point3D(interface[3], interface[2] + (
        interface[8] - interface[2]) / 2 - minus_2, interface[1] + interface[7] + interface[9])
    polyline += geometry.Point3D(interface[3] + (interface[2] - interface[0] * 2 - interface[5]) / 2, interface[2] + (
        interface[8] - interface[2]) / 2 - minus_2, interface[1] + interface[7] + interface[9])
    polyline += geometry.Point3D(interface[3], interface[2] -
                                 interface[0] - minus_1, interface[1] + interface[7])

    poly_path = geometry.Polyline3D()
    poly_path += geometry.Point3D(interface[3], interface[2] -
                                  interface[0] - minus_1, interface[1] + interface[7])
    poly_path += geometry.Point3D(interface[3], interface[2] -
                                  interface[0] - minus_1 + digit, interface[1] + interface[7])

    _, sh = geometry.CreatePolyhedron(polyline, poly_path)

    return sh


def tp_3_3(self, build_ele):
    interface = Lab3BeamDasha.interface(self, build_ele)
    polyline = geometry.Polygon3D()
    polyline += geometry.Point3D(interface[3],
                                 interface[0], interface[1] + interface[7])
    polyline += geometry.Point3D(interface[3] + interface[4], interface[0] + (
        interface[2] - interface[0] * 2 - interface[5]) / 2, interface[1] + interface[7])
    polyline += geometry.Point3D(interface[3] + interface[4] + (interface[2] - interface[0] * 2 - interface[5]) / 2, (interface[2] -
                                 interface[0] * 2 - interface[5]) / 2 - (interface[8] - interface[2]) / 2, interface[1] + interface[7] + interface[9])
    polyline += geometry.Point3D(interface[3] + (interface[2] - interface[0] * 2 - interface[5]) / 2, -(
        interface[8] - interface[2]) / 2, interface[1] + interface[7] + interface[9])
    polyline += geometry.Point3D(interface[3],
                                 interface[0], interface[1] + interface[7])

    poly_path = geometry.Polyline3D()
    poly_path += geometry.Point3D(interface[3],
                                  interface[0], interface[1] + interface[7])
    poly_path += geometry.Point3D(interface[3] - 10,
                                  interface[0] + 10, interface[1] + interface[7] - 10)

    _, sh = geometry.CreatePolyhedron(polyline, poly_path)

    return sh


def tp_5(self, build_ele):
    interface = Lab3BeamDasha.interface(self, build_ele)
    polyline = geometry.Polygon3D()
    polyline += geometry.Point3D(0, -(
        interface[8] - interface[2]) / 2, interface[1] + interface[7] + interface[9])
    polyline += geometry.Point3D(0, interface[8] - (
        interface[8] - interface[2]) / 2, interface[1] + interface[7] + interface[9])
    polyline += geometry.Point3D(0, interface[8] - (
        interface[8] - interface[2]) / 2, interface[1] + interface[7] + interface[12])
    polyline += geometry.Point3D(0, interface[8] - (
        interface[8] - interface[2]) / 2 - interface[10], interface[1] + interface[7] + interface[12])
    polyline += geometry.Point3D(0, interface[8] - (interface[8] - interface[2]) /
                                 2 - interface[10], interface[1] + interface[7] + interface[12] + interface[13])
    polyline += geometry.Point3D(0, - (interface[8] - interface[2]) / 2 +
                                 interface[10], interface[1] + interface[7] + interface[12] + interface[13])
    polyline += geometry.Point3D(0, - (interface[8] - interface[2]) /
                                 2 + interface[10], interface[1] + interface[7] + interface[12])
    polyline += geometry.Point3D(0, - (
        interface[8] - interface[2]) / 2, interface[1] + interface[7] + interface[12])
    polyline += geometry.Point3D(0, -(
        interface[8] - interface[2]) / 2, interface[1] + interface[7] + interface[9])

    poly_path = geometry.Polyline3D()
    poly_path += geometry.Point3D(0, -(
        interface[8] - interface[2]) / 2, interface[1] + interface[7] + interface[9])
    poly_path += geometry.Point3D(interface[6], -(
        interface[8] - interface[2]) / 2, interface[1] + interface[7] + interface[9])
    _, sh = geometry.CreatePolyhedron(polyline, poly_path)

    return sh
