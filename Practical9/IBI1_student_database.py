class students(object):
    """
    Includes information about studentname,major,score for code,score for group,exam score coordinates of a point.
    """
    def __init__(self,studentname,major,score_for_code,score_for_group,examscore):
        self.studentname=studentname
        self.major=major
        self.score_for_code=score_for_code
        self.score_for_group=score_for_group
        self.examscore=examscore
print(students.__doc__)
Tom=students("Tom","BMS",90,90,88)
print(Tom.major)