from CrossReference import modify_name
devices = {}


class Device:

    def __init__(self, name):
        self.name = name  # also the name of the folder it's in
        self.backward_ref = []
        self.forward_ref = []
        self.authors = []
        self.date = ''
        self.publisher = ''
        self.sections = {}
        self.figures = {}
        self.citations = []


def init_device(name):
    # this assumes that a session has already been created
    new_device = Device(name)
    modified_name = modify_name(name)
    # add_forward_ref(new_device, modified_name, False, None)
    devices[modified_name] = new_device

    return new_device


def initialize_forward_ref():
    for device in devices:
        for ref in devices[device].backward_ref:
            if ref in devices:
                devices[ref].forward_ref.append(device)


# Parameters:
# device: device where backwardRef should be added
# ref_name: name of the reference (not modified)
def add_backward_ref(device, ref_name):
    ref_name = modify_name(ref_name)
    device.backward_ref.append(ref_name)


def get_devices():
    return devices