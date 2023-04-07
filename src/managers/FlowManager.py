class FlowManager:
    def __init__(self, project, configuration):
        self.project = project
        self.configuration = configuration


    def get_names(self):
        steps = self.get_steps()
        names =  list(map(lambda item: item['step']['name'], steps))

        return names

    def get_callers(self):
        steps = self.get_steps()
        callers =  list(map(lambda item: item['step']['caller'], steps))

        return callers

    def get_steps(self):
        flows = self.configuration.get_configuration("flows")
        flows = map(lambda p: p["flow"], flows)
        flows = filter(lambda p: p["name"] == self.project, flows)
        steps = map(lambda p: p["steps"], flows)
        steps = next(steps, [])
        return steps

    def get_services(self):
        steps = self.get_steps()
        services = dict(map(lambda obj: (obj['step']['name'], obj['step']['caller']), steps))
        return services