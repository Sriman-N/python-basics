#Short Circuiting
is_Friend = True
is_User = True

if is_Friend or is_User: #it won't care about the is_User because is_friend is already true and once we follow the or rules, it would be automatically true
    print('best friend forever')

is_friend = False
is_User = True

if is_friend and is_User: #it won't care about the is_user because is_friend is already false and once we follow the and rules, it would be false
    print('best friend forever')
