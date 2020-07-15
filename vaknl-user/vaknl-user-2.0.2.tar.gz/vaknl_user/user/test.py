
from vaknl_user import user

firestore_client = user.utils.create_firestore_client('vaknldev')
dmp_user_id = 'xxx'
u = user.user.User(dmp_user_id)
u.import_statistics(firestore_client)
# u.create_user_from_clickstream(firestore_client)
print(u)
u.statistics.general.activity_first_timestamp = 1
u.export_statistics(firestore_client)




