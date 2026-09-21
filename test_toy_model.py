import unittest

from toy_model import Parameters, State, simulate, step


class ToyModelTests(unittest.TestCase):
    def test_states_remain_bounded(self):
        trajectory = simulate(months=120)
        for row in trajectory:
            for name, value in row.items():
                if name != "month":
                    self.assertGreaterEqual(value, 0.0)
                    self.assertLessEqual(value, 1.0)

    def test_stronger_correction_improves_performance(self):
        initial = State(concern=0.5, maintenance=0.8)
        weak = step(initial, Parameters(correction=0.02))
        strong = step(initial, Parameters(correction=0.20))
        self.assertGreater(strong.performance, weak.performance)

    def test_negative_horizon_is_rejected(self):
        with self.assertRaises(ValueError):
            simulate(months=-1)


if __name__ == "__main__":
    unittest.main()

