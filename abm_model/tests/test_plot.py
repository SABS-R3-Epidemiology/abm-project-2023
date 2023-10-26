# import sys
import unittest
from unittest import TestCase
from unittest.mock import patch, mock_open
from abm_model.plot import Plotter
import csv


class TestPlot(TestCase):

    def setUp(self) -> None:
        self.plot = Plotter()
        self.data = "Time,Susceptible,Infected,Recovered\n"
        self.data += "1, 90, 10, 0\n"
        self.data += "2, 79, 20, 1"

    def test__init__(self):
        self.plot = Plotter(csv_file_name='plot_data_test.csv')
        self.assertEqual(self.plot.csv_file_name, "plot_data_test.csv")

    def test_plot_data(self):
        with patch('builtins.open', new_callable=mock_open, read_data=self.data) as mock_file:
            self.plot = Plotter(csv_file_name='plot_data_test.csv')
            read_data = open("data/" + self.plot.csv_file_name).read()
            assert read_data == self.data
            # print(read_data)
            mock_file.assert_called_with("data/plot_data_test.csv")

            rows = read_data.splitlines()
            reader = csv.reader(rows, delimiter=',')
            read_data = []
            for row in reader:
                read_data.append(row)
                self.assertEqual(len(row), 4)

            self.assertEqual(read_data[0][0], 'Time')
            self.assertEqual(read_data[0][1], 'Susceptible')
            self.assertEqual(read_data[0][2], 'Infected')
            self.assertEqual(read_data[0][3], 'Recovered')

    @patch('plot.plt')
    def test_create_plot_legend(self, mock_plt):
        # Plotter.plot_data(self.plot)
        # assert mock_plt.legend.called
        mock_plt.xlabel.assert_called_once_with("Time step")
        mock_plt.ylabel.assert_called_once_with("Number of individuals")


if __name__ == '__main__':

    unittest.main()
