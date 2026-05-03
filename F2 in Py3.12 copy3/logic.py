from PyQt6.QtWidgets import *
from votegui import *
import csv
import os

class Logic(QMainWindow, Ui_voting_menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__user_ID = ''
        self.__user_selection = ''
        #keep track of votes as they are entered, set display labels equal to variables once finalized
        self.__isa_votes = 0
        self.__genji_votes = 0
        self.__hann_votes = 0
        self.__total = 0

        self.__search_ID = ''
        self.__content = ''
        self.votes_filename = 'votes.csv'
        if not os.path.exists(self.votes_filename):
            with open(self.votes_filename, "w") as file:
                writer = csv.writer(file)
                writer.writerow(['Voter ID, Voted for'])


        self.vote_bttn.clicked.connect(self.vote)
        self.candidate_options_group.buttonClicked.connect(self.candidate_selection)
        self.submit_id.clicked.connect(self.submit)
        self.done_button.clicked.connect(self.done)

    def vote(self):
        """
        displays instructions and voting options once user selects option to vote
        :return: None
        """
        self.instruct_label.setText("Select desired candidate.")
        self.isabella_select.setGeometry(70, 130, 100, 20)
        self.genji_select.setGeometry(70, 160, 100, 20)
        self.hannah_select.setGeometry(70, 190, 100, 20)
        self.voter_id_label.setGeometry(70, 230, 210, 15)
        self.voter_id.setGeometry(70, 255, 115, 20)

        self.error_message.setGeometry(70, 280, 230, 15)

    def verify_id(self):
        """
        checks validity of voter ID
        :return: True if user has not voted, False otherwise
        """
        self.__user_ID = self.voter_id.text().strip()
        if len(self.__user_ID) != 8:
            self.error_message.setText("Your ID should be 8 digits.")
            return False
        elif not self.__user_ID.isdigit():
            self.error_message.setText("Your ID should only contain numbers.")
            return False
        else:
            with open(self.votes_filename, 'r+') as votes_file:
                reader = csv.reader(votes_file)
                for row in reader:
                    if row[0] == self.__user_ID:
                        self.error_message.setText("You have already voted.")
                        return False
                return True

    def candidate_selection(self, button : QPushButton):
        """
        updates user selection variable for csv writing purposes
        :param button: QPushButton
        :return: None
        """
        self.__user_selection = button.text()
        self.submit_id.setGeometry(200, 250, 90, 30)


    def submit(self):
        """
        uses verify function and records voting if the function returns True
        :return: None
        """
        if self.verify_id():
            with open(self.votes_filename, 'a') as votes_file:
                writer = csv.writer(votes_file)
                writer.writerow((f'{self.__user_ID}', f'{self.__user_selection}'))
            self.error_message.setText("Vote successful.")
            self.submit_id.setGeometry(200, 250, 0, 0)
            self.voter_id.setText('')
            self.candidate_options_group.setExclusive(False)
            for button in self.candidate_options_group.buttons():
                button.setChecked(False)
            self.candidate_options_group.setExclusive(True)

    def done(self):
        """
        removes voting options
        :return: None
        """
        self.isabella_select.setGeometry(70, 130, 0, 0)
        self.genji_select.setGeometry(70, 160, 0, 0)
        self.hannah_select.setGeometry(70, 190, 0, 0)
        self.voter_id_label.setGeometry(70, 230, 0, 0)
        self.voter_id.setGeometry(70, 255, 0, 0)
        self.submit_id.setGeometry(200, 250, 0, 0)
        self.error_message.setGeometry(200, 280, 0, 0)












