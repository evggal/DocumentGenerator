from API import to_send, to_accept
from Converter import Converter

d_vars: dict[str, str] = {
    'name': 'Роберт Полсон',
    'very': 'не очень',
    'hellblade': 'тут что-то',
    'varis': 'возможно'
}

conv = Converter('files/exam.docx', 'files/exam2.docx')
conv.replace_vars(d_vars)