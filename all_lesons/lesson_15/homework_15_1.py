

class Rhombus:
    def __init__(self, side_a, angle_a):

        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):

        if name == 'side_a':
            if value <= 0:
                raise ValueError("Side must be greater than 0.")

        elif name == 'angle_a':
            if not (0 < value < 180):
                raise ValueError("Angle must be between 0 and 180.")

            # Set angle_b automatically to satisfy the rhombus angle property
            super().__setattr__('angle_b', 180 - value)

        elif name == "angle_b":
            raise AttributeError("You cannot set 'angle_b' directly. It is calculated based on 'angle_a'.")

        # Set the attribute value to avoid recursion
        super().__setattr__(name, value)


# rhombus = Rhombus(side_a=25, angle_a=20)
#
# print(f"side_a: {rhombus.side_a}")  # Outputs: side_a: 25
# print(f"angle_a: {rhombus.angle_a}")  # Outputs: angle_a: 20
# print(f"angle_b: {rhombus.angle_b}")  # Outputs: angle_b: 160

