import time

def bigo_n(filename: str):
    """Writes to a file benchmarking data of O(n)

    :param filename: Input filename no need to add the extensions
    """

    # Open a file based on its name
    with open(filename +'.txt', 'w') as f:

        # Increment the number of items to be added to a list
        for i in range(1, 11):
            items_to_add = 10_000 * i
            sample_list = []

            # Get 10 datapoints 
            for t in range(10):

                # Benchmark how many times it takes for number of items it takes to add to list
                start = time.perf_counter_ns()
                for j in range(items_to_add):
                    sample_list.append(j)
                end = time.perf_counter_ns()

                # Write output to a file 
                f.write(f'{items_to_add}\t{(end-start)/1E6}\n')

bigo_n('example')



