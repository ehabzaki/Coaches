class Student:
    next_id = 1

    def __init__(self, name):
        self.id = Student.next_id
        self.name = name
        self.coaches = set()
        Student.next_id += 1

    def __getattr__(self, id):
        return id

    def __getattr__(self, name):
        return name

    def enroll_with_coaches(self, coach_id):
        self.coaches.add(coach_id)

    def __getattr__(self, coaches):
        return coaches


class Coach:
    next_id = 1

    def __init__(self):
        self.id = Coach.next_id
        self.capacity = 100
        self.students = set ()
        self.students_count = 0
        Coach.next_id += 1

    def __getattr__(self, id):
        return id

    def register_students(self, student_id):
        self.students.add(student_id)
        self.students_count = len(self.students)

    def __getattr__(self, students):
        return students

    def change_capacity(self, capacity):
        self.capacity = capacity

    def __getattr__(self, students_count):
        return self.students_count

    def __getattr__(self, capacity):
        return self.capacity


class CoachDistribution:

    def __init__(self):
        self.coaches = {}
        self.coaches_count = 0
        self.students = {}
        self.students_count = 0
   # all coaches
    def add_coach(self, coach):
        self.coaches[coach.id] = coach
        self.coaches_count = len(self.coaches)

    # all student
    def add_student(self, student):

        self.students[student.id] = student
        self.students_count = len(self.students)
    # distribute students to each coach
    def distribute(self):
        check = False
        total = 0
        all_ids = []
        students_id = list(self.students.keys())
        capacities = 0
        for c in self.coaches:
            capacities += self.coaches[c].capacity
            if len(self.coaches[c].students) == 0:
                check = True
            else:
                check = False
            all_ids += self.coaches[c].students
        for i in all_ids:
            students_id.remove(i)
        dist = 0
        remaining_student = 0
        if capacities == self.coaches_count * 100:
            if check:
                dist = int((len(students_id)) / self.coaches_count)
                remaining_student = (len(students_id)) % self.coaches_count
            elif not check:
                for c in self.coaches:
                    total += len(self.coaches[c].students)
                dist = int((total + len(students_id)) / self.coaches_count)
                remaining_student = (total + len(students_id)) % self.coaches_count
            couches_students = [dist for i in range(self.coaches_count)]
            for n in range(remaining_student):
                couches_students[n] += 1
            counter1 = 0

            for c in self.coaches:
                for i in list ( students_id ):
                    if couches_students[ counter1 ] > len ( self.coaches[ c ].students ):
                        self.coaches[ c ].register_students ( i )
                        self.students[ i ].enroll_with_coaches ( c )
                    else:
                        break
                    students_id.remove ( i )

                counter1 += 1
        else:
            couches_students = []

            for c in self.coaches:
                    self.coaches[ c ].students.clear()

            for i in self.coaches:
                cap = (round(len(self.students.keys()) * (self.coaches[i].capacity / 100)))
                couches_students.append(cap)
                caps = len(self.students.keys()) - sum(couches_students)
                couches_students[couches_students.index(max(couches_students))] += caps
            counter1 = 0
            s=list(self.students.keys())
            prev=0
            curr=0
            for c in self.coaches:
                curr = couches_students[counter1]
                ss=s[ prev:curr+prev]
                prev=curr+prev
                for i in ss:
                    self.coaches[c].register_students(i)
                    self.students[i].enroll_with_coaches(c)
                counter1 += 1
