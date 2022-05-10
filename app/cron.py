from .models import UserData

def reset_kudos():
    k = UserData.objects.all()
    k.update(kudos_available=3)
    print("Updated")
    pass
