# Windows Shutdown Control

### A simple GUI-based Windows application to schedule system actions like shutdown, restart, log off, or hibernate after a set time.

---

## Features

- **Set Timer**: Specify hours, minutes, and seconds until the action occurs.
- **Choose Action**: Options to:
  - Shutdown
  - Restart
  - Log Off
  - Hibernate
- **Countdown Display**: Shows the remaining time until the chosen action.
- **Cancel Timer**: Cancel the scheduled action anytime before the countdown ends.
- **Warning Notifications**: Option to receive a warning notification before the system action is executed.
- **Error Handling**: Ensures invalid inputs (e.g., negative time or zero time) are properly handled.

## How to Use

1. **Download the Executable**:
   - Download the `.exe` file from the [Releases](https://github.com/jerankda/shutdown_control/releases/tag/release) section of this repository.
   - No installation required; just run the executable directly.

2. **Set the Timer**:
   - Enter the desired time (hours, minutes, and seconds).
   - Select the action you want to perform (Shutdown, Restart, Log Off, Hibernate).
   - Optionally enable warning notifications before the action is triggered.

3. **Start Timer**:
   - Click "Start Timer" to start the countdown.
   - The remaining time will be displayed.

4. **Cancel the Timer**:
   - Click "Cancel Shutdown" to abort the scheduled action at any time.

## How to Build From Source

If you prefer to run the Python source code or build the executable yourself:

### Prerequisites:

- **Python 3.x** must be installed on your system.
- Install the required dependencies by running:
  ```bash
  pip install tkinter

## Running the Source Code:
Clone this repository or download the shutdown_timer.py file.

```bash
git clone https://github.com/your-username/shutdown-timer.git
cd shutdown-timer
```

## Run the script:

```bash
python shutdown_timer.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.


