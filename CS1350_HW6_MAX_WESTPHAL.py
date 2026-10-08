from abc import ABC, abstractmethod

# Problem 1

class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_pay(self):
        pass

    @abstractmethod
    def description(self):
        pass

    def pay_stub(self):
        return f"{self.name} (ID: {self.employee_id}): ${self.calculate_pay():.2f}"

    @staticmethod
    def validate_positive(value, name):
        if value <= 0:
            raise ValueError(f"{name} must be positive!")
        return True


class SalariedEmployee(Employee):
    def __init__(self, name, employee_id, annual_salary):
        super().__init__(name, employee_id)
        Employee.validate_positive(annual_salary, "annual_salary")
        self.annual_salary = annual_salary

    def calculate_pay(self):
        return self.annual_salary / 24

    def description(self):
        return f"Salaried: {self.name}"


class HourlyEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)

        Employee.validate_positive(hourly_rate, "hourly_rate")
        Employee.validate_positive(hours_worked, "hours_worked")

        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        if self.hours_worked <= 40:
            return self.hourly_rate * self.hours_worked
        else:
            overtime_hours = self.hours_worked - 40
            return (40 * self.hourly_rate) + (
                overtime_hours * self.hourly_rate * 1.5
            )

    def description(self):
        return f"Hourly: {self.name}"


class CommissionEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, sales, commission_rate):
        super().__init__(name, employee_id)

        Employee.validate_positive(base_salary, "base_salary")
        Employee.validate_positive(sales, "sales")
        Employee.validate_positive(commission_rate, "commission_rate")

        if commission_rate > 1.0:
            raise ValueError("commission_rate must be positive!")

        self.base_salary = base_salary
        self.sales = sales
        self.commission_rate = commission_rate

    def calculate_pay(self):
        return self.base_salary + (self.sales * self.commission_rate)

    def description(self):
        return f"Commission: {self.name}"


class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def total_payroll(self):
        total = 0

        for employee in self.employees:
            total += employee.calculate_pay()

        return total

    def print_all_stubs(self):
        for employee in self.employees:
            print(employee.pay_stub())


# Problem 2

class Song:
    total_songs = 0

    def __init__(self, title, artist, duration_seconds):
        self.title = title
        self.artist = artist
        self.duration_seconds = duration_seconds

        Song.total_songs += 1

    def display(self):
        return f"{self.title} - {self.artist} ({Song.format_duration(self.duration_seconds)})"

    @classmethod
    def from_string(cls, s):
        parts = s.split(" | ")

        title = parts[0]
        artist = parts[1]
        duration_seconds = cls.parse_duration(parts[2])

        return cls(title, artist, duration_seconds)

    @classmethod
    def get_total_songs(cls):
        return cls.total_songs

    @staticmethod
    def format_duration(seconds):
        minutes = seconds // 60
        remaining_seconds = seconds % 60

        return f"{minutes}:{remaining_seconds:02d}"

    @staticmethod
    def parse_duration(duration_str):
        parts = duration_str.split(":")
        minutes = int(parts[0])
        seconds = int(parts[1])

        return minutes * 60 + seconds


class Playlist:
    total_playlists = 0

    def __init__(self, name):
        Playlist.total_playlists += 1

        self.playlist_id = f"PL_{Playlist.total_playlists:03d}"
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def total_duration(self):
        total = 0

        for song in self.songs:
            total += song.duration_seconds

        return total

    def display(self):
        return (
            f"Playlist: {self.name} "
            f"({len(self.songs)} songs, "
            f"{Song.format_duration(self.total_duration())})"
        )

    @classmethod
    def get_total_playlists(cls):
        return cls.total_playlists


class LibraryManager:
    @staticmethod
    def create_playlist_from_strings(name, song_strings):
        playlist = Playlist(name)

        for song_string in song_strings:
            playlist.add_song(Song.from_string(song_string))

        return playlist

    @staticmethod
    def format_library_report(playlists):
        report = "=== LIBRARY REPORT ===\n"

        total_songs = 0

        for playlist in playlists:
            report += f"Playlist: {playlist.name}\n"

            for index, song in enumerate(playlist.songs, start=1):
                report += f"  {index}. {song.display()}\n"

            report += (
                f"  Duration: "
                f"{Song.format_duration(playlist.total_duration())}\n"
            )

            total_songs += len(playlist.songs)

        report += f"Total Songs: {total_songs}\n"
        report += "======================"

        return report


# Problem 3

class GradeBook:
    def __init__(self, course_name):
        self.course_name = course_name
        self.grades = {}

    # Display Methods
    def __str__(self):
        return f"GradeBook: {self.course_name} ({len(self)} students)"

    def __repr__(self):
        return f"GradeBook('{self.course_name}')"

    def __len__(self):
        return len(self.grades)

    def __getitem__(self, student):
        if student not in self.grades:
            raise KeyError(student)

        return self.grades[student]

    def __setitem__(self, student, grade):
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100")

        self.grades[student] = grade

    def __contains__(self, student):
        return student in self.grades

    def __iter__(self):
        return iter(self.grades)

    def __bool__(self):
        return len(self.grades) > 0

    @property
    def average(self):
        if len(self.grades) == 0:
            return 0.0

        total = sum(self.grades.values())
        return total / len(self.grades)

# Arithmetic Operators
    def __add__(self, other):
        new_gradebook = GradeBook(
            f"{self.course_name} + {other.course_name}"
        )

        for student, grade in self.grades.items():
            new_gradebook.grades[student] = grade

        for student, grade in other.grades.items():
            if student in new_gradebook.grades:
                if grade > new_gradebook.grades[student]:
                    new_gradebook.grades[student] = grade
            else:
                new_gradebook.grades[student] = grade

        return new_gradebook

    def __iadd__(self, other):
        for student, grade in other.grades.items():
            if student in self.grades:
                if grade > self.grades[student]:
                    self.grades[student] = grade
            else:
                self.grades[student] = grade
        return self

    def __mul__(self, factor):
        new_gradebook = GradeBook(
            f"{self.course_name} (curved)"
        )

        for student, grade in self.grades.items():
            curved_grade = grade * factor

            if curved_grade > 100:
                curved_grade = 100

            new_gradebook.grades[student] = curved_grade

        return new_gradebook

# Comparison Operators
    def __eq__(self, other):
        return abs(self.average - other.average) < 0.01

    def __lt__(self, other):
        return self.average < other.average

    def __le__(self, other):
        return self.average <= other.average
    
    
    
# Test code


if __name__ == "__main__":

    # === Part A: Display and Container ===
    print("=== Part A: Container Protocol ===")

    cs101 = GradeBook("CS 101")

    # __setitem__
    cs101["Alice"] = 92
    cs101["Bob"] = 78
    cs101["Carol"] = 88
    cs101["David"] = 95

    # __str__ and __repr__
    print(cs101)
    print(repr(cs101))

    # __getitem__
    print(f"Alice's grade: {cs101['Alice']}")

    # __contains__
    print(f"Bob enrolled? {'Bob' in cs101}")
    print(f"Eve enrolled? {'Eve' in cs101}")

    # __len__
    print(f"Class size: {len(cs101)}")

    # __iter__
    print("Students:")
    for student in cs101:
        print(f" {student}: {cs101[student]}")

    # __bool__
    empty = GradeBook("Empty")
    print(f"cs101 has students? {bool(cs101)}")
    print(f"empty has students? {bool(empty)}")

    # Validation
    print("\nValidation test:")
    try:
        cs101["Eve"] = 150
    except ValueError as e:
        print(f" Caught: {e}")

    # === Part B: Arithmetic ===
    print("\n=== Part B: Arithmetic ===")

    math201 = GradeBook("Math 201")
    math201["Alice"] = 85
    math201["Bob"] = 90
    math201["Eve"] = 76

    # __add__ — merge (keep higher grade)
    combined = cs101 + math201

    print(f"\n{combined}")
    print("Merged grades:")

    for student in combined:
        print(f" {student}: {combined[student]}")

    # __mul__ — curve
    curved = math201 * 1.1

    print(f"\n{curved}")
    print("Curved grades:")

    for student in curved:
        print(f" {student}: {curved[student]}")

    # Test cap at 100
    big_curve = math201 * 1.5
    print(f"\nBig curve - Bob's grade: {big_curve['Bob']}")

    # === Part C: Comparisons ===
    print("\n=== Part C: Comparisons ===")

    print(f"CS 101 average: {cs101.average:.2f}")
    print(f"Math 201 average: {math201.average:.2f}")

    print(f"CS 101 == Math 201? {cs101 == math201}")
    print(f"Math 201 < CS 101? {math201 < cs101}")
    print(f"Math 201 <= CS 101? {math201 <= cs101}")

    # Sorting
    classes = [math201, cs101, curved]
    classes.sort()

    print("\nSorted by average:")
    for gb in classes:
        print(f" {gb} - avg: {gb.average:.2f}")
