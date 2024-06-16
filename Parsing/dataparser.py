import Parsing.datatypes as dt
import re


class DataParser:
    # File path of the data to be parsed
    filePath: str = None

    # Data that was read from the file provided
    fileData: list[str] = []

    parsedData: dt.ParsedCyclictestData = None

    # Constructor
    def __init__(self, file_path):
        self.filePath = file_path
        self.parsedData = dt.ParsedCyclictestData()

    def read_file(self) -> None:
        try:
            latency_file = open(self.filePath, "r")

            # Place every line individually into mem
            for line in latency_file:
                # Clean the lines from trailing whitespace etc
                self.fileData.append(line.strip())
        except FileNotFoundError:
            return -1

    # Returns FileData object containing all information that was parsed from the file
    def get_data(self) -> dt.ParsedCyclictestData:
        return self.parsedData

    def parse_data(self):
        # Test whether we are trying to parse valid histogram data
        if not self.fileData[0].startswith("# Histogram"):
            return -1
        for line in self.fileData:
            # Find the total amount of samples
            if re.search("^# Total:", line) is not None:
                # The value is the same across all processors, so we can just take it from second position
                self.parsedData.totalCount = int(line.split(" ")[2])
            # Filter for data lines (they start with a numeric value)
            elif re.search("^[0-9]", line) is not None:
                # The index is at the very beginning of the line, padded with zeroes
                # We can use the space following the index as the delimiter
                current_index = int(line.split(" ")[0])

                # The values are split per processor, with a tab symbol
                current_values = [int(x) for x in line.split(" ")[1].split("\t")]
                self.parsedData.values.insert(current_index, current_values)

        # Continue computing the statistical data from those functions
        self.parsedData.compute_minimum_latency()
        self.parsedData.compute_maximum_latency()
        self.parsedData.compute_averages()
        self.parsedData.compute_standard_deviations()
