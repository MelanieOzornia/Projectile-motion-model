# Projectile Motion Model
This project takes user inputs and creates a visual model of the motion. 
It also computes the time of flight, max height, horizontal displacement, and final velocity.

## Features:
- Inputs: launch speed, angle, initial position, final height
- Find x and y positions based on a specific lookup time
- Visual Plot of position as projectile moves through space

## How to run:

**Requirements:** Python 3 (3.11 or newer recommended, since `requirements.txt` pins recent package versions).

### 1. Get the code

```
git clone https://github.com/MelanieOzornia/Projectile-motion-model.git
cd Projectile-motion-model
```

### 2. (Optional) Create a virtual environment

**macOS / Linux**
```
python3 -m venv myenv
source myenv/bin/activate
```

**Windows (Command Prompt)**
```
python -m venv myenv
myenv\Scripts\activate
```

**Windows (PowerShell)**
```
python -m venv myenv
myenv\Scripts\Activate.ps1
```

### 3. Install the dependencies

```
pip install -r requirements.txt
```

### 4. Run the program

**macOS / Linux**
```
python3 main.py
```

**Windows**
```
python main.py
```

(If `python` isn't recognized on Windows, try `py main.py`.)

## Example:
<img width="1010" height="290" alt="Screenshot 2026-11-16 at 8 09 36 PM" src="https://github.com/user-attachments/assets/94df569e-56a5-480f-89b7-d80ed73ef309" />
<img width="2990" height="1344" alt="Screenshot 2026-11-16 at 8 09 51 PM" src="https://github.com/user-attachments/assets/0f0081a8-5915-436f-b695-afe073609d45" />
Inputs: 50 m/s, 50°, start at origin, final height 0, lookup at 0.5 s


## Limitations:
- ideal motion (no air resistance, g= 9.81)
- final height assumes launch starts from ground level
  
## Planned Features:
- Flexibility with starting height
- Adding air drag / comparing motion with drag vs ideal
- Adding a valid time range before you search up a position at a specific time
- Adding animations to the plot line



