class Box:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        # اگر session_key وجود ندارد، یک دیکشنری خالی بساز
        if 'session_key' not in self.session:
            self.session['session_key'] = {}

        self.box = self.session['session_key']

    def add_character(self, character_id):
        """اضافه کردن کاراکتر به session"""
        if 'characters' not in self.box:
            self.box['characters'] = []

        if int(character_id) not in self.box['characters']:
            self.box['characters'].append(int(character_id))
            self.session.modified = True
            return True
        return False

    def get_characters(self):
        """دریافت لیست کاراکترها"""
        return self.box.get('characters', [])