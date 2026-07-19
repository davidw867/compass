from dataclasses import dataclass

from .severity import Severity


@dataclass
class Result:

    severity: Severity

    message: str
