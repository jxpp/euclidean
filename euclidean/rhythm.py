from typing import Dict, List

from dataclasses import asdict, dataclass


def _compute_bitmap(num_slots, num_pulses):
    """  Taken from
    `https://web.archive.org/web/20100528023736/https://ics-web.sns.ornl.gov/timing/Rep-Rate%20Tech%20Note.pdf`
    """
    divisor = num_slots - num_pulses
    remainder = [num_pulses]
    count = []
    level = 0

    # this is a kinda hacky do while, i hate it
    while True:
        count.append(divisor // remainder[level])
        remainder.append(divisor % remainder[level])
        divisor = remainder[level]
        level += 1
        if remainder[level] <= 1:
            break

    count.append(divisor)

    def _build_string(bitmap, level):
        if level == -1:
            return bitmap + '0'
        elif level == -2:
            return bitmap + '1'
        else:
            for _ in range(count[level]):
                bitmap = _build_string(bitmap, level - 1)
            if remainder[level] != 0:
                bitmap = _build_string(bitmap, level - 2)
            return bitmap
    bitmap = _build_string('', level)

    # The algorithm described has the output shifted from where we want it
    try:
        offset = bitmap.index('1')
    except ValueError:  # in case of no ones
        offset = 0
    bitmap = bitmap[offset:] + bitmap[:offset]

    return bitmap


def _bitmap_to_bool_list(bitmap: str) -> List[bool]:
    return [bool(int(s)) for s in bitmap]


@dataclass
class EuclideanRhythm:
    """ Class for handling euclidean rhythms defined by the number of total
    steps, the number of active steps and the offset of the cycle.
    """
    steps: int
    active: int
    offset: int

    def __post_init__(self):
        if self.active > self.steps:
            raise ValueError('The amount of active steps cannot be greater '
                             'than the amount of total steps')
        if not (0 <= self.offset < self.steps):
            raise ValueError('The offset has to be between 0 and the amount of '
                             'total steps')

    @classmethod
    def from_gates(cls, gates: List[bool]) -> 'EuclideanRhythm':
        """ Generate the euclidean rhythm that corresponds to a series of
        gates.
        """
        # FIXME: this is a dumb implementation that doesn't work until I
        #        figure out the inverse algorithm
        steps = len(gates)
        active = gates.count(True)
        try:
            offset = gates.index(True)
        except ValueError:
            offset = 0

        return cls(steps, active, offset)

    def to_gates(self) -> List[bool]:
        """ Convert the euclidean rhythm to a series of gates
        """
        bitmap = _compute_bitmap(self.steps, self.active)
        gate_list = _bitmap_to_bool_list(bitmap)
        gates = gate_list[self.offset:] + gate_list[:self.offset] if self.offset > 0 else gate_list

        return gates

    def as_dict(self) -> Dict[str, int]:
        """ Return the rhythm as a dictionary
        """
        return asdict(self) 
