from ..sessioncontroll import baseobj, strobj, baseobj, intobj, colobj, relobj, fkyobj, bkrobj


class ReturninfoData(baseobj):
    __tablename__ = 'returninfo'
    racekey = colobj(strobj, fkyobj('bangumi.racekey'), primary_key=True)
    win1_num = colobj(intobj)
    win1_ret = colobj(intobj)
    win2_num = colobj(intobj)
    win2_ret = colobj(intobj)
    win3_num = colobj(intobj)
    win3_ret = colobj(intobj)
    place1_num = colobj(intobj)
    place1_ret = colobj(intobj)
    place2_num = colobj(intobj)
    place2_ret = colobj(intobj)
    place3_num = colobj(intobj)
    place3_ret = colobj(intobj)
    place4_num = colobj(intobj)
    place4_ret = colobj(intobj)
    place5_num = colobj(intobj)
    place5_ret = colobj(intobj)
    wakuren1_num1 = colobj(intobj)
    wakuren1_num2 = colobj(intobj)
    wakuren1_ret = colobj(intobj)
    wakuren2_num1 = colobj(intobj)
    wakuren2_num2 = colobj(intobj)
    wakuren2_ret = colobj(intobj)
    wakuren3_num1 = colobj(intobj)
    wakuren3_num2 = colobj(intobj)
    wakuren3_ret = colobj(intobj)
    umaren1_num1 = colobj(intobj)
    umaren1_num2 = colobj(intobj)
    umaren1_ret = colobj(intobj)
    umaren2_num1 = colobj(intobj)
    umaren2_num2 = colobj(intobj)
    umaren2_ret = colobj(intobj)
    umaren3_num1 = colobj(intobj)
    umaren3_num2 = colobj(intobj)
    umaren3_ret = colobj(intobj)
    wide1_num1 = colobj(intobj)
    wide1_num2 = colobj(intobj)
    wide1_ret = colobj(intobj)
    wide2_num1 = colobj(intobj)
    wide2_num2 = colobj(intobj)
    wide2_ret = colobj(intobj)
    wide3_num1 = colobj(intobj)
    wide3_num2 = colobj(intobj)
    wide3_ret = colobj(intobj)
    wide4_num1 = colobj(intobj)
    wide4_num2 = colobj(intobj)
    wide4_ret = colobj(intobj)
    wide5_num1 = colobj(intobj)
    wide5_num2 = colobj(intobj)
    wide5_ret = colobj(intobj)
    wide6_num1 = colobj(intobj)
    wide6_num2 = colobj(intobj)
    wide6_ret = colobj(intobj)
    wide7_num1 = colobj(intobj)
    wide7_num2 = colobj(intobj)
    wide7_ret = colobj(intobj)
    umatan1_num1 = colobj(intobj)
    umatan1_num2 = colobj(intobj)
    umatan1_ret = colobj(intobj)
    umatan2_num1 = colobj(intobj)
    umatan2_num2 = colobj(intobj)
    umatan2_ret = colobj(intobj)
    umatan3_num1 = colobj(intobj)
    umatan3_num2 = colobj(intobj)
    umatan3_ret = colobj(intobj)
    umatan4_num1 = colobj(intobj)
    umatan4_num2 = colobj(intobj)
    umatan4_ret = colobj(intobj)
    umatan5_num1 = colobj(intobj)
    umatan5_num2 = colobj(intobj)
    umatan5_ret = colobj(intobj)
    umatan6_num1 = colobj(intobj)
    umatan6_num2 = colobj(intobj)
    umatan6_ret = colobj(intobj)
    sanrenpuku1_num1 = colobj(intobj)
    sanrenpuku1_num2 = colobj(intobj)
    sanrenpuku1_num3 = colobj(intobj)
    sanrenpuku1_ret = colobj(intobj)
    sanrenpuku2_num1 = colobj(intobj)
    sanrenpuku2_num2 = colobj(intobj)
    sanrenpuku2_num3 = colobj(intobj)
    sanrenpuku2_ret = colobj(intobj)
    sanrenpuku3_num1 = colobj(intobj)
    sanrenpuku3_num2 = colobj(intobj)
    sanrenpuku3_num3 = colobj(intobj)
    sanrenpuku3_ret = colobj(intobj)
    sanrentan1_num1 = colobj(intobj)
    sanrentan1_num2 = colobj(intobj)
    sanrentan1_num3 = colobj(intobj)
    sanrentan1_ret = colobj(intobj)
    sanrentan2_num1 = colobj(intobj)
    sanrentan2_num2 = colobj(intobj)
    sanrentan2_num3 = colobj(intobj)
    sanrentan2_ret = colobj(intobj)
    sanrentan3_num1 = colobj(intobj)
    sanrentan3_num2 = colobj(intobj)
    sanrentan3_num3 = colobj(intobj)
    sanrentan3_ret = colobj(intobj)
    sanrentan4_num1 = colobj(intobj)
    sanrentan4_num2 = colobj(intobj)
    sanrentan4_num3 = colobj(intobj)
    sanrentan4_ret = colobj(intobj)
    sanrentan5_num1 = colobj(intobj)
    sanrentan5_num2 = colobj(intobj)
    sanrentan5_num3 = colobj(intobj)
    sanrentan5_ret = colobj(intobj)
    sanrentan6_num1 = colobj(intobj)
    sanrentan6_num2 = colobj(intobj)
    sanrentan6_num3 = colobj(intobj)
    sanrentan6_ret = colobj(intobj)
