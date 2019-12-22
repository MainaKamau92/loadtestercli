from typing import List, Dict
from statistics import mean


class Results:
    """
    Results handles calculating stats based on a list of requests that were made.
    Here's an example of what the info will look like:

    Successful requests    500
    Slowest                0.010s
    Fastest                0.001s
    Average                0.003s
    Total time             0.020s
    Results per minute    48360
    Results per second    80
    """

    def __init__(self, total_time: float, requests: List[Dict]):
        self.total_time = total_time
        self.requests = sorted(requests, key=lambda r: r["request_time"])

    def slowest(self) -> float:
        """
        Returns the slowest request's completion time

        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4,
        ... },{
        ...     'status_code': 500,
        ...     'request_time': 6.1,
        ... },{
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }])
        >>> results.slowest()
        6.1
        """
        return self.requests[-1]["request_time"]

    def fastest(self) -> float:
        """
        Returns the fastest request's completion time

        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4,
        ... },{
        ...     'status_code': 500,
        ...     'request_time': 6.1,
        ... },{
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }])
        >>> results.fastest()
        1.04
        """
        return self.requests[0]["request_time"]

    def average_time(self) -> float:
        """
        Returns the average requests completion time

        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4,
        ... },{
        ...     'status_code': 500,
        ...     'request_time': 6.1,
        ... },{
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }])
        >>> results.average_time()
        3.513333333333333
        """
        return mean([i["request_time"] for i in self.requests])

    def successful_requests(self) -> int:
        """
        Returns the total number of successful requests

        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4,
        ... },{
        ...     'status_code': 500,
        ...     'request_time': 6.1,
        ... },{
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }])
        >>> results.successful_requests()
        2
        """

        return len([i for i in self.requests if i["status_code"] in range(200, 299)])

    def request_per_minute(self) -> float:
        """
        Returns the total number of requests per minute

        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4,
        ... },{
        ...     'status_code': 500,
        ...     'request_time': 6.1,
        ... },{
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }])
        >>> results.request_per_minute()
        17.077798861480076
        """
        # use the formula C * r / tt where C is the constant i.e 60 secs r is the number of requests and tt is the
        # total time taken by the rs(requests)
        return (60 * len(self.requests)) / sum(
            [i["request_time"] for i in self.requests]
        )

    def request_per_second(self) -> float:
        """
        Returns the total number of requests in a second

        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4,
        ... },{
        ...     'status_code': 500,
        ...     'request_time': 6.1,
        ... },{
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }])
        >>> results.request_per_second()
        0.28462998102466797
        """
        # use the formula C * r / tt where C is the constant i.e 1 sec r is the number of requests and tt is the
        # total time taken by the rs(requests)
        return (1 * len(self.requests)) / sum(
            [i["request_time"] for i in self.requests]
        )
