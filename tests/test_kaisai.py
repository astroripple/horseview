def test_kaisai():
    from sqlalchemy.orm import joinedload

    from jrdb_model import KaisaiData, create_app

    app = create_app()
    with app.app_context():
        kaisais = (
            KaisaiData.query.filter(
                KaisaiData.ymd >= 20220101, KaisaiData.ymd <= 20220130
            )
            .options(joinedload("*"))
            .all()
        )
        assert len(kaisais) == 1
