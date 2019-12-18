from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    firstname = db.Column(db.String(120), nullable=False)
    lastname = db.Column(db.String(120) )
    password = db.Column(db.String(80), nullable=False)
    avatar = db.Column(db.String(220), default='avatar.png')
    wallet = db.Column(db.Float(5), default=0)
    admin = db.Column(db.Integer)

    def __repr__(self):
        return '<Users %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "avatar": self.avatar,
            "wallet": self.wallet,
            "admin": self.admin
        }
    
class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fromId = db.Column(db.Integer)
    fromName = db.Column(db.String(120))
    fromEmail = db.Column(db.String(120))
    toId = db.Column(db.Integer)
    toName = db.Column(db.String(120))
    toEmail = db.Column(db.String(120))
    message = db.Column(db.Text)
    dateSent = db.Column(db.String(120))
    read = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Chat %r>' % self.fromName
    
    def serialize(self):
        return {
            "id": self.id,
            "fromId": self.fromId,
            "fromName": self.fromName,
            "fromEmail": self.fromEmail,
            "toId": self.toId,
            "toName": self.toName,
            "toEmail": self.toEmail,
            "message": self.message,
            "dateSent": self.dateSent,
            "read": self.read
        }
