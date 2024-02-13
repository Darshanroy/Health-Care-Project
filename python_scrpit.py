import os

def create_project_template():
    """
    Creates a project template with specified folders and files.

    Parameters: None

    Returns: None
    """
    folders = ["src", "steps","pipelines",'artifacts',"data-imgs",]
    files = ["steps/DataIngestionStep.py","steps/DataProcessingStep.py"     ,"steps/ModelTrainingStep.py","steps/ModelEvaluvationStep.py","src/DataIngestion.py","src/DataProcessing.py" ,"src/ModelTraining.py","src/ModelEvaluvation.py"]

    # Create folders
    for folder in folders:
        os.makedirs(folder)

    # Create files
    for file in files:
        with open(file, 'w') as f:
            pass  # You can write content to the files if needed


if __name__ == "__main__":
    create_project_template()
