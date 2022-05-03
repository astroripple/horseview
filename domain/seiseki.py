from ..sessioncontroll import (
    baseobj,
    strobj,
    baseobj,
    intobj,
    colobj,
    relobj,
    fkyobj,
    bkrobj,
)


class SeisekiData(baseobj):
    __tablename__ = "seiseki"
    racehorsekey = colobj(strobj, primary_key=True)
    racekey = colobj(strobj, fkyobj("seisekirace.racekey"))
    bacode = colobj(intobj)
    year = colobj(intobj)
    kai = colobj(intobj)
    day = colobj(intobj)
    raceno = colobj(intobj)
    seisekirace = relobj("SeisekiRaceData", uselist=False, backref=bkrobj("seiseki"))
    num = colobj(intobj)
    raceseisekikey = colobj(strobj)
    blood = colobj(intobj)
    ymd = colobj(strobj)
    horse = colobj(strobj)
    distance = colobj(intobj)
    tdscode = colobj(intobj)
    right_left = colobj(intobj)
    in_out = colobj(intobj)
    baba = colobj(intobj)
    baba_abst = colobj(intobj)
    baba_detail = colobj(intobj)
    shubetsu = colobj(intobj)
    joken = colobj(strobj)
    kigo = colobj(intobj)
    juryo = colobj(intobj)
    grade = colobj(intobj)
    racename = colobj(strobj)
    num_of_all_horse = colobj(intobj)
    racename_ryaku = colobj(strobj)
    order_of_arrival = colobj(intobj)
    ijo_kbn = colobj(intobj)
    time = colobj(intobj)
    kinryo = colobj(intobj)
    jockey_name = colobj(strobj)
    trainer_name = colobj(strobj)
    decided_odds = colobj(intobj)
    decided_pop_order = colobj(intobj)
    idm = colobj(intobj)
    natural_score = colobj(intobj)
    baba_sa = colobj(intobj)
    pace = colobj(intobj)
    start_late = colobj(intobj)
    position = colobj(intobj)
    furi = colobj(intobj)
    mae_furi = colobj(intobj)
    naka_furi = colobj(intobj)
    ushiro_furi = colobj(intobj)
    race = colobj(intobj)
    course_position = colobj(intobj)
    up_code = colobj(intobj)
    class_code = colobj(intobj)
    batai_code = colobj(intobj)
    kehai_code = colobj(intobj)
    racepace = colobj(strobj)
    umapace = colobj(strobj)
    ten_score = colobj(intobj)
    up_score = colobj(intobj)
    pace_score = colobj(intobj)
    racep_score = colobj(intobj)
    win_horse_name = colobj(strobj)
    time_sa = colobj(intobj)
    mae3f_time = colobj(intobj)
    agari3f_time = colobj(intobj)
    biko = colobj(strobj)
    yobi = colobj(strobj)
    decided_place_odds = colobj(intobj)
    juji_win_odds = colobj(intobj)
    juji_place_odds = colobj(intobj)
    corner_order1 = colobj(intobj)
    corner_order2 = colobj(intobj)
    corner_order3 = colobj(intobj)
    corner_order4 = colobj(intobj)
    mae3f_sa = colobj(intobj)
    agari3f_sa = colobj(intobj)
    jockey_code = colobj(intobj)
    trainer_code = colobj(intobj)
    weight = colobj(intobj)
    weight_increase = colobj(intobj)
    tenko = colobj(intobj)
    course = colobj(intobj)
    race_leg_type = colobj(strobj)
    win_ret = colobj(intobj)
    place_ret = colobj(intobj)
    this_money = colobj(intobj)
    earned_money = colobj(intobj)
    race_pace_flow = colobj(intobj)
    horse_pace_flow = colobj(intobj)
    corner4_course_position = colobj(intobj)
