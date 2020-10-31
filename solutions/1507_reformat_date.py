class Solution:
    def reformatDate(self, date: str) -> str:
    	"""String.
    	"""
        months = {
            'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05',
            'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10',
            'Nov': '11', 'Dec': '12'
        }
        splits = date.split(' ')
        day = splits[0][:-2]
        return splits[2] + '-' + months[splits[1]] + '-' + '0' * (2 - len(day)) + day
