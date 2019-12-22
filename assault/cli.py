import click
from .http import assault
from .stats import Results
from typing import TextIO
import sys
import json


@click.command()
@click.option("--requests", "-r", default=500, help="Number of requests")
@click.option("--concurrency", "-c", default=1, help="Number of concurrent requests")
@click.option("--json-file", "-j", default=None, help="Path to output json file")
@click.argument("url")
def cli(requests, concurrency, json_file, url):
    output_file = None
    if json_file:
        try:
            output_file = open(json_file, "w")
        except:
            raise Exception("Unable to open json file")
    result_dicts, total_time = assault(url, requests, concurrency)
    results = Results(total_time, result_dicts)
    display(results, output_file)


def display(results: Results, json_file: TextIO):
    if json_file:
        # Write results to the json file
        json.dump(
            {
                "successful_requests": results.successful_requests(),
                "slowest": results.slowest(),
                "fastest": results.fastest(),
                "total_time": results.total_time,
                "requests_per_minute": results.request_per_minute(),
                "requests_per_second": results.request_per_second(),
            },
            json_file,
        )
        json_file.close()
        print("Done.....")
    # Print to screen
    print(".......... Done!")
    print(
        f"""
    ------ Results --------
    Successful requests {results.successful_requests()}
    Slowest             {results.slowest()}
    Fastest             {results.fastest()}
    Average             {results.average_time()}
    Total Time          {results.total_time}
    Requests per minute {results.request_per_minute()}
    Requests per second {results.request_per_second()}
    """
    )
