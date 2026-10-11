from base import Session

def get_all(model):
    try:
        with Session() as session:
            return session.query(model).all()
    except:
        raise "Error"

def create_new(model):
    try:
        with Session() as session:
            session.add(model)
            session.commit()
            return model
    except Exception as e:
        print(e)
        raise "Error"


def delete(model):
    try:
        with Session() as session:
            session.delete(model)
            session.commit()
            return model
    except Exception as e:
        print(e)
        raise "Error"