import structures.functions.alphanumeric


class Inspector:

    def __init__(self):
        """

        """

        self.alphanumeric = structures.functions.alphanumeric.AlphaNumeric()

    def exc(self, model_id: int):

        schema = {'developerId': self.alphanumeric.numeric(),
                  'developerName': 'Ex',
                  'developerDesc': 'ML Consultancy',
                  'clientId': self.alphanumeric.numeric(),
                  'clientName': 'FCA',
                  'clientDesc': 'Financial Conduct Authority',
                  'auditId': self.alphanumeric.numeric(),
                  'auditIdComment': 'The universally unique audit identifier',
                  'auditDate': '2023-03-03',
                  'auditDateComment': 'The date the audit was completed',
                  'auditRequested': '2023-03-01',
                  'auditRequestedComment': 'The date the audit was requested',
                  'auditVersionNumber': 1,
                  'modelId': model_id}
