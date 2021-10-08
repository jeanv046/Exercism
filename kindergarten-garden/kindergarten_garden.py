import itertools
class Garden(object):
    PLANTS = {
        'C': 'Clover',
        'G': 'Grass',
        'R': 'Radishes',
        'V': 'Violets',
    }
    DEFAULT_STUDENTS = [
        'Alice',
        'Bob',
        'Charlie',
        'David',
        'Eve',
        'Fred',
        'Ginny',
        'Harriet',
        'Ileana',
        'Joseph',
        'Kincaid',
        'Larry',
    ]
    
    CUPS_EACH = 2
    def __init__(self, layout, students=DEFAULT_STUDENTS):
        self.rows = layout.split()
        self.students = sorted(students)
    def plants(self, owner):
        
        pos = self.students.index(owner) * Garden.CUPS_EACH
        
        cups = itertools.chain(*(row[pos:pos+Garden.CUPS_EACH]
                                 for row in self.rows))
        
        return [Garden.PLANTS[cup] for cup in cups]