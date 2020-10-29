from ..sessioncontroll import (
    baseobj,
    strobj,
    baseobj,
    intobj,
    colobj,
    relobj,
    fkyobj,
    bkrobj,
    jsonobj,
)


class PredictRaceData(baseobj):
    __tablename__ = "predict_race"
    racekey = colobj(strobj, fkyobj("bangumi.racekey"), primary_key=True)
    umaren = colobj(jsonobj)
    wide = colobj(jsonobj)
    wakuren = colobj(jsonobj)
