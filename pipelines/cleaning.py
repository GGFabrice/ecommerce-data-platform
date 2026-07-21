from pathlib import Path
import pandas as pd

from pipelines.pipeline import Pipeline


class CleaningPipeline(Pipeline):

    def __init__(self, input_folder: Path, output_folder: Path):
        self.input_folder = input_folder
        self.output_folder = output_folder

    def run(self):
        self.output_folder.mkdir(parents=True, exist_ok=True)

        for file in self.input_folder.glob("*.csv"):

            print(f"Nettoyage : {file.name}")

            df = pd.read_csv(file)

            # supprimer les doublons
            df = df.drop_duplicates()

            # supprimer les lignes entièrement vides
            df = df.dropna(how="all")

            output = self.output_folder / file.name

            df.to_csv(output, index=False)

        print("Pipeline de nettoyage terminé.")