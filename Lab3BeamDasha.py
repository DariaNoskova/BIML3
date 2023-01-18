import NemAll_Python_Geometry as geometry
import NemAll_Python_BaseElements as b_el
import NemAll_Python_BasisElements as bs_el
import g_val as g_val
import first_part_addition
import third_part_addition


# Потрібно для перевірки версії програми
def check_allplan_version(build_ele, version):
    del build_ele
    del version
    return True


# Потрібно для створення самого об'єкту
def create_element(build_ele, doc):
    el = Lab3BeamDasha(doc)
    return el.create(build_ele)


# Клас об'єкту балки
class Lab3BeamDasha:
    def __init__(self, doc):
        self.model_ele_list = []
        self.handle_list = []
        self.document = doc

    # Повинен бути
    def create(self, build_ele):
        self.parts_union(build_ele)
        return (self.model_ele_list, self.handle_list)

    # Первинні налаштування
    def settings(self, build_ele):
        settings = b_el.CommonProperties()
        settings.GetGlobalProperties()
        settings.Pen = 1
        settings.Color = 8
        settings.Stroke = 1
        return settings

    # Створення всіх частин балки
    def build_parts(self, build_ele):
        polyhedron_bottom = self.first_part(build_ele)
        polyhedron_center = self.second_part(build_ele)
        polyhedron_top = self.third_part(build_ele)
        return polyhedron_bottom, polyhedron_center, polyhedron_top

    # Об'єднання усіх частин балки
    def parts_union(self, build_ele):
        settings = self.settings(build_ele)
        tuple_parts = self.build_parts(build_ele)
        _, sh = geometry.MakeUnion(tuple_parts[0], tuple_parts[1])
        _, sh = geometry.MakeUnion(sh, tuple_parts[2])
        self.model_ele_list.append(bs_el.ModelElement3D(settings, sh))

    def interface(self, build_ele):
        LengthBottomCut = build_ele.LengthBottomCut.value
        HeightBottom = build_ele.HeightBottom.value
        WidthBottom = build_ele.WidthBottom.value
        LengthCenterWidth = build_ele.LengthCenterWidth.value
        LengthTransition = build_ele.LengthTransition.value
        WidthCentralLittle = build_ele.WidthCentralLittle.value
        Length = build_ele.Length.value
        HeightCenter = build_ele.HeightCenter.value
        WidthTop = build_ele.WidthTop.value
        HeightTopCut = build_ele.HeightTopCut.value
        Identation = build_ele.Identation.value
        HeightBottomCut = build_ele.HeightBottomCut.value
        HeightTop = build_ele.HeightTop.value
        HeightPlate = build_ele.HeightPlate.value
        return LengthBottomCut, HeightBottom, WidthBottom, LengthCenterWidth, LengthTransition, WidthCentralLittle, Length, HeightCenter, WidthTop, HeightTopCut, Identation, HeightBottomCut, HeightTop, HeightPlate

    def first_part(self, build_ele):
        sh = fp_1(build_ele)
        _, sh = geometry.MakeUnion(sh, fp_2(build_ele))
        _, sh = geometry.MakeUnion(sh, fp_3(build_ele))
        _, sh = geometry.MakeUnion(sh, fp_4(build_ele))
        _, sh = geometry.MakeUnion(sh, fp_2_2(build_ele))
        _, sh = geometry.MakeUnion(sh, fp_3_2(build_ele))
        _, sh = geometry.MakeUnion(sh, fp_4_2(build_ele))
        _, sh = geometry.MakeUnion(sh, fp_2_3(build_ele))
        _, sh = geometry.MakeUnion(sh, fp_3_3(build_ele))
        _, sh = geometry.MakeUnion(sh, fp_2_4(build_ele))
        _, sh = geometry.MakeUnion(sh, fp_3_4(build_ele))
        _, sh = geometry.MakeUnion(sh, fp_5(build_ele))
        return sh

    def second_part(self, build_ele):
        interface = self.interface(self, build_ele)
        polyline = geometry.Polygon3D()
        polyline += geometry.Point3D(0, interface[0], interface[1])
        polyline += geometry.Point3D(0, interface[2] - interface[0], interface[1])
        polyline += geometry.Point3D(interface[3], interface[2] - interface[0], interface[1])
        polyline += geometry.Point3D(interface[3] + interface[4], interface[2] - interface[0] - (interface[2] - interface[0] * 2 - interface[5]) / 2, interface[1])
        polyline += geometry.Point3D(interface[6] - (interface[3] + interface[4]), interface[2] - interface[0] - (interface[2] - interface[0] * 2 - interface[5]) / 2, interface[1])
        polyline += geometry.Point3D(interface[6] - interface[3], interface[2] - interface[0], interface[1])
        polyline += geometry.Point3D(interface[6], interface[2] - interface[0], interface[1])
        polyline += geometry.Point3D(interface[6], interface[0], interface[1])
        polyline += geometry.Point3D(interface[6] - interface[3], interface[0], interface[1])
        polyline += geometry.Point3D(interface[6] - interface[3] - interface[4], interface[0] + (interface[2] - interface[0] * 2 - interface[5]) / 2, interface[1])
        polyline += geometry.Point3D(interface[3] + interface[4], interface[0] + (interface[2] - interface[0] * 2 - interface[5]) / 2, interface[1])
        polyline += geometry.Point3D(interface[3], interface[0], interface[1])
        polyline += geometry.Point3D(0, interface[0], interface[1])

        poly_path = geometry.Polyline3D()
        poly_path += geometry.Point3D(0, interface[0], interface[1])
        poly_path += geometry.Point3D(0, interface[0], interface[1] + interface[7])

        _, sh = geometry.CreatePolyhedron(polyline, poly_path)

        return sh

    def third_part(self, build_ele):
        interface = self.interface(self, build_ele)
        sh = tp_1(build_ele)
        _, sh = geometry.MakeUnion(sh, tp_2(build_ele))
        _, sh = geometry.MakeUnion(sh, tp_3(build_ele))
        _, sh = geometry.MakeUnion(sh, tp_2(build_ele, plus=(interface[6] - interface[3])))
        _, sh = geometry.MakeUnion(sh, tp_4(build_ele))
        _, sh = geometry.MakeUnion(sh, tp_2_2(build_ele))
        _, sh = geometry.MakeUnion(sh, tp_4(build_ele, interface[2] - interface[0] * 2, interface[8], 10))
        _, sh = geometry.MakeUnion(sh, tp_2_3(build_ele))
        _, sh = geometry.MakeUnion(sh, tp_4_2(build_ele))
        _, sh = geometry.MakeUnion(sh, tp_4_2(build_ele, interface[2] - interface[0] * 2, interface[8], 10))
        _, sh = geometry.MakeUnion(sh, tp_3_3(build_ele))
        _, sh = geometry.MakeUnion(sh, tp_5(build_ele))
        return sh

