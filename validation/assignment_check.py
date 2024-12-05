import unittest

from working.assignment import sort_test, create_a_list_test, stack_test, queue_test


class TestFunctions(unittest.TestCase):
    def test_create_a_list_test(self):
        result = create_a_list_test()
        self.assertEqual(len(result), 5)
        self.assertTrue(
            all(
                isinstance(item, dict) and
                set(item.keys()) == {'nama', 'domisili', 'suku'}
                for item in result
            )
        )
        names = [item['nama'] for item in result]
        domisilis = [item['domisili'] for item in result]
        sukus = [item['suku'] for item in result]

        self.assertEqual(len(names), len(set(names)))
        self.assertEqual(len(domisilis), len(set(domisilis)))
        self.assertEqual(len(sukus), len(set(sukus)))

    def test_sort_test(self):
        data_acak = [
            {"nama": "Dina", "umur": 22, "teman": ["Budi", "Ali"]},
            {"nama": "Ali", "umur": 25, "teman": ["Dina"]},
            {"nama": "Citra", "umur": 22, "teman": ["Ali", "Budi", "Citra"]},
            {"nama": "Ali", "umur": 20, "teman": ["Dina", "Citra"]},
            {"nama": "Budi", "umur": 30, "teman": ["Dina"]},
            {"nama": "Citra", "umur": 20, "teman": ["Ali"]},
        ]

        sort_test(data_acak)
        expected = [
            {"nama": "Citra", "umur": 22, "teman": ["Ali", "Budi", "Citra"]},
            {"nama": "Ali", "umur": 20, "teman": ["Dina", "Citra"]},
            {"nama": "Dina", "umur": 22, "teman": ["Budi", "Ali"]},
            {"nama": "Ali", "umur": 25, "teman": ["Dina"]},
            {"nama": "Budi", "umur": 30, "teman": ["Dina"]},
            {"nama": "Citra", "umur": 20, "teman": ["Ali"]}
        ]
        self.assertEqual(data_acak, expected)

    def test_stack_test(self):
        result = stack_test("string")
        self.assertEqual(result, "gnirts")
        result_empty = stack_test("")
        self.assertEqual(result_empty, "")

    def test_queue_test(self):
        result = queue_test([5, 3, 8, 2, 6])
        self.assertEqual(result, (14, 10))  # Lane 1 = 5+6+3, Lane 2 = 8+2

        result_empty = queue_test([])
        self.assertEqual(result_empty, (0, 0))

        result_single = queue_test([7])
        self.assertEqual(result_single, (7, 0))


if __name__ == "__main__":
    unittest.main()
