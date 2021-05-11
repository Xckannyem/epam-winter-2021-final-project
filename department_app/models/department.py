from department_app import db


class Department(db.Model):
    """
    Create a Department table
    """
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='department',
                                lazy='dynamic')

    def to_dict(self):
        """
        Serializer that returns a dictionary from its fields (in json format)
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'employees': [employee.to_dict() for employee in self.employees]
        }

    def __repr__(self):
        return f'Department: {self.name}'
