from mycroft import MycroftSkill, intent_file_handler


class RedlineRunnerIntro(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('intro.runner.redline.intent')
    def handle_intro_runner_redline(self, message):
        self.speak_dialog('intro.runner.redline')


def create_skill():
    return RedlineRunnerIntro()

