# Problem 1

class Gradebook:
    def __init__(self):
        self.grades = {}

    def add_score(self, student, assignment, score):
        if student not in self.grades:
            self.grades[student] = {}
        self.grades[student][assignment] = score

    def student_average(self, student):
        if student not in self.grades or not self.grades[student]:
            return None

        scores = self.grades[student].values()
        return sum(scores) / len(scores)

    def assignment_average(self, assignment):
        scores = []

        for assignments in self.grades.values():
            if assignment in assignments:
                scores.append(assignments[assignment])

        if not scores:
            return None

        return sum(scores) / len(scores)

    def top_students(self, n):
        averages = []

        for student in self.grades:
            avg = self.student_average(student)
            if avg is not None:
                averages.append((avg, student))

        averages.sort(reverse=True)

        return [student for avg, student in averages[:n]]

    def missing(self, assignment):
        result = []

        for student, assignments in self.grades.items():
            if assignment not in assignments:
                result.append(student)

        return sorted(result)
    
gb = Gradebook()
gb.add_score("Alice", "hw1", 90)
gb.add_score("Alice", "hw2", 80)
gb.add_score("Bob", "hw1", 70)
gb.add_score("Bob", "hw2", 60)
gb.add_score("Carol", "hw1", 100)
gb.add_score("Bob", "hw2", 75) 
print(gb.student_average("Alice"))
print(gb.student_average("Bob")) 
print(gb.student_average("Zed")) 
print(gb.assignment_average("hw1")) 
print(gb.assignment_average("hw9")) 
print(gb.top_students(2)) 
print(gb.missing("hw2")) 


# Problem 2

class Door:
    def __init__(self, name):
        self.name = name
        self.cards = set()

    def grant(self, card_id):
        self.cards.add(card_id)

    def revoke(self, card_id):
        self.cards.discard(card_id)

    def can_open(self, card_id):
        return card_id in self.cards


def master_cards(doors):
    if not doors:
        return set()

    result = doors[0].cards.copy()

    for door in doors[1:]:
        result &= door.cards

    return result


def single_door_cards(doors):
    counts = {}

    for door in doors:
        for card in door.cards:
            counts[card] = counts.get(card, 0) + 1

    return {card for card, count in counts.items() if count == 1}


def unused_cards(all_cards, doors):
    authorized = set()

    for door in doors:
        authorized |= door.cards

    return all_cards - authorized


def audit(doors):
    for door in doors:
        print(f"{door.name}: {len(door.cards)} cards")

    print(f"Master cards: {master_cards(doors)}")
    
lobby = Door("Lobby")
for c in [101, 102, 103, 104]:
    lobby.grant(c)
lab = Door("Lab")
for c in [101, 103, 105]:
    lab.grant(c)
server = Door("Server Room")
for c in [101, 105]:
    server.grant(c)
lab.revoke(105)
lab.revoke(999) # no error
print(lab.can_open(103), lab.can_open(105)) # True False
doors = [lobby, lab, server]
print(master_cards(doors)) # {101}
12 / 16
print(single_door_cards(doors)) # {102, 104}
print(unused_cards({101, 102, 105, 200}, doors)) # {200}
audit(doors)


# Problem 4

from abc import ABC, abstractmethod


class Shipment(ABC):

    def __init__(self, tracking_id, weight_kg):
        Shipment.validate_weight(weight_kg)

        self.tracking_id = tracking_id
        self.weight_kg = weight_kg

    @abstractmethod
    def cost(self):
        pass

    def label(self):
        return (
            f"{self.tracking_id} "
            f"({self.weight_kg} kg): "
            f"${self.cost():.2f}"
        )

    @staticmethod
    def validate_weight(weight_kg):
        if weight_kg <= 0:
            raise ValueError("Weight must be positive")


class StandardShipment(Shipment):

    def __init__(self, tracking_id, weight_kg,
                 rate_per_kg=2.0):
        super().__init__(tracking_id, weight_kg)
        self.rate_per_kg = rate_per_kg

    def cost(self):
        return self.weight_kg * self.rate_per_kg


class ExpressShipment(StandardShipment):

    def __init__(self, tracking_id, weight_kg,
                 rate_per_kg=2.0,
                 surcharge=10.0):
        super().__init__(
            tracking_id,
            weight_kg,
            rate_per_kg
        )
        self.surcharge = surcharge

    def cost(self):
        return super().cost() + self.surcharge


class InternationalShipment(Shipment):

    def __init__(self, tracking_id, weight_kg,
                 country,
                 customs_pct=0.15):
        super().__init__(tracking_id, weight_kg)
        self.country = country
        self.customs_pct = customs_pct

    def cost(self):
        return self.weight_kg * 5.0 * (
            1 + self.customs_pct
        )


def manifest(shipments):
    total = 0

    for shipment in shipments:
        print(shipment.label())
        total += shipment.cost()

    print(f"Total: ${total:.2f}")

    return total

shipments = [
StandardShipment("S100", 4.0),
ExpressShipment("E200", 2.5),
InternationalShipment("I300", 3.0, country="Canada"),
]
total = manifest(shipments)
# S100 (4.0 kg): $8.00
# E200 (2.5 kg): $15.00
# I300 (3.0 kg): $17.25
# Total: $40.25
try:
    Shipment.validate_weight(-1)
except ValueError as e:
    print("Caught:", e)
# Caught: Weight must be positive


# Problem 5 

class Polynomial:

    def __init__(self, coeffs):
        self.coeffs = coeffs[:]

    def __str__(self):
        terms = []

        for power in range(
            len(self.coeffs) - 1,
            -1,
            -1
        ):
            coeff = self.coeffs[power]

            if coeff == 0:
                continue

            if power == 0:
                terms.append(str(coeff))

            elif power == 1:
                if coeff == 1:
                    terms.append("x")
                else:
                    terms.append(f"{coeff}x")

            else:
                if coeff == 1:
                    terms.append(f"x^{power}")
                else:
                    terms.append(
                        f"{coeff}x^{power}"
                    )

        return " + ".join(terms)

    def __repr__(self):
        return f"Polynomial({self.coeffs})"
    def __len__(self):
        return len(self.coeffs)
    def __getitem__(self, i):
        if i >= len(self.coeffs):
            return 0
        return self.coeffs[i]
    def __call__(self, x):
        total = 0

        for power, coeff in enumerate(
            self.coeffs
        ):
            total += coeff * (x ** power)

        return total

    def __add__(self, other):
        size = max(
            len(self.coeffs),
            len(other.coeffs)
        )

        result = []

        for i in range(size):
            result.append(self[i] + other[i])

        return Polynomial(result)

    def __mul__(self, scalar):
        return Polynomial(
            [c * scalar for c in self.coeffs]
        )

    def degree(self):
        for i in range(
            len(self.coeffs) - 1,
            -1,
            -1
        ):
            if self.coeffs[i] != 0:
                return i
        return 0

    def __eq__(self, other):
        return self.degree() == other.degree()
    def __lt__(self, other):
        return self.degree() < other.degree()
    
p = Polynomial([1, 2, 3]) # 1 + 2x + 3x^2
q = Polynomial([0, 1]) # x
print(p) # 3x^2 + 2x + 1
print(q) # x
print(repr(p)) # Polynomial([1, 2, 3])
print(len(p)) # 3
print(p[2], p[7]) # 3 0
print(p(2)) # 17
print(q(5)) # 5
r = p + q
print(r) # 3x^2 + 3x + 1
print(p * 2) # 6x^2 + 4x + 2
print(p == Polynomial([5, 0, 1])) # True (both degree 2)
print(q < p) # True (degree 1 < degree 2)
