class Employ(object):
    id=0
    def __init__(self, name, lastName,age,job,experience):
        self.id=id
        self.name=name
        self.lastName=lastName
        self.age=age
        self.job=job
        self.experience=experience
        id+=1

    def get_name(self):
        return self.name
    def get_lastName(self):
        return self.lastName
    def get_age(self):
        return self.age
    def get_job(self):
        return self.job
    def get_experience(self):
        return self.experience
    def set_name(self,name):
        self.name=name
    def set_lastName(self, lastName):
        self.lastName=lastName
    def set_age(self,age):
        self.age=age
    def set_job(self, job):
        self.job=job
    def set_experience(self,experience):
        self.experience=experience