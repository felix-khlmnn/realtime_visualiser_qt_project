import numpy as np


class ParsedCyclictestData:
    values: list[list[int]] = []
    totalCount: int = None
    minimumLatencies: list[int] = []
    maximumLatencies: list[int] = []
    averageLatencies: list[float] = []
    standardDeviations: list[float] = []

    # Minimum latency per core
    def compute_minimum_latency(self):
        """
        Get the total number of processors
        This can be derived from the values list, as each processor gets one entry in each entry
        The length of this array should ideally be the same across every entry, hence we can derive the value from
        the first element alone.
        :return:
        """
        number_of_processors = len(self.values[0])

        # Determine the minimum latency per processor
        for processor in range(number_of_processors):
            current_minimum = 0
            for index, entry in enumerate(self.values):
                # Stop the count if we find a latency count unequal to 0
                if entry[processor] != 0:
                    break
                current_minimum += 1
            # Store the calculated minimum per processor
            self.minimumLatencies.insert(processor, current_minimum)

    def compute_maximum_latency(self):
        # This function is basically analogous to the minimum function
        number_of_processors = len(self.values[0])

        # In order to find the maximum latency, we reverse the value list and determine the index at which the first
        # nonzero value occurs. By determining the total dataset count, we can then calculate the index at which the
        # maximum lies
        total_count_of_datasets = len(self.values)

        for processor in range(number_of_processors):
            # This value has to be subtracted from the total count of datasets to determine the actual index of the max
            # latency. Our temporary value has to start at one
            temporary_maximum = 1

            for index, entry in enumerate(self.values[::-1]):
                # Stop the count if we find a latency count unequal to 0
                if entry[processor] != 0:
                    break
                temporary_maximum += 1
            # Compute the maximum and store it
            maximum_latency = total_count_of_datasets - temporary_maximum
            self.maximumLatencies.insert(processor, maximum_latency)

    def clear(self):
        self.values = []

    def compute_averages(self):
        number_of_processors = len(self.values[0])

        print("Number of processors:", number_of_processors)

        for processor in range(number_of_processors):

            # Reformat the data for numpy, since the frequency of a latency can be viewed as its weight
            indices = []
            processor_latencies = []

            for index, entry in enumerate(self.values):
                #print(entry)
                indices.append(index)
                processor_latencies.append(entry[processor])

            # Convert the lists to numpy arrays
            indices = np.array(indices)
            processor_latencies = np.array(processor_latencies)

            average_latency_of_processor = np.average(indices, weights=processor_latencies)

            self.averageLatencies.insert(processor, average_latency_of_processor)

    def compute_standard_deviations(self):
        number_of_processors = len(self.values[0])

        for processor in range(number_of_processors):

            indices = []
            processor_latencies = []

            for index, entry in enumerate(self.values):
                indices.append(index)
                processor_latencies.append(entry[processor])

            # Convert the lists to numpy arrays
            indices = np.array(indices)
            processor_latencies = np.array(processor_latencies)

            std_per_processor = np.sqrt(np.average((indices - np.average(indices, weights=processor_latencies)) ** 2, weights=processor_latencies))

            # Store the standard deviation of each processor
            self.standardDeviations.insert(processor, std_per_processor)
