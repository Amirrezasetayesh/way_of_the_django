from .box_choices import Box



def box(request):
    return {'box':Box(request)}


# this file is for global kardane Box class and after this file we can use the Box on all of our app and site