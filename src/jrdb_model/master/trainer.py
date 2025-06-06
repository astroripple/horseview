"""調教師データ."""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from ..sessioncontroll import db


class TrainerData(db.Model):
    __tablename__ = "trainer"
    trainer_code: Mapped[int] = mapped_column(primary_key=True)
    delete_flg: Mapped[int] = mapped_column()
    delete_ymd: Mapped[int] = mapped_column()
    trainer_name: Mapped[str] = mapped_column(String(255))
    trainer_kana: Mapped[str] = mapped_column(String(255))
    trainer_name_short: Mapped[str] = mapped_column(String(255))
    shozoku_code: Mapped[int] = mapped_column()
    shozoku_region: Mapped[str] = mapped_column(String(255))
    birthday: Mapped[int] = mapped_column()
    get_licence_year: Mapped[int] = mapped_column()
    trainer_comment: Mapped[str] = mapped_column(String(255))
    comment_ymd: Mapped[int] = mapped_column()
    this_leading: Mapped[int] = mapped_column()
    this_seiseki_flat_1st: Mapped[int] = mapped_column()
    this_seiseki_flat_2nd: Mapped[int] = mapped_column()
    this_seiseki_flat_3rd: Mapped[int] = mapped_column()
    this_seiseki_flat_out: Mapped[int] = mapped_column()
    this_seiseki_steeple_1st: Mapped[int] = mapped_column()
    this_seiseki_steeple_2nd: Mapped[int] = mapped_column()
    this_seiseki_steeple_3rd: Mapped[int] = mapped_column()
    this_seiseki_steeple_out: Mapped[int] = mapped_column()
    this_tokubetsu_win: Mapped[int] = mapped_column()
    this_jusho_win: Mapped[int] = mapped_column()
    last_leading: Mapped[int] = mapped_column()
    last_seiseki_flat_1st: Mapped[int] = mapped_column()
    last_seiseki_flat_2nd: Mapped[int] = mapped_column()
    last_seiseki_flat_3rd: Mapped[int] = mapped_column()
    last_seiseki_flat_out: Mapped[int] = mapped_column()
    last_seiseki_steeple_1st: Mapped[int] = mapped_column()
    last_seiseki_steeple_2nd: Mapped[int] = mapped_column()
    last_seiseki_steeple_3rd: Mapped[int] = mapped_column()
    last_seiseki_steeple_out: Mapped[int] = mapped_column()
    last_tokubetsu_win: Mapped[int] = mapped_column()
    last_jusho_win: Mapped[int] = mapped_column()
    total_seiseki_flat_1st: Mapped[int] = mapped_column()
    total_seiseki_flat_2nd: Mapped[int] = mapped_column()
    total_seiseki_flat_3rd: Mapped[int] = mapped_column()
    total_seiseki_flat_out: Mapped[int] = mapped_column()
    total_seiseki_steeple_1st: Mapped[int] = mapped_column()
    total_seiseki_steeple_2nd: Mapped[int] = mapped_column()
    total_seiseki_steeple_3rd: Mapped[int] = mapped_column()
    total_seiseki_steeple_out: Mapped[int] = mapped_column()
    data_ymd: Mapped[int] = mapped_column()
