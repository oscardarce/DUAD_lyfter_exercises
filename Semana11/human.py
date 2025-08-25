class Torso:
    def __init__(self, head, right_leg, right_arm, left_leg, left_arm):
        self.head = head
        self.right_leg = right_leg
        self.right_arm = right_arm
        self.left_leg = left_leg
        self.left_arm = left_arm


class Hand:
    def __init__(self, left_or_right):
        self.left_or_right = left_or_right


class Foot:
    def __init__(self, left_or_right):
        self.left_or_right = left_or_right


class Arm:
    def __init__(self, hand):
        self.hand = hand
        print(
            f"Tienes la mano {hand.left_or_right} y el brazo pegado al torso")


class Leg:
    def __init__(self, foot):
        self.foot = foot
        print(
            f"Tienes el pie {foot.left_or_right} y la pierna pegado al torso")


class Head:
    def __init__(self):
        print("La cabeza está pegada al torso")


left_hand = Hand("Izquierda")
left_arm = Arm(left_hand)

right_hand = Hand("Derecha")
right_arm = Arm(right_hand)

right_foot = Foot("Derecho")
right_leg = Leg(right_foot)

left_foot = Foot("Izquierda")
left_leg = Leg(left_foot)

head = Head()

torso = Torso(head, right_leg, right_arm, left_leg, left_arm)

print(torso)
