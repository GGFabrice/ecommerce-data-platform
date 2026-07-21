from abc import ABC, abstractmethod

class Pipeline(ABC):
    """
    Classe de base pour tous les pipelines.
    """

    @abstractmethod
    def run(self):
        pass