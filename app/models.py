from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app import db


class ClubInfo(db.Base):

    __tablename__ = "club info"

    id = Column(Integer, primary_key=True)
    club_name = Column(String(120), index=True, unique=True)
    club_address = Column(String(120), index=True, unique=True)
    club_contact = relationship('ClubContactInfo', backref='contact')

    def __repr__(self):
        return f"Club name: {self.club_name},\nClub address: {self.club_address},"


class User(db.Base):

    __tablename__ = "user info"

    id = Column(Integer, primary_key=True)
    name = Column(String(120), index=True)
    login = Column(String(120), index=True, unique=True)
    created_date = Column(Date(), nullable=False)
    password_hash = Column(String(128))

    def __repr__(self):
        return f"Username: {self.name}"


class ClubContactInfo(db.Base):

    __tablename__ = "contact info"

    id = Column(Integer, primary_key=True)
    club_id = Column(Integer, ForeignKey("ClubInfo.id"))
    contact_username = Column(String(120), index=True, unique=True)
    contact_email = Column(String(120), index=True, unique=True)
    contact_password_hash = Column(String(128))

    def __repr__(self):
        f"""Contact username: {self.contact_username},\n
        Contact email: {self.contact_email},\n
        Club id: {self.club_id}
        """


if __name__ == "__main__":
    db.Base.metadata.create_all(bind=db.engine)
