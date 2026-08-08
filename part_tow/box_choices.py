class Box:
    def __init__(self,request):
        # request is the request of the user or customer of site
        self.session= request.session
        # now jst we should set one  session attribute for box with up code
        box=self.session.get('session_key')
        # with up code we check the session part of the box for know about the product or targets on box user

        if 'session_key' not in request.session:
            box=self.session['session_key'] = {}
        self.box=box

# the role of this file is our main box for choice some character in our site
    def add(self,character):
        character_id=str(character.id)
        if character_id in self.box:
            pass
        else:
            self.box[character_id] = {
                'bounty_char': str(character.Height)
            }
            self.session.modified = True
    def __len__(self):
        return len(self.box)