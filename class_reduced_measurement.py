class ReducedMeasurement():
    def __init__(self, tissue, tvec_since_contact, fvec, zvec, is_corrected=False):
        self.is_corrected = is_corrected
        self.tissue = tissue
        self.timestamp = tvec_since_contact
        self.frequency = fvec
        self.z = zvec

