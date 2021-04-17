from abc import ABC

import json

from rest_framework.serializers import ListField

class Validator(ABC):

    fields = {} # All fields in format 'name': [type] e.g. 'title': str

    def __init__(self, data, *args, **kwargs):
        self.data = data
        self.validated_data = {}

    def validation(self, *args, **kwargs):
        ''' Individual validation here '''
        pass
        
    def is_valid(self, *args, **kwargs):
        print(self.data['choices'])

        # validate if data contains all fields
        for name, data_type in self.fields.items():
            if name in self.data.keys():
                # validate if data types are correct
                try:
                    self.validated_data[name] = data_type(self.data[name])
                except:
                    self.error = '"{name}" is not type {data_type}'.format(name=name, data_type=data_type)
                    return False

            else:
                self.error = '"{name}" does not exist!'.format(name=name)
                return False

        # validate validation
        try:
            self.error = self.validation(self, *args, **kwargs)
        except:
            self.error = 'An error occured, probably because the submission is invalid.'
            return False
        if error:
            return False
        
        return True

class Validation(ABC):
    def __init__(self, data, *args, **kwargs):
        self.data = data

    def validation(self, *args, **kwargs):
        ''' Individual validation here '''
        pass

    def is_valid(self, *args, **kwargs):
        try:
            self.validated_data = self.validation(self, *args, **kwargs)
            return True
        except:
            return False

class ListValidation(Validation):
    def validation(self, *args, **kwargs):
        return None
        


##### Custom validators #####

class PollValidator(Validator):

    fields = {
        'title': str,
        'description': str,
        'votes_amt': int,
        'less_allowed': bool,
        'show_while_running': bool,
        'date_to_start': str,
        'date_to_end': str,
        'choices': ListValidation,
    }

    def validation(self, *args, **kwargs):
        data = self.data
        if not data.title.isspace():
            return 'Title must contain at least one none-whitespace character!'
        if not data.description.isspace():
            return 'Description must contain at least one none-whitespace character!'
        if int(data.votes_amt) < 1:
            return 'Votes amount must be higher than 0!'
        