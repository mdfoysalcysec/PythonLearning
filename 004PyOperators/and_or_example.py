user = 'admin'
log_info = True

if user=='admin' and log_info==True:
    print('Here, is your dashboard')
elif user=='admin' and log_info==False:
    print('User name is ok, But you need password')
else:
    print('Wrong information')



register_info = 'ok'
log_info = False
if register_info=='ok' or log_info==True:
    print('You can login')
else:
    print('You can\'t login')