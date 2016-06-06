import movie_service_resources
import movie_service_pb2
import logging
import os
import timeit
import time
import datetime


class SerializationTest:
    def __init__(self):
        self.db = movie_service_resources.read_movie_service_database()
        # print(str(self.db))
        logger = logging.getLogger('SerilizationTest')
        logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        directory = "Logging"
        if not os.path.exists(directory):
            os.makedirs(directory)
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%HH%MM%SS')
        filepath = directory + "//Serialization_" + st + ".log"

        fh = logging.FileHandler(filepath)
        fh.setLevel(logging.INFO)
        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)  # handler = PingHandler()
        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # add the handlers to the logger
        logger.addHandler(fh)
        logger.addHandler(ch)
        self.logger = logger

    def run(self):

        response = movie_service_pb2.MoviesInTheaterResponse(movies=self.db)
        bytes = response.SerializeToString()
        self.logger.log(logging.INFO, "serialized length: %s", str(len(bytes)))

        total_ser = 0
        total_deser = 0
        n = 10000
        for i in range(0, n):
            tic = timeit.default_timer()
            b = response.SerializeToString()
            elapsed = timeit.default_timer() - tic
            total_ser = total_ser + elapsed
            tic2 = timeit.default_timer()
            m = movie_service_pb2.MoviesInTheaterResponse()
            m.ParseFromString(b)
            elapsed2 = timeit.default_timer() - tic2
            # print (str(m));
            total_deser = total_deser + elapsed2

        avg_ser = (total_ser*(10**9))/n
        avg_deser = (total_deser*(10**9))/n
        self.logger.log(logging.INFO, "Serialization time: \n%s", avg_ser)
        self.logger.log(logging.INFO, "De-serialization time: \n%s", avg_deser)


if __name__ == '__main__':
    tester = SerializationTest()
    for j in range(0, 10):
        tester.logger.log(logging.INFO, "*** ITERATION %s ***", j)
        tester.run()
    tester.logger.log(logging.INFO, "######### FINISHED ##########")
