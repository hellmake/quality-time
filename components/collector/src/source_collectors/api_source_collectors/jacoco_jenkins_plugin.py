"""Jacoco Jenkins plugin coverage report collector."""

from abc import ABC

from base_collectors import JenkinsPluginSourceUpToDatenessCollector, SourceCollector
from collector_utilities.type import URL
from source_model import SourceMeasurement, SourceResponses


class JacocoJenkinsPluginBaseClass(SourceCollector, ABC):  # skipcq: PYL-W0223
    """Base class for Jacoco Jenkins plugin collectors."""

    async def _landing_url(self, responses: SourceResponses) -> URL:
        return URL(f"{await super()._api_url()}/lastSuccessfulBuild/jacoco")


class JacocoJenkinsPluginCoverageBaseClass(JacocoJenkinsPluginBaseClass):
    """Base class for Jacoco Jenkins plugin coverage collectors."""

    coverage_type = "subclass responsibility"

    async def _api_url(self) -> URL:
        return URL(f"{await super()._api_url()}/lastSuccessfulBuild/jacoco/api/json")

    async def _parse_source_responses(self, responses: SourceResponses) -> SourceMeasurement:
        coverage = (await responses[0].json())[f"{self.coverage_type}Coverage"]
        return SourceMeasurement(value=str(coverage["missed"]), total=str(coverage["total"]))


class JacocoJenkinsPluginUncoveredLines(JacocoJenkinsPluginCoverageBaseClass):
    """Collector for Jacoco Jenkins plugin uncovered lines."""

    coverage_type = "line"


class JacocoJenkinsPluginUncoveredBranches(JacocoJenkinsPluginCoverageBaseClass):
    """Collector for Jacoco Jenkins plugin uncovered branches."""

    coverage_type = "branch"


class JacocoJenkinsPluginSourceUpToDateness(JacocoJenkinsPluginBaseClass, JenkinsPluginSourceUpToDatenessCollector):
    """Collector for the up to dateness of the Jacoco Jenkins plugin coverage report."""
