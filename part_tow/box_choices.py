from part_one.models import Character,Personal_data


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
#         3 up lines we remake the box with session_key object
# the role of this file is our main box for choice some character in our site

    def add(self,character,quantity):
        character_id=str(character.id)
        character_qty =str(quantity)

        if character_id in self.box:
            pass
        else:
            self.box[character_id] = character_qty
            self.session.modified = True
    def __len__(self):
        return len(self.box)
    # below func jus for give character choice from session of the site
    def get_character(self):
        # for this part we should to give key of the our session (mean ==> self.box[character_id]) to find and set character in box
        character_id=self.box.keys()
        # so in up line we give our goal character for box
        character=Character.objects.filter(id__in=character_id)
        # and we filter the objects of character with filter and (id__in) methods
        # id__in method can search goal id on all the id characters
        return character
    def get_quants(self):
        quantities=self.box
        return quantities