from application import application, db, Recipe
from datetime import datetime

with application.app_context():
    db.create_all()
    print("Database tables created!")

    # Add initial data
    initial_data = [
        Recipe(
            id=1,
            title='Chicken Curry',
            making_time='45 min',
            serves='4 people',
            ingredients='onion, chicken, seasoning',
            cost=1000,
            created_at=datetime(2016, 1, 10, 12, 10, 12),
            updated_at=datetime(2016, 1, 10, 12, 10, 12)
        ),
        Recipe(
            id=2,
            title='Rice Omelette',
            making_time='30 min',
            serves='2 people',
            ingredients='onion, egg, seasoning, soy sauce',
            cost=700,
            created_at=datetime(2016, 1, 11, 13, 10, 12),
            updated_at=datetime(2016, 1, 11, 13, 10, 12)
        )
    ]
    db.session.bulk_save_objects(initial_data)
    db.session.commit()
    print("Initial data inserted!")
