from typing import Dict
from abc import ABC, abstractmethod

class BalanceEditorInterface(ABC):

    @abstractmethod
    def edit(self, user_id: int, new_balance: float) -> Dict: pass