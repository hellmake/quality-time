"""HQ metrics collector."""

import requests

from collector.collector import Collector
from collector.type import Measurement


class HQViolations(Collector):
    """HQ violations collector."""

    def parse_source_response(self, response: requests.Response, **parameters) -> Measurement:
        metric = [m for m in response.json()["metrics"] if m["stable_metric_id"] == parameters.get("metric_id")][0]
        return metric["value"]