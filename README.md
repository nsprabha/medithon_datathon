# Medithon_datathon

## Problem Statement 4:
There is a critical need for a reliable method to accurately track insulin injection times for individuals with diabetes to prevent insulin overdose and underdosage, ultimately improving diabetes management and reducing associated health risks.

## Innovation

- Precision Monitoring: MPU 9250 (Pressure sensor) and BMP 280 (Accelerometre) track the exact amount of insulin administered.

- Real-time Tracking: Bluetooth-enabled insulin pin allows seamless monitoring via a mobile app.

- Safety Assurance: GPIO pin as a touch sensor ensuresinsulin is injected only when the needle fully contacts the skin.

- Data Logging: Integrated clock module records the precise dosage and time of insulin administration for accurate tracking.

## Working process

- Prepare the Device: Fill the insulin cartridge and change the needle as required.

- Power On and Connect: Once the module is powered on, it automatically connects to the mobile app. All
stored data is refreshed.

- Connection Confirmation: A blue light indicates successful Bluetooth connection with the app, accompanied
by a buzzer sound for 2 seconds.

- Insulin Level Setting: While adjusting the knob to set the insulin dosage, the red and blue lights blink, and the buzzer remains on. Once the desired level is set, the lights stop blinking, the blue light remains on, and the buzzer turns off.

Injection Process:

- When the needle touches the skin, the GPIO touch sensor triggers, turning off the blue light.

- After the full insulin dose is injected, a beep sound confirms completion.

- Data Storage: With the help of the clock module, the ESP32-C3 stores all data, including the precise insulin dosage and time of injection.

Post-Injection: Safely remove the disposable needle after the injection.
