from abc import ABC, abstractmethod

# -----------------------------
# Base Abstract Class
# -----------------------------
class Device(ABC):
    def __init__(self, device_id, name):
        self.__device_id = device_id
        self.__name = name
        self.__status = False

    def get_id(self):
        return self.__device_id

    def get_name(self):
        return self.__name

    def get_status(self):
        return "ON" if self.__status else "OFF"

    def turn_on(self):
        self.__status = True
        print(f"{self.__name} turned ON.")

    def turn_off(self):
        self.__status = False
        print(f"{self.__name} turned OFF.")

    @abstractmethod
    def display(self):
        pass


# -----------------------------
# Light Class
# -----------------------------
class Light(Device):
    def __init__(self, device_id, name, brightness=50):
        super().__init__(device_id, name)
        self.brightness = brightness

    def set_brightness(self, value):
        self.brightness = value
        print("Brightness set to", value)

    def display(self):
        print(f"Light: {self.get_name()} | Status: {self.get_status()} | Brightness: {self.brightness}")


# -----------------------------
# Fan Class
# -----------------------------
class Fan(Device):
    def __init__(self, device_id, name, speed=1):
        super().__init__(device_id, name)
        self.speed = speed

    def set_speed(self, speed):
        self.speed = speed
        print("Fan speed set to", speed)

    def display(self):
        print(f"Fan: {self.get_name()} | Status: {self.get_status()} | Speed: {self.speed}")


# -----------------------------
# Air Conditioner Class
# -----------------------------
class AirConditioner(Device):
    def __init__(self, device_id, name, temperature=24):
        super().__init__(device_id, name)
        self.temperature = temperature

    def set_temperature(self, temp):
        self.temperature = temp
        print("Temperature set to", temp)

    def display(self):
        print(f"AC: {self.get_name()} | Status: {self.get_status()} | Temp: {self.temperature}°C")


# -----------------------------
# Door Lock Class
# -----------------------------
class DoorLock(Device):
    def __init__(self, device_id, name):
        super().__init__(device_id, name)
        self.locked = True

    def lock(self):
        self.locked = True
        print("Door Locked")

    def unlock(self):
        self.locked = False
        print("Door Unlocked")

    def display(self):
        state = "Locked" if self.locked else "Unlocked"
        print(f"Door Lock: {self.get_name()} | {state}")


# -----------------------------
# Security Camera Class
# -----------------------------
class SecurityCamera(Device):
    def __init__(self, device_id, name):
        super().__init__(device_id, name)
        self.recording = False

    def start_recording(self):
        self.recording = True
        print("Recording Started")

    def stop_recording(self):
        self.recording = False
        print("Recording Stopped")

    def display(self):
        state = "Recording" if self.recording else "Idle"
        print(f"Camera: {self.get_name()} | {state}")


# -----------------------------
# User Class
# -----------------------------
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        return self.username == username and self.password == password


# -----------------------------
# Smart Home Class
# -----------------------------
class SmartHome:
    def __init__(self):
        self.devices = []
        self.logs = []

    def add_device(self, device):
        self.devices.append(device)
        self.logs.append(device.get_name() + " added.")
        print("Device Added Successfully.")

    def remove_device(self, device_id):
        for device in self.devices:
            if device.get_id() == device_id:
                self.devices.remove(device)
                self.logs.append(device.get_name() + " removed.")
                print("Device Removed.")
                return
        print("Device Not Found.")

    def show_devices(self):
        if not self.devices:
            print("No Devices Available")
        else:
            for device in self.devices:
                device.display()
                
    # -----------------------------
    # Turn Device ON
    # -----------------------------
    def turn_on_device(self, device_id):
        for device in self.devices:
            if device.get_id() == device_id:
                device.turn_on()
                self.logs.append(device.get_name() + " turned ON.")
                return
        print("Device Not Found.")

    # -----------------------------
    # Turn Device OFF
    # -----------------------------
    def turn_off_device(self, device_id):
        for device in self.devices:
            if device.get_id() == device_id:
                device.turn_off()
                self.logs.append(device.get_name() + " turned OFF.")
                return
        print("Device Not Found.")

    # -----------------------------
    # Show Logs
    # -----------------------------
    def show_logs(self):
        print("\n===== Activity Logs =====")
        if not self.logs:
            print("No Activity Yet.")
        else:
            for log in self.logs:
                print("-", log)


# -----------------------------
# Main Program
# -----------------------------
def main():

    print("=" * 40)
    print(" SMART HOME MANAGEMENT SYSTEM ")
    print("=" * 40)

    admin = User("admin", "1234")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if not admin.login(username, password):
        print("Invalid Username or Password")
        return

    print("\nLogin Successful!")

    home = SmartHome()

    # Default Devices
    home.add_device(Light(1, "Living Room Light"))
    home.add_device(Fan(2, "Bedroom Fan"))
    home.add_device(AirConditioner(3, "Hall AC"))
    home.add_device(DoorLock(4, "Main Door"))
    home.add_device(SecurityCamera(5, "Front Camera"))

    while True:

        print("\n")
        print("=" * 40)
        print("1. Show All Devices")
        print("2. Turn ON Device")
        print("3. Turn OFF Device")
        print("4. Add Device")
        print("5. Remove Device")
        print("6. View Activity Logs")
        print("7. Exit")
        print("=" * 40)

        choice = input("Enter Choice: ")

        if choice == "1":
            home.show_devices()

        elif choice == "2":
            try:
                device_id = int(input("Enter Device ID: "))
                home.turn_on_device(device_id)
            except ValueError:
                print("Invalid Input")

        elif choice == "3":
            try:
                device_id = int(input("Enter Device ID: "))
                home.turn_off_device(device_id)
            except ValueError:
                print("Invalid Input")

        elif choice == "4":

            print("\nSelect Device Type")
            print("1. Light")
            print("2. Fan")
            print("3. Air Conditioner")
            print("4. Door Lock")
            print("5. Security Camera")

            option = input("Choice: ")

            try:
                device_id = int(input("Device ID: "))
            except ValueError:
                print("Invalid ID")
                continue

            name = input("Device Name: ")

            if option == "1":
                brightness = int(input("Brightness: "))
                home.add_device(Light(device_id, name, brightness))

            elif option == "2":
                speed = int(input("Fan Speed: "))
                home.add_device(Fan(device_id, name, speed))

            elif option == "3":
                temp = int(input("Temperature: "))
                home.add_device(AirConditioner(device_id, name, temp))

            elif option == "4":
                home.add_device(DoorLock(device_id, name))

            elif option == "5":
                home.add_device(SecurityCamera(device_id, name))

            else:
                print("Invalid Option")

        elif choice == "5":

            try:
                device_id = int(input("Enter Device ID: "))
                home.remove_device(device_id)
            except ValueError:
                print("Invalid Input")

        elif choice == "6":
            home.show_logs()

        elif choice == "7":
            print("\nThank You for Using Smart Home Management System")
            print("Good Bye!")
            break

        else:
            print("Invalid Choice")

# -----------------------------
# Run Program
# -----------------------------
if __name__ == "__main__":
    main()
