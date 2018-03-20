class BonsaiClientError(Exception):
    """
    Generic wrapper for exceptions originating in client implementations
    """
    def __init__(self, msg, e):
        super().__init__("{}: {}".format(msg, repr(e)))
        self.original_exception = e


class SimulateError(BonsaiClientError):
    def __init__(self, e):
        super().__init__("Error in simulate", e)


class EpisodeStartError(BonsaiClientError):
    def __init__(self, e):
        super().__init__("Error in episode_start", e)


class BonsaiServerError(Exception):
    pass


class SimStateError(Exception):
    pass
