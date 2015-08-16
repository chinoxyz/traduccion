

class Myrequest():
    """
    Class for mocking a request in view testing
    """
    data = {}
    session = {}
    def __init__(self,data={},user=None):
        self.data =data;
        self.query_params =data;
        self.POST = data;
        self.session = {}
        if user is not None:
            self.session["user"] = user.id