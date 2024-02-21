from datetime import datetime, timedelta

class Field:
    def __init__(self, name="Unused Field", growtime=0, value=0, crop_type=None,plant_time=None):
        self.name = name
        self.growtime = growtime
        self.value = value
        self.crop_type = crop_type
        self.plant_time = plant_time

    def plant_crops(self, crop_type):
        self.crop_type = crop_type
        self.plant_time = datetime.now()
        if crop_type == "Wheat":
            self.growtime = 200
        elif crop_type == "Corn":
            self.growtime = 100
        elif crop_type == "Canola":
            self.growtime = 400
        elif crop_type == "Barley":
            self.growtime = 50
        elif crop_type == "Potatoes":
            self.growtime = 600
        elif crop_type == "Grapes":
            self.growtime = 200
        else:
            self.growtime = 0

    def is_ready_to_harvest(self):
        if self.plant_time is None:
            return False
        else:
            current_time = datetime.now()
            time_elapsed = current_time - self.plant_time
            return time_elapsed.total_seconds() >= self.growtime

    def harvest(self):
            self.plant_time = None
            return self.value

    def random_event(self):
        event_option = random.randint(1,2)
        if event_option == 1:
            print("A swarm of locusts attacks your crops, killing them all off. Field is destroyed")
            self.plant_time = None
            self.crop_type = None
        elif event_option == 2:
            print("Its rained and flooded all your crops, Field is destroyed")
            self.plant_time = None
            self.crop_type = None

    def progress_bar(self):
        if self.plant_time is None:
            return "No crops planted"
        else:
            current_time = datetime.now()
            time_elapsed = current_time - self.plant_time
            progress = min(1.0, time_elapsed.total_seconds() / self.growtime)
            bar_length = 20
            filled_length = int(bar_length * progress)
            bar = '█' * filled_length + '-' * (bar_length - filled_length)
            return f"[{bar}] {progress * 100:.1f}%"