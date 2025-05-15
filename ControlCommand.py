from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ControlCommand:
    device: str
    action: int
    values: Optional[List[List[int]]] = None
