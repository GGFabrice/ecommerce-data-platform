from config.settings import RAW_DIR, CLEANSED_DIR

from pipelines.cleaning import CleaningPipeline

pipeline = CleaningPipeline(
    RAW_DIR,
    CLEANSED_DIR
)

pipeline.run()