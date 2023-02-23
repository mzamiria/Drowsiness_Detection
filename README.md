# Drowsiness_Detection
This app receives live video feed from the host's camera, detects the human face, human eyes and the state of the eyes(open/closed). If both eyes are closed for period of 10 video frames or more,it will issue a "WAKE UP!" warning.

To run the app follow these steps:

Fork the repository to your repository: (https://docs.github.com/en/get-started/quickstart/fork-a-repo)
Clone the repo on your server using the command: git clone < repo http >
In the command line create a new virtual environment: python venv -m .venv
Activate the environment by following command: .venv\Scripts\activate.bat for windows , other OSes source .venv/bin/activate
cd the cloned repository and install requirement packages: cd path\to\cloned\repository\pip install -r requirements.txt
Run the main.py file in the app folder : cd app\python main.py open your browser and open the http:// address refered in the command line.
Warning: Sometimes the video feed might not be received properly. To fix the issue just refresh the http:// tap.
