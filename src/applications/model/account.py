from sqlalchemy import Boolean, Column, Integer, String, SmallInteger, BigInteger
from src.applications.config.database import Base


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    account = Column(String(128))
    password = Column(String(128))
    email_identify_password = Column(String(64))
    status = Column(Boolean, default=True)
    platform = Column(String(64))
    max_user = Column(SmallInteger)
    user_avail = Column(SmallInteger)
    create_time = Column(BigInteger)
    modify_time = Column(BigInteger)

    def to_json(self):
        return dict(
            id=self.id, account=self.account, password=self.password,
            email_identify_password=self.email_identify_password, status=self.status,
            platform=self.platform, max_user=self.max_user, user_avail=self.user_avail,
            create_time=self.create_time, modify_time=self.modify_time
        )