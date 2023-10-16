class ChainInterface:
    def __init__(self, handlers):
        self.handlers = handlers

    def execute(self, context):
        for handler in self.handlers:
            handler(context).perform()
