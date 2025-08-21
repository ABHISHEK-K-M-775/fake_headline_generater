import random

print("hello")
subject = ["prithviraj sukumaran ","virat kohli ","putin ","glenn maxwell ","arnab goswami ","amish devagan ","hema malini "]
action=["doesnt like ","eats watching ","was offered a  role in ","is fond of ","loves ","is not good at "]
object=["pro kabaddi league","prime time news","bhojpuri film","great indian circus","you"]

while True:

    sub=random.choice(subject)
    act=random.choice(action)
    obj=random.choice(object)
    fake_news = f"Breaking news :study reveals {sub} {act} {obj}"
    print("\n"+fake_news)

    user_input = input(("\n d you want one maore fake news:(yes/no)")).strip().lower()
    
    if user_input == "no":
        break
print("thank you")
