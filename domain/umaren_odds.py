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
    dateobj,
)


class UmarenOddsData(baseobj):
    __tablename__ = "umaren_odds"
    racekey = colobj(strobj, fkyobj("bangumi.racekey"), primary_key=True)
    data_kbn = colobj(intobj)
    created_at = colobj(dateobj)
    published_date = colobj(dateobj)
    registered_horses = colobj(intobj)
    ran_horses = colobj(intobj)
    sold_flg = colobj(intobj)
    all_odds = colobj(jsonobj)
    all_estimated_odds = colobj(jsonobj)
    sum_of_all_bought_count = colobj(intobj)