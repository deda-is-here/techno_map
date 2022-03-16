from sqlalchemy import Column, Integer, String

from db import Base, engine


class ClubInfo(Base):

    __tablename__ = "club info"

    id = Column(Integer, primary_key=True)
    club_name = Column(String(120), index=True, unique=True)
    club_address = Column(String(120), index=True, unique=True)

    def __repr__(self):
        return f"Club name - {self.club_name},\nClub address - {self.club_address},"


class User(Base):

    __tablename__ = "user info"

    id = Column(Integer, primary_key=True)
    user_name = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128))

    def __repr__(self):
        return f"Username - {self.user_name}"


class ClubContactInfo(Base):

    __tablename__ = "contact info"

    id = Column(Integer, primary_key=True)
    contact_username = Column(String(120), index=True, unique=True)
    contact_email = Column(String(120), index=True, unique=True)
    contact_password_hash = Column(String(128))

    def __repr__(self):
        f"""Contact username - {self.contact_username},\n
        Contact email - {self.contact_email}
        """


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
